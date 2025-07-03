__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3') 

import os, sys, datetime, time
import streamlit as st
from crewai import Agent, Task, Crew, LLM

from core.budget_methods import get_budgets_list

from file_methods.csv_file_methods import extract_csv_content
from file_methods.md_file_methods import find_md_file_location
from file_methods.txt_file_methods import create_and_format_pretty_table

from crewai_toolkits_gem_2point0_flash.transform_csv_to_md_table import transformed_table

from utils.git_utils import git_push_md

def gen_report(): 
  GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY") 
  if not GOOGLE_API_KEY:
    st.error("\nGOOGLE_API_KEY environment variable not set. \nPlease set it as a secret in your GitHub repository. \nIf in command line/terminal, run the command: export GOOGLE_API_KEY='YOUR_API_KEY' ")
    st.stop() 
        
  llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.5,
    api_key=GOOGLE_API_KEY
  ) 

  analyser = Agent(
    role = "Transaction Intelligence Analyst",
    goal = '''Uncover strategic financial insights from {pretty_table} data and {budgets}:
    1. Behavioral spending patterns and customer segmentation
    2. Cash flow health and liquidity risk
    3. Recurring expense optimization opportunities
    4. Fraud and anomaly detection with contextual analysis
    5. Budget performance analysis (monthly/yearly spend vs allocation)
    ''',
    backstory = "Ex-McKinsey financial strategist specializing in transaction intelligence",
    verbose = True,
    llm = llm
  ) 

  rep_generator = Agent(
    role = "Financial Strategy Consultant",
    goal = """Transform analysis (got from Analyser) into actionable business intelligence:
    - Executive strategy brief
    - Behavioral segmentation profiles
    - Liquidity risk dashboard
    - Fraud prevention roadmap
    - Expense optimization plan
    - Budget recovery strategies (make a note of {budgets})""",
    backstory = "Lead report designer for Fortune 500 financial departments",
    verbose = True,
    llm = llm
  ) 

  analysis = Task(
    name = "Strategic Transaction Analysis",
    agent = analyser,
    description = """Conduct analysis of {pretty_table} data:
    - Net cash position trend (daily)
    - Top 5 cash inflow/outflow events
    - Customer segmentation by spending signature (impulse vs planned)
    - Life event detection via spending habit shifts
    - Subscription/cancellation patterns
    - Liquidity risk scoring (days of runway)
    - Fraud network analysis (common counterparties)
    - Recurring expense optimization opportunities
    - Payment method distribution
    - Transaction status analysis
    - Calculate % of monthly/yearly budget consumed using {budgets}
    - Identify budget overruns by category
    - Project year-end financial position
    - Quantify overspend impact on annual savings goals
    """,
    expected_output = "JSON with: cash_position, behavioral_segments, liquidity_risk, fraud_networks, expense_optimization"
  ) 

  to_do_rep_generation = Task(
    name = "Strategic Financial Brief",
    agent = rep_generator,
    description = """Create report using Strategic Transaction Analysis's output:
    - Executive Summary (key strategic insights)
    - Behavioral Segmentation Profiles
    - Liquidity Risk Dashboard
    - Fraud Network Mapping
    - Expense Optimization Plan
    - Budget Recovery Roadmap: % of Monthly and Yearly budget spent and best course of action to stay within budget
    - Appendix: Full transaction table, directly from {pretty_table}

    Format: Consultancy-style Markdown with data visualizations
    Use {budgets} if needed

    Section 5 will use {budgets}, and will have:
    - If monthly budget exceeded:
      a) Present Plan A: Full deduction from next month's budget
      b) Present Plan B: Proportional reduction across remaining months
    - Show 3-month cash flow forecast under each plan
    - Quantify annual savings impact of each strategy
    - Recommend optimal path based on liquidity risk profile""",
    expected_output = "Full report in Markdown format with 5 sections and appendix"
  )

  crewww = Crew(
    agents = [analyser, rep_generator],
    tasks = [analysis, to_do_rep_generation],
    process = 'sequential',
    verbose = True,
    chat_llm = llm
  )
  
  for attempt in range(5): 
      n = str(attempt+1).zfill(2) 
      try: 
        data_lines = extract_csv_content() 
        break 
      except Exception as e: 
        if attempt == 4:
          st.error(f"Failed to extract CSV content after 5 attempts: {e}") 
          st.stop() 
        time.sleep(3)  

  t_t_res = transformed_table(data_lines) 
  budgettt = get_budgets_list()

  try:
    m_bud = budgettt[0].replace("monthly = ", "").strip()
    y_bud = budgettt[1].replace("yearly = ", "").strip()
    bud_light = {"monthly" : float(m_bud), "yearly" : float(y_bud)}
  except:
    st.warning(f"Budget parse failed: {e}")
    bud_light = {"monthly" : 1000, "yearly" : 12000}

  res = crewww.kickoff(inputs = {"pretty_table": t_t_res, "budgets": bud_light})
 
  curr_md_path = find_md_file_location() 
  tst = datetime.datetime.today()  

  with open(curr_md_path, "w") as md_f:
    md_f.write(f"### Report Generated On: {str(tst)}") 
    md_f.write(" \n\n--- \n")
    md_f.write((res.raw.strip('```')).strip('markdown'))

  curr_md_path = find_md_file_location() 

  md_f_name = f"md_report_{tst.day}_{tst.month}_{tst.year}_{tst.hour}_{tst.minute}_{tst.second}.md"

  curr_dir = os.getcwd()
  saved_files_path = os.path.join(curr_dir, "saved_files")
  new_md_path = os.path.join(saved_files_path, md_f_name)

  os.rename(curr_md_path, new_md_path)
  git_push_md(new_md_path)

  return new_md_path

if __name__ == "__main__":
  gen_report()

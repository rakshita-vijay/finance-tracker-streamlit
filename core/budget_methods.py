import os, sys, re, math, datetime

import streamlit as st

from file_methods.csv_file_methods import extract_csv_content
from file_methods.txt_file_methods import find_txt_file_location
 
from utils.git_utils import git_push_txt

def get_budgets_list():
  with open("core/default_budget.txt", 'r') as f:
    f.seek(0)
    fr = f.read()
  frs = fr.split(', ')
  return frs

def displayBudget(budget_list):
  mb = re.search(r'monthly = (\d+)', budget_list[0].strip()).group(1)
  yb = re.search(r'yearly = (\d+)', budget_list[1].strip()).group(1)

  st.write("{} budget = {}".format('monthly'.title(), mb))

  budget_type = 'YEARLY'
  st.write("{bt} budget = {b}".format(bt = budget_type.title(), b = yb))

def changeBudget():
  st.write("")
  
  budget_type = st.selectbox(
    "Do you want to enter a monthly or yearly budget?",
    options=["NONE", "monthly", "yearly"] 
  )
 
  if budget_type != "NONE": 
    budget = None
    budget = st.number_input(
      f"Enter your {budget_type} budget:",
      min_value=0,
      value = int(((get_budgets_list()[0]).split(" = "))[1]) if budget_type == "monthly" else int(((get_budgets_list()[1]).split(" = "))[1])
    )  
   
    if budget != None: 
      if budget_type == "monthly":
        monthly_budget = budget
        yearly_budget = math.floor(budget * 12)
      else:
        monthly_budget = math.floor(budget / 12)
        yearly_budget = budget
    
      bl = f"monthly = {monthly_budget}, yearly = {yearly_budget}".split(', ')
      displayBudget(bl)
    
      f = open("core/default_budget.txt", 'w')
      f.write(f"monthly = {monthly_budget}, yearly = {yearly_budget}")
      f.close()
      
      git_push_txt()
      return True
  return False

'''
def calc_percent(prev_months_expenditure, curr_month_expenditure, bud_lst):
  tot_y_exp = prev_months_expenditure + curr_month_expenditure
  m_percent = float(curr_month_expenditure * 100.00 / bud_lst[0])
  y_percent = float(tot_y_exp * 100.00 / bud_lst[1])
  return m_percent, y_percent

def plan_b(m_or_y):
  if m_or_y == 'm':
    focus = "monthly"
  elif m_or_y == 'y':
    focus = "yearly"
  else:
    focus = "monthly AND yearly"

  st.warning(f"Your {focus} budget has exceeded")

def compare_with_budget():
  csv_content = extract_csv_content()

  t_now = datetime.datetime.today()
  month_now, year_now = t_now.month, t_now.year

  num_rows = len(csv_content)
  num_col = len(csv_content[0])

  curr_month_expenditure_rows, prev_months_expenditure_rows = [], []
  curr_month_expenditure, prev_months_expenditure = 0, 0

  for row in csv_content:
    m_d_y = row[1].split('/')
    if m_d_y[1] == month_now and m_d_y[2] == year_now:
      curr_month_expenditure_rows.append(row)
      curr_month_expenditure += row[3]
    elif m_d_y[1] < month_now and m_d_y[2] == year_now:
      prev_months_expenditure_rows.append(row)
      prev_months_expenditure += row[3]

  bud_lst = get_budgets_list()

  m_percent, y_percent = calc_percent(prev_months_expenditure, curr_month_expenditure, bud_lst)
  st.write("% of Monthly budget used: {}%".format(m_percent))
  st.write("% of Yearly budget used: {}%".format(y_percent))

  if m_percent > 100.00 and y_percent < 100.00:
    plan_b("m")
  elif m_percent < 100.00 and y_percent > 100.00:
    plan_b("y")
  elif m_percent > 100.00 and y_percent > 100.00:
    plan_b("m, y")
  else:
    st.write("You are going great! Expenses are under this month's budget, keep up the good work! :)")
'''

  # if it exceeds this month's budget, then i should ask user whether they want tto cut it completely form the next month's budget, or piecemeal througout the months left in the year
  # Calculate percentage of monthly and yearly budget used
  # Project year-end financial position based on current spending patterns
  # Show impact of different cut strategies on annual savings

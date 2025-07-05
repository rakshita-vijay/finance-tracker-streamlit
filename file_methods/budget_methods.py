import os, sys, re, math

import streamlit as st

from file_methods.csv_file_methods import extract_csv_content
from file_methods.txt_file_methods import find_txt_file_location

from utils.git_utils import git_push_txt

def find_budgets_file_location():
  curr_budgets = ""
  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[-19:] == 'default_budgets.txt':
        curr_budgets = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break
  return curr_budgets

def get_budgets_list():
  with open(find_budgets_file_location(), 'r') as f:
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
   with st.form("budget_form"):
      budget_type = st.selectbox(
         "Do you want to enter a monthly or yearly budget?",
         options=["NONE", "monthly", "yearly"]
      )
      budget = None
      if budget_type != "NONE":
         current_budgets = get_budgets_list()
         if budget_type == "monthly":
            default_val = int((current_budgets[0].split(" = "))[1])
         else:
            default_val = int((current_budgets[1].split(" = "))[1])
         budget = st.number_input(
            f"Enter your {budget_type} budget:",
            min_value=0,
            value=default_val,
            step=1
         )
      submitted = st.form_submit_button("Update Budget")
      if submitted and budget_type != "NONE" and budget is not None:
         if budget_type == "monthly":
            monthly_budget = budget
            yearly_budget = math.floor(budget * 12)
         else:
            monthly_budget = math.floor(budget / 12)
            yearly_budget = budget
         bl = f"monthly = {monthly_budget}, yearly = {yearly_budget}".split(', ')
         with open(find_budgets_file_location(), 'w') as f:
            f.write(f"monthly = {monthly_budget}, yearly = {yearly_budget}")
         git_push_txt(find_budgets_file_location(), "Update default budgets via Streamlit")
         return True
   return False

  # if it exceeds this month's budget, then i should ask user whether they want tto cut it completely form the next month's budget, or piecemeal througout the months left in the year
  # Calculate percentage of monthly and yearly budget used
  # Project year-end financial position based on current spending patterns
  # Show impact of different cut strategies on annual savings

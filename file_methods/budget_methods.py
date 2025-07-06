import streamlit as st
if 'username' not in st.session_state:
    st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']

import os, sys, re, math

from file_methods.csv_file_methods import extract_csv_content
from file_methods.txt_file_methods import find_txt_file_location
from file_methods.user_file_utils import get_user_file

from utils.git_utils import git_push_txt

def find_budgets_file_location():
  user_name = st.session_state['username']
  budgets_path = get_user_file(user_name, "budgets", "txt")
  return budgets_path

def get_budgets_list():
  try:
    with open(find_budgets_file_location(), 'r') as f:
      f.seek(0)
      fr = f.read()
    frs = fr.split(', ')
  except:
    st.warning(f"Unable to get budget from file: {find_budgets_file_location()}")
    frs = [500, 6000]
  return frs

def displayBudget(budget_list):
  try:
    mb = re.search(r'monthly = (\d+)', budget_list[0].strip()).group(1)
    yb = re.search(r'yearly = (\d+)', budget_list[1].strip()).group(1)
    st.write("{} budget = {}".format('monthly'.title(), mb))

    budget_type = 'YEARLY'
    st.write("{bt} budget = {b}".format(bt = budget_type.title(), b = yb))
  except:
    st.warning(f"Unable to get budget from file: {find_budgets_file_location()}")
    mb = 500
    yb = 6000
    st.write("{} budget = {}".format('monthly'.title(), mb))

    budget_type = 'YEARLY'
    st.write("{bt} budget = {b}".format(bt = budget_type.title(), b = yb))

def changeBudget():
  current_budgets = get_budgets_list()
  m_def = int((current_budgets[0].split(" = "))[1])
  y_def = int((current_budgets[1].split(" = "))[1])
  with st.form("budget_form"):
    budget_type = st.selectbox(
      "Do you want to enter a monthly or yearly budget?",
      options=["NONE", "monthly", "yearly"]
    )

    if budget_type != "NONE":
      budget = st.number_input(
        f"Enter your {budget_type} budget:",
        min_value=0,
        value=m_def if budget_type=="monthly" else y_def,
        step=1,
        key=f"{budget_type}_input",
        disabled=False
      )

    submitted = st.form_submit_button("Update Budget")
    if submitted and budget_type != "NONE":
      if budget_type == "monthly":
        monthly_budget = budget
        yearly_budget = math.floor(budget * 12)
      else:
        monthly_budget = math.floor(budget / 12)
        yearly_budget = budget

      with open(find_budgets_file_location(), 'w') as f:
        f.write(f"monthly = {monthly_budget}, yearly = {yearly_budget}")
      git_push_txt(find_budgets_file_location(), "Update default budgets via Streamlit")
      return True
  return False

  # if it exceeds this month's budget, then i should ask user whether they want tto cut it completely form the next month's budget, or piecemeal througout the months left in the year
  # Calculate percentage of monthly and yearly budget used
  # Project year-end financial position based on current spending patterns
  # Show impact of different cut strategies on annual savings

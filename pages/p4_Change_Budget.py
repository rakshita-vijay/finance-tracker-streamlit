import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']  

from pages.p0_Authentication import create_empty_files 
create_empty_files(username)

from file_methods.budget_methods import changeBudget, get_budgets_list, displayBudget

st.set_page_config(
  page_title="Change Budget",
  page_icon="💰",
  layout="wide",
  initial_sidebar_state="expanded"
)

from the_sidebar import the_sb
the_sb() 

def change_budget_button():
  st.page_link("pages/p4_Change_Budget.py", label="💰 Change Budget")

def change_budget_page():
  st.header("💰 Change Budget")
  st.divider()
  budget_list = get_budgets_list()
  st.subheader("Current Budgets")
  try:
    displayBudget(budget_list)
  except StopIteration:
    st.warning("Budget info not found or malformed.")
  st.divider()
  if changeBudget():
    st.success("Budget updated!")
    st.subheader("Updated Budgets")
    budget_list = get_budgets_list()
    displayBudget(budget_list)

change_budget_page()

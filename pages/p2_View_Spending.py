import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']  

from pages.p0_Authentication import create_empty_files 
create_empty_files(username)

from file_methods.budget_methods import get_budgets_list, displayBudget
from file_methods.csv_file_methods import extract_csv_content

st.set_page_config(
  page_title="View Spending",
  page_icon="📊",
  layout="wide",
  initial_sidebar_state="expanded"
)

from the_sidebar import the_sb
the_sb() 

def view_spending_button():
  st.page_link("pages/p2_View_Spending.py", label="📊 View Spending")

def view_spending_page():
  st.header("📊 View Spending")
  st.divider()

  # Get budgets as a list of strings like ['monthly = 5000', 'yearly = 60000']
  budget_list = get_budgets_list()
  st.subheader("Current Budgets")

  try:
    displayBudget(budget_list)
  except StopIteration:
    st.warning("Budget info not found or malformed.")

  st.divider()

  # Display transactions
  st.subheader("Transactions to Date")
  csv_content = extract_csv_content()
  if not csv_content:
    st.info("No transactions found.")
    return

  # Prepare table data
  headers = ["S.NO", "DATE", "DESCRIPTION", "AMOUNT", "PAYMENT METHOD", "STATUS", "NOTES"]
  rows = [dict(zip(headers, row)) for row in csv_content[1:]]

  st.table(rows)

view_spending_page()

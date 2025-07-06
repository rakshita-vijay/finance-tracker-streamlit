import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username'] 

from pages.p0_Authentication import authentication_button, create_empty_files(username)
create_empty_files(username)
from pages.p1_Add_Transactions import add_transactions_button
from pages.p2_View_Spending import view_spending_button
from pages.p3_Generate_Report import generate_report_button
from pages.p4_Change_Budget import change_budget_button
from pages.p5_Download_Files import download_files_button
from pages.p6_Wipe_Transactions import wipe_transactions_button
from pages.p7_Cleanup import cleanup_page_button

st.set_page_config(
  page_title="Finance Tracker",
  page_icon="💸",
  layout="wide",
  initial_sidebar_state="expanded"
)

with st.sidebar:
  st.markdown("## Main Menu")
  st.page_link("Main_Menu.py", label="Home", icon="🏠")
  st.page_link("pages/p0_Authentication.py", label="Authentication", icon="🔐")
  st.page_link("pages/p1_Add_Transactions.py", label="Add Transactions", icon="➕")
  st.page_link("pages/p2_View_Spending.py", label="View Spending", icon="📊")
  st.page_link("pages/p3_Generate_Report.py", label="Generate Report", icon="📝")
  st.page_link("pages/p4_Change_Budget.py", label="Change Budget", icon="💰")
  st.page_link("pages/p5_Download_Files.py", label="Download Files", icon="⬇️")
  st.page_link("pages/p6_Wipe_Transactions.py", label="Wipe Transactions", icon="🗑️")
  st.page_link("pages/p7_Cleanup.py", label="Cleanup", icon="🧹")

def main_menu_page():
  st.title("💸 Finance Tracker")
  st.write("Navigate using the sidebar to manage your finances, analyze trends, and generate reports.")
  st.divider()
  authentication_button()
  add_transactions_button()
  view_spending_button()
  generate_report_button()
  change_budget_button()
  download_files_button()
  wipe_transactions_button()
  cleanup_page_button()

main_menu_page()

import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']  

from pages.p0_Authentication import create_empty_files 
create_empty_files(username)

from file_methods.csv_file_methods import find_csv_file_location
from utils.git_utils import git_push_csv

st.set_page_config(
  page_title="Wipe Transactions",
  page_icon="🗑️",
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

def wipe_transactions_button():
  st.page_link("pages/p6_Wipe_Transactions.py", label="🗑️ Wipe Transactions")

def wipe_transactions_page():
  st.header("🗑️ Wipe Transactions")
  st.divider()
  if st.button("Wipe All Transactions"):
    csv_path = find_csv_file_location()
    with open(csv_path, "w") as f:
      f.write("S.NO,DATE,DESCRIPTION,AMOUNT,PAYMENT METHOD,STATUS,NOTES\n")
    st.success("All transactions wiped!")
  git_push_csv()

wipe_transactions_page()

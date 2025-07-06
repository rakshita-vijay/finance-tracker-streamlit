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

  # Step 1: Ask if user wants to wipe
  if "wipe_confirm" not in st.session_state:
    st.session_state.wipe_confirm = False

  if not st.session_state.wipe_confirm:
    if st.button("Wipe All Transactions"):
      st.session_state.wipe_confirm = True

  # Step 2: If confirmed, ask for password
  if st.session_state.wipe_confirm:
    pwd = st.text_input("Please enter your password to confirm wiping all transactions", type="password")
    col1, col2 = st.columns(2)
    with col1:
      if st.button("Confirm Wipe"):
        if pwd == st.session_state.get('password', ''):
          csv_path = find_csv_file_location()
          with open(csv_path, "w") as f:
            f.write("S.NO,DATE,DESCRIPTION,AMOUNT,PAYMENT METHOD,STATUS,NOTES\n")
          git_push_csv()
          st.success("All transactions wiped!")
          st.session_state.wipe_confirm = False
        else:
          st.error("Incorrect password. Transactions not wiped.")
    with col2:
      if st.button("Cancel"):
        st.session_state.wipe_confirm = False

'''
def wipe_transactions_page():
  st.header("🗑️ Wipe Transactions")
  st.divider()
  if st.button("Wipe All Transactions"):
    csv_path = find_csv_file_location()
    with open(csv_path, "w") as f:
      f.write("S.NO,DATE,DESCRIPTION,AMOUNT,PAYMENT METHOD,STATUS,NOTES\n")
    st.success("All transactions wiped!")
  git_push_csv()
'''

wipe_transactions_page()

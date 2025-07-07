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

from the_sidebar import the_sb
the_sb() 

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
  dunnit = False
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
          # st.success("All transactions wiped!")
          dunnit = True
          st.session_state.wipe_confirm = False
        else:
          st.error("Incorrect password. Transactions not wiped.")
    with col2:
      if st.button("Cancel"):
        st.session_state.wipe_confirm = False
        
  if dunnit:
    st.success("All transactions wiped!")

maybe_it = '''
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

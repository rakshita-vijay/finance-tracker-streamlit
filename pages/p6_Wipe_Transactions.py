import streamlit as st
from file_methods.csv_file_methods import find_csv_file_location
from utils.git_utils import git_push_csv

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

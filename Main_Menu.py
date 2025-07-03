__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3') 

import streamlit as st
from pages.p1_Add_Transactions import add_transactions_button
from pages.p2_View_Spending import view_spending_button
from pages.p3_Generate_Report import generate_report_button
from pages.p4_Change_Budget import change_budget_button
from pages.p5_Download_Files import download_files_button
from pages.p6_Wipe_Transactions import wipe_transactions_button

st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main {background-color: #18141A;}
    .stApp {background-color: #18141A;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💸 Finance Tracker")
st.write("Navigate using the sidebar to manage your finances, analyze trends, and generate reports.")
st.divider()
add_transactions_button()
view_spending_button()
generate_report_button()
change_budget_button()
download_files_button()
wipe_transactions_button()

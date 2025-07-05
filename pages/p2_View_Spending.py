import streamlit as st
if 'username' not in st.session_state:
    st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']

from file_methods.budget_methods import get_budgets_list, displayBudget
from file_methods.csv_file_methods import extract_csv_content

st.set_page_config(
    page_title="View Spending",
    page_icon="📊",
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

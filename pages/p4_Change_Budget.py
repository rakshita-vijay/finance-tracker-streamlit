import streamlit as st
from core.budget_methods import changeBudget, get_budgets_list, displayBudget

st.set_page_config(
    page_title="Change Budget",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
) 

with st.sidebar:
    st.markdown("## Main Menu")
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/p1_Add_Transactions.py", label="Add Transactions", icon="➕")
    st.page_link("pages/p2_View_Spending.py", label="View Spending", icon="📊")
    st.page_link("pages/p3_Generate_Report.py", label="Generate Report", icon="📝")
    st.page_link("pages/p4_Change_Budget.py", label="Change Budget", icon="💰")
    st.page_link("pages/p5_Download_Files.py", label="Download Files", icon="⬇️")
    st.page_link("pages/p6_Wipe_Transactions.py", label="Wipe Transactions", icon="🗑️")
    st.page_link("pages/p7_Cleanup.py", label="Cleanup", icon="🧹")  

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

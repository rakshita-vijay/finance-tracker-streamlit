import streamlit as st
from core.budget_methods import get_budgets_list, displayBudget
from file_methods.csv_file_methods import display_csv_content
 
def view_spending_button():
    st.page_link("pages/p2_View_Spending.py", label="📊 View Spending") 

def view_spending_page():
    st.header("📊 View Spending")

    view_spend = st.button("View Spending")
    if view_spend:
        budgets = get_budgets_list()
        st.write("**Current Budgets:**")
        displayBudget(budgets)
        st.write("---")
        st.write("**Transactions to Date:**")
        display_csv_content() 

view_spending_page()

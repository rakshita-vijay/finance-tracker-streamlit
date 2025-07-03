import streamlit as st
from core.budget_methods import get_budgets_list, displayBudget
from file_methods.csv_file_methods import display_csv_content
 
def view_spending_button():
    st.page_link("pages/2_View_Spending.py", label="📊 View Spending") 

st.header("📊 View Spending")
budgets = get_budgets_list()
st.write("**Current Budgets:**")
displayBudget(budgets)
st.write("---")
st.write("**Transactions to Date:**")
display_csv_content()

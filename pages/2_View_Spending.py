import streamlit as st
from core.budget_methods import get_budgets_list, displayBudget
from file_methods.csv_file_methods import display_csv_content

st.header("📊 View Spending")
budgets = get_budgets_list()
st.write("**Current Budgets:**")
displayBudget(budgets)
st.write("---")
st.write("**Transactions to Date:**")
display_csv_content()

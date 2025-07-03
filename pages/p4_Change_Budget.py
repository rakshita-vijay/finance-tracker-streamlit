import streamlit as st
from core.budget_methods import changeBudget, get_budgets_list, displayBudget

def change_budget_button():
    st.page_link("pages/4_Change_Budget.py", label="💰 Change Budget")

st.header("💰 Change Budget")
budgets = get_budgets_list()
st.write("**Current Budgets:**")
displayBudget(budgets)
if st.button("Change Budget"):
    changeBudget()
    st.success("Budget updated!")

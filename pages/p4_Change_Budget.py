import streamlit as st
from core.budget_methods import changeBudget, get_budgets_list, displayBudget

def change_budget_button():
    st.page_link("pages/p4_Change_Budget.py", label="💰 Change Budget")

def change_budget_page():
    st.header("💰 Change Budget") 
    st.divider()
    budget_list = get_budgets_list()
    st.subheader("Current Budgets")
    displayBudget(budget_list) 
 
    try:
        monthly = next(s for s in budget_list if 'monthly' in s.lower())
        yearly = next(s for s in budget_list if 'yearly' in s.lower())
        st.write(f"**{monthly.title()}**")
        st.write(f"**{yearly.title()}**")
    except StopIteration:
        st.warning("Budget info not found or malformed.") 
        
    st.divider()
        
    if st.button("Change Budget"):
        changeBudget()
        
        st.success("Budget updated!")
        
        st.subheader("Updated Budgets")
        budget_list = get_budgets_list()
        displayBudget(budget_list)

change_budget_page() 

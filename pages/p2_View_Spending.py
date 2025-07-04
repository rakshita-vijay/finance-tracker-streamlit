import streamlit as st
from core.budget_methods import get_budgets_list, displayBudget
from file_methods.csv_file_methods import extract_csv_content

def view_spending_button():
    st.page_link("pages/p2_View_Spending.py", label="📊 View Spending")

def view_spending_page():
    st.header("📊 View Spending")
    st.divider()

    # Get budgets as a list of strings like ['monthly = 5000', 'yearly = 60000']
    budget_list = get_budgets_list()
    st.subheader("Current Budgets")
    displayBudget(budget_list)  
 
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

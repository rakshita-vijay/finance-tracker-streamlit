import streamlit as st
from core.budget_methods import get_budgets_list, displayBudget
from file_methods.csv_file_methods import extract_csv_content

def view_spending_page():
    st.header("📊 View Spending")

    # Get budgets as a list of strings like ['monthly = 5000', 'yearly = 60000']
    budget_list = get_budgets_list()
    st.subheader("Current Budgets")
    displayBudget(budget_list)  # This prints budgets to console; let's also display in Streamlit

    # Additionally, display budgets in Streamlit
    try:
        monthly = next(s for s in budget_list if 'monthly' in s.lower())
        yearly = next(s for s in budget_list if 'yearly' in s.lower())
        st.write(f"**{monthly.title()}**")
        st.write(f"**{yearly.title()}**")
    except StopIteration:
        st.warning("Budget info not found or malformed.")

    # Display transactions
    st.subheader("Transactions to Date")
    csv_content = extract_csv_content()
    if not csv_content:
        st.info("No transactions found.")
        return

    # Prepare table data
    headers = ["S.NO", "DATE", "DESCRIPTION", "AMOUNT", "PAYMENT METHOD", "STATUS", "NOTES"]
    rows = [dict(zip(headers, row)) for row in csv_content]

    st.table(rows)

view_spending_page() 

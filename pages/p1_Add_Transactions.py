import streamlit as st
from file_methods.csv_file_methods import add_to_csv 
from file_methods.txt_file_methods import update_txt_file 

def add_transactions_button():
    st.page_link("pages/p1_Add_Transactions.py", label="➕ Add Transactions")
    
def add_transactions_page():
    st.header("➕ Add Transaction(s)")
    num = st.number_input("How many transactions to add?", min_value=1, max_value=20, value=1)
    all_trans = []
    errors = []

    for i in range(num):
        st.subheader(f"Transaction #{i+1}")
        with st.form(key=f"form_{i}", clear_on_submit=False):
            date = st.date_input("Date (MM/DD/YYYY or MM-DD-YYYY)", key=f"date_{i}") 
            desc = st.text_input("Description", key=f"desc_{i}")
            amt = st.number_input("Amount", key=f"amt_{i}")
            pay_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Debit Card", "Bank Transfer", "UPI", "Other"], key=f"pay_{i}")
            status = st.selectbox("Status", ["Completed", "Pending", "Failed", "Cancelled"], key=f"status_{i}")
            notes = st.text_area("Notes", key=f"notes_{i}")
            submitted = st.form_submit_button("Submit")

            if submitted:
                # Validation
                if not date:
                    errors.append(f"Transaction #{i+1}: Date is required.")
                if not desc.strip():
                    errors.append(f"Transaction #{i+1}: Description is required.")
                if amt == 0:
                    errors.append(f"Transaction #{i+1}: Amount cannot be zero.")
                if errors:
                    for err in errors:
                        st.error(err)
                else:
                    all_trans.append([None, date, desc, amt, pay_method, status, notes])
                    st.success(f"Transaction #{i+1} added!")

    if all_trans:
        add_to_csv(all_trans)
        # Auto-update TXT, PDF, MD after CSV update 
        update_txt_file() 
        st.success("All files updated after adding transactions.")

add_transactions_page() 

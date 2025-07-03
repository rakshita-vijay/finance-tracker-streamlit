import streamlit as st
from file_methods.csv_file_methods import get_trans_line_details, add_to_csv

st.header("➕ Add Transaction(s)")

num = st.number_input("How many transactions do you want to add?", min_value=1, max_value=20, value=1)

if st.button("Add Transactions"):
    all_trans = []
    for i in range(num):
        st.subheader(f"Transaction #{i+1}")
        with st.form(key=f"form_{i}"):
            date = st.text_input("Date (MM/DD/YYYY or MM-DD-YYYY)")
            desc = st.text_input("Description")
            amt = st.number_input("Amount", value=0.0)
            pay_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Debit Card", "Bank Transfer", "UPI", "Other"])
            status = st.selectbox("Status", ["Completed", "Pending", "Failed", "Cancelled"])
            notes = st.text_area("Notes")
            submitted = st.form_submit_button("Submit")
            if submitted:
                all_trans.append([None, date, desc, amt, pay_method, status, notes])
    if all_trans:
        add_to_csv(all_trans)
        st.success("Transactions added!")

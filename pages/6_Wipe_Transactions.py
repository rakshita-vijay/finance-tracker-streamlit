import streamlit as st
from file_methods.csv_file_methods import find_csv_file_location

st.header("🗑️ Wipe Transactions")
if st.button("Wipe All Transactions"):
    csv_path = find_csv_file_location()
    with open(csv_path, "w") as f:
        f.write("S.NO,DATE,DESCRIPTION,AMOUNT,PAYMENT METHOD,STATUS,NOTES\n")
    st.success("All transactions wiped!")

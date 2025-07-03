import streamlit as st
from file_methods.csv_file_methods import add_to_csv, find_csv_file_location
from file_methods.txt_file_methods import update_txt_file 
from utils.git_utils import git_push_csv

def setup_git_repo():
    try:
        GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
        repo = git.Repo(".")
        username = "rakshita-vijay"
        repo_url = f"https://{username}:{GITHUB_TOKEN}@github.com/{username}/automated-onboarder.git"
        repo.remote().set_url(repo_url)
        st.success("Using existing Git repository!")
        return repo
    except git.exc.InvalidGitRepositoryError:
        st.error("Not in a Git repository. Make sure you're running from your repo directory.")
        return None

def add_transactions_button():
    st.page_link("pages/p1_Add_Transactions.py", label="➕ Add Transactions")
    
def add_transactions_page():
    st.header("➕ Add Transaction(s)")
    
    st.divider() 
    num = st.number_input("How many transactions to add?", min_value=1, max_value=20, value=1)
    all_trans = []
    errors = []

    st.divider()

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
        update_txt_file()
        # Push to GitHub
        push_success, push_msg = git_push_csv(find_csv_file_location())
        if push_success:
            st.success("All files updated after adding transactions!")
        else:
            st.warning(push_msg)
         
add_transactions_page() 

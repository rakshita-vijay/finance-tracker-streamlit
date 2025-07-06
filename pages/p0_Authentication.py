import streamlit as st
import os, csv

from file_methods.user_file_utils import ensure_user_dir

from utils.git_utils import git_push_txt, git_push_csv, git_push_md, git_push_pdf

st.set_page_config(
    page_title="Authentication",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

def authentication_button():
    st.page_link("pages/p0_Authentication.py", label="🔐 Authentication") 
    
CRED_FILE = "saved_files/user_credentials.txt"

def check_credentials(username, password):
    if not os.path.exists(CRED_FILE):
        return False
    with open(CRED_FILE, "r") as f:
        for line in f:
            u, p = line.strip().split(":", 1)
            if u == username and p == password:
                return True
    return False

def create_empty_files(username, user_dir):  
    file_list = [
        f"{username}_csv_transactions.csv",
        f"{username}_ascii_table_of_transactions.txt",
        f"{username}_pdf_of_transactions.pdf",
        f"{username}_md_report.md",
        f"{username}_budgets.txt"
    ]
    for fname in file_list:
        path = os.path.join(user_dir, fname) 
        if fname.endswith('.pdf'):
            open(path, "wb").close()
            git_push_pdf(path)
        elif fname.endswith('.csv'):
            fields = ['S.NO', 'DATE', 'DESCRIPTION', 'AMOUNT', 'PAYMENT METHOD', 'STATUS', 'NOTES'] 
            with open(path, "w", newline='') as csv_f:
                csv_writer = csv.writer(csv_f, delimiter=',')
                csv_writer.writerow(fields)
            git_push_csv(path)
        else:
            open(path, "w").close() 
            if fname.split(".")[1] == 'txt':
                git_push_txt(path)
            elif fname.split(".")[1] == 'md':
                git_push_md(path)
                
def register_user(username, password):
    user_dir = f"saved_files/{username}"
    os.makedirs(user_dir, exist_ok=True)
    with open(CRED_FILE, "a") as f:
        f.write(f"{username}: {password}\n")
    git_push_txt(CRED_FILE)
    create_empty_files(username, user_dir)

def check_and_recreate_user_files(username):
    user_dir = os.path.join('saved_files', username)
    ensure_user_dir(username)
    file_list = [
        f"{username}_csv_transactions.csv",
        f"{username}_ascii_table_of_transactions.txt",
        f"{username}_pdf_of_transactions.pdf",
        f"{username}_md_report.md",
        f"{username}_budgets.txt"
    ] 
    missing_files = []
    for fname in file_list:
        path = os.path.join(user_dir, fname)
        if not os.path.exists(path):
            missing_files.append(fname)
    if missing_files:
        create_empty_files(username, user_dir)

def authentication_page():
    st.title("🔐 Login or Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    mode = st.radio("Login or Register", ["Login", "Register"])
    if st.button("Submit"):
        if not username or not password:
            st.error("Please enter both username and password.")
            return
        if mode == "Login":
            if check_credentials(username, password):
                st.session_state['username'] = username
                st.session_state['password'] = password
                st.success("Login successful!")
                st.switch_page("pages/m_Main_Menu.py")  
            else:
                st.error("Invalid credentials.")
        else:
            if check_credentials(username, password):
                st.error("User already exists.")
            else:
                register_user(username, password)
                st.session_state['username'] = username
                st.session_state['password'] = password 
                ensure_user_dir(username)
                check_and_recreate_user_files(username)
                st.success("Registration successful!")
                st.switch_page("pages/m_Main_Menu.py") 
 
authentication_page()

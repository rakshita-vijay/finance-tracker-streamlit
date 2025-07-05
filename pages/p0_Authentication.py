import streamlit as st
import os

from file_methods.user_file_utils import ensure_user_dir

st.set_page_config(
    page_title="Authentication",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
) 

with st.sidebar:
    st.markdown("## Main Menu")
    st.page_link("Main_Menu.py", label="Home", icon="🏠")
    st.page_link("pages/p0_Authentication.py", label="Authentication", icon="🔐")
    st.page_link("pages/p1_Add_Transactions.py", label="Add Transactions", icon="➕")
    st.page_link("pages/p2_View_Spending.py", label="View Spending", icon="📊")
    st.page_link("pages/p3_Generate_Report.py", label="Generate Report", icon="📝")
    st.page_link("pages/p4_Change_Budget.py", label="Change Budget", icon="💰")
    st.page_link("pages/p5_Download_Files.py", label="Download Files", icon="⬇️")
    st.page_link("pages/p6_Wipe_Transactions.py", label="Wipe Transactions", icon="🗑️")
    st.page_link("pages/p7_Cleanup.py", label="Cleanup", icon="🧹") 

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

def register_user(username, password):
    os.makedirs(f"saved_files/{username}", exist_ok=True)
    with open(CRED_FILE, "a") as f:
        f.write(f"{username}:{password}\n")

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
                st.experimental_rerun()
            else:
                st.error("Invalid credentials.")
        else:
            if check_credentials(username, password):
                st.error("User already exists.")
            else:
                register_user(username, password)
                st.session_state['username'] = username
                st.session_state['password'] = password
                st.success("Registration successful!")
                st.experimental_rerun()
                ensure_user_dir(username)

if 'username' not in st.session_state:
    authentication_page()
    st.stop() 

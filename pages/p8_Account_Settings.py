import streamlit as st
if 'username' not in st.session_state:
    st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username'] 
password = st.session_state['password'] 

import shutil
import os
import git

from utils.git_utils import git_push_txt

st.set_page_config(
    page_title="Account Settings",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
) 

from the_sidebar import the_sb
the_sb() 

def account_settings_button():
    st.page_link("pages/p8_Account_Settings.py", label="⚙️ Account Settings")

def account_settings_page():
    st.title("⚙️ Account Settings")
    
    st.divider()
    st.write(f"Logged in as: **{username}**")
    st.divider()
    
    # Log Out button
    if st.button("⏻ Log Out"):
        # Clear all session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun() 

    if username == "demo":
        st.error("Sorry, this is the demo account. You cannot delete this account :(")
        
    else: 
        # Delete Account flow
        if 'delete_confirm' not in st.session_state:
            st.session_state.delete_confirm = False
        
        if not st.session_state.delete_confirm:
            if st.button("⌫ Delete Account"):
                st.session_state.delete_confirm = True
        
        if st.session_state.delete_confirm:
            pwd_input = st.text_input("Enter your password to confirm account deletion", type="password") 
            
            if st.button("Confirm Deletion"):
                if pwd_input == password:
                    user_folder = os.path.join("saved_files", username) 
                    
                    try:
                        shutil.rmtree(user_folder)
                        
                        user_dir = f"saved_files/{username}"
                        os.makedirs(user_dir, exist_ok=True)
                        from pages.p0_Authentication import create_empty_files
                        create_empty_files(username)
                    except Exception as e:
                        st.error(f"Error deleting user data: {e}")
                        st.stop()  
                        
                    # Remove user credentials from credentials file
                    cred_file = "saved_files/user_credentials.txt" 
                    
                    try:
                        with open(cred_file, "r") as f:
                            lines = f.readlines()
                        with open(cred_file, "w") as f:
                            for line in lines:
                                if not line.startswith(f"{username}:"):
                                    f.write(line) 
                        git_push_txt(cred_file, "Updated credentials doc via Streamlit")
                        
                    except Exception as e:
                        st.error(f"Error updating credentials file: {e}")
                        st.stop()
                    
                    # Clear session and redirect to login
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                    st.success("Account deleted successfully. Redirecting to login page...")
                    st.switch_page("pages/p0_Authentication.py")
                    st.rerun()  # or st.rerun()
                else:
                    st.error("Incorrect password. Account not deleted.") 

account_settings_page()

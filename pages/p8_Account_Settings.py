import streamlit as st
if 'username' not in st.session_state:
    st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username'] 
password = st.session_state.get('password', '')

import shutil
import os

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
    st.write(f"Logged in as: **{username}**")
    
    # Log Out button
    if st.button("⏻ Log Out"):
        # Clear all session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()  # or st.rerun() depending on Streamlit version
    
    st.divider()
    
    # Delete Account flow
    if 'delete_confirm' not in st.session_state:
        st.session_state.delete_confirm = False
    
    if not st.session_state.delete_confirm:
        if st.button("⌫ Delete Account"):
            st.session_state.delete_confirm = True
    
    if st.session_state.delete_confirm:
        pwd_input = st.text_input("Enter your password to confirm account deletion", type="password")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Confirm Deletion"):
                if pwd_input == password:
                    user_folder = os.path.join("saved_files", username)
                    try:
                        shutil.rmtree(user_folder)
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
                    except Exception as e:
                        st.error(f"Error updating credentials file: {e}")
                        st.stop()
                    # Clear session and redirect to login
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                    st.success("Account deleted successfully. Redirecting to login page...")
                    st.experimental_rerun()  # or st.rerun()
                else:
                    st.error("Incorrect password. Account not deleted.")
        with col2:
            if st.button("Cancel"):
                st.session_state.delete_confirm = False 

account_settings_page()

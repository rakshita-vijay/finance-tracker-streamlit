import streamlit as st
if 'username' not in st.session_state:
    st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']

import os

def get_user_file(username, basename, ext):
    """Returns the full path for a user's file with the given suffix."""
    return os.path.join("saved_files", username, f"{username}_{basename}.{ext}") 

def ensure_user_dir(username):
    os.makedirs(os.path.join("saved_files", username), exist_ok=True) 

import os, glob

from file_methods.user_file_utils import get_user_file

import streamlit as st

if 'username' not in st.session_state:
    st.warning("Please login first.")
    st.stop()
username = st.session_state['username']

def find_md_file_location(): 
  md_path = get_user_file(username, "md_report", "md") 
  return md_path 

def save_and_cleanup_md_report(md_content, timestamp, md_filename="md_report.md", saved_files_dir="saved_files"):
  md_path = os.path.join(saved_files_dir, md_filename)
  with open(md_path, "w") as f:
    f.write(f"### Report Generated On: {str(timestamp)}") 
    f.write(" \n\n--- \n")
    f.write(md_content) 
    
  curr_md_path = ''.join(os.path.join(os.getcwd(), md_path).split('./'))
  return curr_md_path

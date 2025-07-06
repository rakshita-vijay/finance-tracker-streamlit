import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']

import os, glob

from file_methods.user_file_utils import get_user_file

def find_md_file_location():
  user_name = st.session_state['username']
  md_path = get_user_file(user_name, "md_report", "md")
  return md_path 

def save_and_cleanup_md_report(md_content, timestamp, md_path = "NOT ENTERED"): 
  if md_path == "NOT ENTERED":
    md_path = find_md_file_location() 
    
  with open(md_path, "w") as f:
    f.write(f"### Report Generated On: {str(timestamp)}")
    f.write(" \n\n--- \n")
    f.write(md_content)

  curr_md_path = ''.join(os.path.join(os.getcwd(), md_path).split('./'))
  return curr_md_path 

import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']  

from pages.p0_Authentication import create_empty_files 
create_empty_files(username)

from download_to_device import cleanup_pycache_and_temp_files

st.set_page_config(
  page_title="Cleanup",
  page_icon="🧹",
  layout="wide",
  initial_sidebar_state="expanded"
)

from the_sidebar import the_sb
the_sb() 

def cleanup_page_button():
  st.page_link("pages/p7_Cleanup.py", label="🧹 Cleanup")

def cleanup_page():
  st.header("🧹 Cleanup Temporary Files")
  st.divider()
  if st.button("Run Cleanup"):
    cleanup_pycache_and_temp_files()
    st.success("Cleanup complete!")

cleanup_page()

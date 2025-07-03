import streamlit as st
from download_to_device import cleanup_pycache_and_temp_files

def cleanup_page_button(): 
    st.page_link("pages/p7_Cleanup.py", label="🗑️ Cleanup")   
  
def cleanup_page():
    st.header("🧹 Cleanup Temporary Files")
    if st.button("Run Cleanup"):
        cleanup_pycache_and_temp_files()
        st.success("Cleanup complete!")

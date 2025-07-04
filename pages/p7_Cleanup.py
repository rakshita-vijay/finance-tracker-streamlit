import streamlit as st
from download_to_device import cleanup_pycache_and_temp_files

st.set_page_config(
    page_title="Cleanup",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded"
)

def cleanup_page_button(): 
    st.page_link("pages/p7_Cleanup.py", label="🧹 Cleanup") 
  
def cleanup_page():
    st.header("🧹 Cleanup Temporary Files")
    st.divider()
    if st.button("Run Cleanup"):
        cleanup_pycache_and_temp_files()
        st.success("Cleanup complete!")

cleanup_page()

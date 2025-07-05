import streamlit as st
if 'username' not in st.session_state:
    st.warning("Please login first.")
    st.stop()
username = st.session_state['username']

from download_to_device import cleanup_pycache_and_temp_files

st.set_page_config(
    page_title="Cleanup",
    page_icon="🧹",
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

def cleanup_page_button(): 
    st.page_link("pages/p7_Cleanup.py", label="🧹 Cleanup") 
  
def cleanup_page():
    st.header("🧹 Cleanup Temporary Files")
    st.divider()
    if st.button("Run Cleanup"):
        cleanup_pycache_and_temp_files()
        st.success("Cleanup complete!")

cleanup_page()

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3') 

import streamlit as st
if 'username' not in st.session_state:
    st.switch_page("pages/p0_Authentication.py") 
 
from pages.m_Main_Menu import main_menu_page 

st.markdown(
    """
    <style>
    .main {background-color: #18141A;}
    .stApp {background-color: #18141A;}
    </style>
    """,
    unsafe_allow_html=True
) 

st.switch_page("pages/m_Main_Menu.py") 

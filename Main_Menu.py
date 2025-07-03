import streamlit as st

st.set_page_config(
    page_title="Finance Tracker",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .main {background-color: #18141A;}
    .stApp {background-color: #18141A;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💸 Finance Tracker")
st.write("Navigate using the sidebar to manage your finances, analyze trends, and generate reports.")

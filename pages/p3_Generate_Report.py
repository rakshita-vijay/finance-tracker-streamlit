import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']  

from pages.p0_Authentication import create_empty_files 
create_empty_files(username)

import os, time

from file_methods.md_file_methods import find_md_file_location
from download_to_device import download_file

from crewai_toolkits_gem_2point0_flash.generate_report_from_csv import gen_report

from utils.git_utils import git_push_md

st.set_page_config(
  page_title="Generate Report",
  page_icon="📝",
  layout="wide",
  initial_sidebar_state="expanded"
)

from the_sidebar import the_sb
the_sb() 

def generate_report_button():
  st.page_link("pages/p3_Generate_Report.py", label="📝 Generate Report")

def generate_report_page():
  st.header("📝 Generate AI Report")
  st.divider()

  md_path = "saved_files/md_report.md"

  if st.button("Generate Report"):
    st.divider()
    with st.spinner("Generating your report..."):
      try:
        md_path = gen_report()
        with open(md_path, "r") as f:
          st.markdown(f.read())
      except Exception as e:
        st.error(f"Error during report generation: {e}")

  git_push_md(md_path)
  st.divider()
  if os.path.isfile(md_path):
    with open(md_path, "rb") as f:
      if st.download_button(
        label="Download Report",
        data=f,
        file_name=os.path.basename(md_path),
        mime="text/markdown"):
        st.success(f"\nDownload of file: {os.path.basename(md_path)} complete! Check your downloads folder :)")

generate_report_page()

import os, time
import streamlit as st

from file_methods.md_file_methods import find_md_file_location
from download_to_device import download_file

from crewai_toolkits_gem_2point0_flash.generate_report_from_csv import gen_report 

from utilsgit_utils import git_push_md
 
def generate_report_button():
    st.page_link("pages/p3_Generate_Report.py", label="📝 Generate Report") 

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
            
git_push_md()
st.divider()            
if os.path.isfile(md_path): 
    with open(md_path, "rb") as f:
        if st.download_button(
            label="Download Report",
            data=f,
            file_name=os.path.basename(md_path),
            mime="text/markdown"):
            st.success(f"\nDownload of file: {os.path.basename(md_path)} complete! Check your downloads folder :)")  

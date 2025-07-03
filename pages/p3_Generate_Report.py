import time
import streamlit as st

from file_methods.md_file_methods import find_md_file_location
from download_to_device import download_file

from crewai_toolkits_gem_2point0_flash.generate_report_from_csv import gen_report 
 
def generate_report_button():
    st.page_link("pages/p3_Generate_Report.py", label="📝 Generate Report") 

st.header("📝 Generate AI Report")

st.divider()

if st.button("Generate Report"): 
    st.divider()
    with st.spinner("Generating your report..."): 
        try:
            md_path = gen_report()
            time.sleep(3) 
            
            with open(md_path, "r") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Error during report generation: {e}") 
            
st.divider()            
if os.path.isfile(md_path): 
    with open(md_path, "rb") as f:
        st.download_button(
            label="Download Report",
            data=f,
            file_name=os.path.basename(md_path),
            mime="text/markdown"
        ) 

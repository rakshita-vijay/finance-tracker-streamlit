import time
import streamlit as st
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
            
            # st.success("Report generated!")
            # st.write(f"Markdown report saved at: `{md_path}`")
            # st.divider()
            
            with open(md_path, "r") as f:
                st.markdown(f.read())
        except Exception as e:
            st.error(f"Error during report generation: {e}") 

import streamlit as st
from crewai_toolkits_gem_2point0_flash.generate_report_from_csv import gen_report
 
def generate_report_button():
    st.page_link("pages/3_Generate_Report.py", label="📝 Generate Report") 

st.header("📝 Generate AI Report")
if st.button("Generate Report"):
    md_path = gen_report()
    st.success("Report generated!")
    st.write(f"Markdown report saved at: `{md_path}`")
    with open(md_path, "r") as f:
        st.markdown(f.read())

import streamlit as st
from download_to_device import download_file, download_all_files_flat_to_downloads

def download_files_button():
    st.page_link("pages/p5_Download_Files.py", label="⬇️ Download Files")

st.header("⬇️ Download Files")
file_type = st.selectbox("Select file to download", ["CSV", "TXT", "PDF", "MD", "All"])
if st.button("Download"):
    if file_type == "All":
        download_all_files_flat_to_downloads()
        st.success("All files downloaded to your Downloads folder.")
    else:
        ext = file_type.lower()
        download_file(f"your_file_name.{ext}")
        st.success(f"{file_type} file downloaded!")

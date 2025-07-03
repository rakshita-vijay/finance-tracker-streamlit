import streamlit as st
from download_to_device import download_file, download_all_files_flat_to_downloads

def download_files_button():
    st.page_link("pages/p5_Download_Files.py", label="⬇️ Download Files") 

def download_files_page():
    st.header("⬇️ Download Files")
    options = ["CSV", "TXT", "PDF", "MD", "All"]
    choice = st.selectbox("Select file type to download", options)

    if st.button("Download"):
        if choice == "All":
            download_all_files_flat_to_downloads()
            st.success("All files downloaded to your Downloads folder.")
        else:
            ext = choice.lower()
            # You may want to implement logic to pick latest file of that type
            filename = f"latest_file.{ext}"  # Replace with actual logic
            download_file(filename)
            st.success(f"{choice} file downloaded.")

download_files_page()

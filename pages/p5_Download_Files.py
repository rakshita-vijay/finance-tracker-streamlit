import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']  

from pages.p0_Authentication import create_empty_files 
create_empty_files(username)

from download_to_device import download_file, download_all_files_flat_to_downloads, cleanup_pycache_and_temp_files

from file_methods.csv_file_methods import find_csv_file_location
from file_methods.txt_file_methods import find_txt_file_location
from file_methods.md_file_methods import find_md_file_location
from file_methods.pdf_file_methods import find_pdf_file_location

st.set_page_config(
  page_title="Download Files",
  page_icon="⬇️",
  layout="wide",
  initial_sidebar_state="expanded"
)

from the_sidebar import the_sb
the_sb() 

def download_files_button():
  st.page_link("pages/p5_Download_Files.py", label="⬇️ Download Files")

def download_files_page():
  st.header("⬇️ Download Files")
  st.divider()
  options = ["CSV (Transactions)", "TXT (ASCII Table)", "PDF (Report)",  "MD (Markdown Report)", "All Files (ZIP)"]

  file_map = {
    "CSV (Transactions)": find_csv_file_location(),
    "TXT (ASCII Table)": find_txt_file_location(),
    "PDF (Report)": find_pdf_file_location(),
    "MD (Markdown Report)": find_md_file_location()
  }

  choice = st.selectbox("Select file to download", options)

  if choice == "All Files (ZIP)":
    clicked = download_all_files_flat_to_downloads()
    if clicked:
      st.success("All files downloaded to your Downloads folder.")
  else:
    file_to_download = file_map.get(choice)
    if file_to_download:
      clicked = download_file(file_to_download)
      if clicked:
        st.success(f"{choice} file downloaded.")

  cleanup_pycache_and_temp_files()

download_files_page()

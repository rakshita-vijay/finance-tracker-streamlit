import os
from fpdf import FPDF

from file_methods.user_file_utils import get_user_file
   
import streamlit as st

if 'username' not in st.session_state:
    st.warning("Please login first.")
    st.stop()
username = st.session_state['username']
   
def find_pdf_file_location(): 
  pdf_path = get_user_file(username, "pdf_transactions", "pdf")
  return pdf_path 

def txt_to_pdf(txt_file, pdf_file):
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Courier", size=8)

  with open(txt_file, "r", encoding="utf-8") as f:
    for line in f:
      pdf.cell(0, 10, txt=line.strip(), ln=True)

  pdf.output(pdf_file)
  # print(f"PDF saved to {pdf_file}")

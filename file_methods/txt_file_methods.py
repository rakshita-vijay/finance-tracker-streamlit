import streamlit as st
if 'username' not in st.session_state:
    st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']

import os, csv
from prettytable import PrettyTable
from file_methods.csv_file_methods import find_csv_file_location
from file_methods.pdf_file_methods import txt_to_pdf

from file_methods.user_file_utils import get_user_file 
   
def find_txt_file_location(): 
  txt_path = get_user_file(username, "txt_version_of_csv_transactions", "txt")
  return txt_path 

def create_and_format_pretty_table():
  curr_csv = find_csv_file_location()
  table = PrettyTable()

  # Read CSV
  with open(curr_csv, "r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    table.field_names = headers
    for row in reader:
      table.add_row(row)

  alignments = {
    "S.NO": "c",
    "DATE": "c",
    "DESCRIPTION": "l",
    "AMOUNT": "r",
    "PAYMENT METHOD": "c",
    "STATUS": "c",
    "NOTES": "l"
  }

  # Set custom alignment per column
  for fn in table.field_names:
    table.align[fn] = alignments[fn]

  return table

def update_txt_file(table = create_and_format_pretty_table()):
  table_str = table.get_string()

  curr_fp = find_txt_file_location()

  with open(curr_fp, "w", encoding='utf-8') as f:
    f.write(table_str)

  curr_csv_fp = find_csv_file_location()
  rn_tsmp = (curr_csv_fp.split("/csv_")[-1]).strip(".csv")

  new_name = f"txt_version_of_csv_{rn_tsmp}.txt"

  curr_fp = find_txt_file_location()
  dir_path = os.path.join(curr_fp.split('saved_files/')[0], 'saved_files/')
  new_fp = os.path.join(dir_path, new_name)

  os.rename(curr_fp, new_fp)

  new_pdf_name = f"pdf_{rn_tsmp}.pdf"
  new_pdf_fp = os.path.join(dir_path, new_pdf_name)

  txt_to_pdf(new_fp, new_pdf_fp)

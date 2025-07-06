import streamlit as st
if 'username' not in st.session_state:
  st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']

import os, csv
from prettytable import PrettyTable
from file_methods.csv_file_methods import find_csv_file_location
from file_methods.pdf_file_methods import txt_to_pdf, find_pdf_file_location

from file_methods.user_file_utils import get_user_file

def find_txt_file_location():
  txt_path = get_user_file(username, "ascii_table_of_transactions", "txt")
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

  curr_txt_fp = find_txt_file_location()

  with open(curr_txt_fp, "w", encoding='utf-8') as f:
    f.write(table_str) 

  curr_txt_fp = find_txt_file_location()
  curr_pdf_fp = find_pdf_file_location() 

  txt_to_pdf(curr_txt_fp, curr_pdf_fp)

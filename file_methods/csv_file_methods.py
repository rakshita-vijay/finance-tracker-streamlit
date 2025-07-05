import streamlit as st
if 'username' not in st.session_state:
    st.switch_page("pages/p0_Authentication.py")
username = st.session_state['username']

import os, csv, sys, datetime, time
from crewai_toolkits_gem_2point0_flash.transform_csv_to_md_table import transformed_table, get_max_width_of_each_column

from file_methods.user_file_utils import get_user_file 

def find_csv_file_location():
  csv_path = get_user_file(username, "csv_transactions", "csv") 
  return csv_path

def extract_csv_content(curr_csv = find_csv_file_location()):
  csv_file = open(curr_csv, mode='r', encoding='utf-8')
  csv_data = csv.reader(csv_file)
  data_lines = list(csv_data)
  csv_file.close()
  return data_lines

def display_csv_content(curr_csv = find_csv_file_location()):
  data_lines = extract_csv_content(curr_csv)

  res = transformed_table(data_lines)
  print(res)

def get_trans_line_details():
  # find_csv_file_location() gives full path
  csv_file_lines = extract_csv_content(find_csv_file_location()) # gives list of lists

  tran_done = len(csv_file_lines) - 1 # because heading also exists
  curr_tran = tran_done + 1 # current transaction

  fields = ['S.NO', 'DATE', 'DESCRIPTION', 'AMOUNT', 'PAYMENT METHOD', 'STATUS', 'NOTES']
  responses = []
  responses.append(curr_tran)

  # DATE
  thro_err = True
  while thro_err:
    try:
      resp = input("Enter the date in MM/DD/YYYY or MM-DD-YYYY format: ")
      stripped_resp = resp.strip().strip("'").strip('"').strip()

      # Extract separator (supports '/', '-', space, or any non-digit)
      demarc = None
      for sep in ['/', '-', ' ', '.']:
        if sep in stripped_resp:
          demarc = sep
          break
      if not demarc:
        # Use any non-digit as separator if no common separator found
        demarc = re.search(r'\D', stripped_resp).group(1) if re.search(r'\D', stripped_resp) else None

      if not demarc:
        raise Exception

      # Split and normalize components
      parts = stripped_resp.split(demarc)

      if len(parts) != 3:
        raise Exception

      # Pad single-digit months/days and normalize year
      month = parts[0].zfill(2)
      day = parts[1].zfill(2)
      year = parts[2].zfill(2)

      # Convert 2-digit year to 4-digit (00-68 → 2000-2068, 69-99 → 1969-1999)
      if len(year) == 2:
        year = f"20{year}" if int(year) <= 68 else f"19{year}"

      # Rebuild normalized date string
      normalized_date = f"{month}/{day}/{year}"
      fin_date = datetime.datetime.strptime(normalized_date, r"%m/%d/%Y")
      date_to_add = f"{fin_date.month:02d}/{fin_date.day:02d}/{fin_date.year}"
      thro_err = False

    except Exception as ex:
      print("\nInvalid date / date format. Retry.")
      thro_err = True

  responses.append(date_to_add)
  print()

  # DESCRIPTION
  thro_err = True
  while thro_err == True:
    try:
      resp = input("Enter the description as text (<60 characters): ")
      stripped_resp = resp.strip().strip("'").strip('"').strip()

      if len(stripped_resp) > 60:
        raise Exception
      else:
        thro_err = False

    except Exception as ex:
      # thro_err = True
      print("\nMessage is too long. Retry.")

  responses.append(stripped_resp)
  print()

  # AMOUNT
  thro_err = True
  while thro_err == True:
    try:
      resp = float(input("Enter the amount as a float number (xx or xx.yyy or xx. or .yyy ): "))
      thro_err = False

    except Exception as ex:
      # thro_err = True
      print("\nInvalid amount format. Retry.")

  responses.append(resp)
  print()

  # PAYMENT METHOD
  thro_err = True
  while thro_err:
    try:
      resp = input("Enter payment method (Cash/Credit/Debit/UPI/etc): ")
      stripped_resp = resp.strip()

      if len(stripped_resp) > 20:
        raise Exception
      else:
        thro_err = False

    except Exception as ex:
      # thro_err = True
      print("\nMessage is too long. Retry.")

  responses.append(stripped_resp)
  print()

  # STATUS
  thro_err = True
  while thro_err:
    try:
      resp = input("Enter status (Completed/Pending/Failed/Cancelled): ")
      stripped_resp = resp.strip()

      valid_statuses = ["Completed", "Pending", "Failed", "Cancelled"]

      if stripped_resp.title() not in valid_statuses:
        raise Exception
      else:
        thro_err = False

    except Exception as ex:
      print("\nInvalid status. Retry.")

  responses.append(stripped_resp.title())
  print()

  # NOTES
  thro_err = True
  while thro_err == True:
    try:
      resp = input("Enter notes (if there are any) as text (<60 characters): ")
      stripped_resp = resp.strip().strip("'").strip('"').strip()

      if len(stripped_resp) > 60:
        raise Exception
      else:
        thro_err = False

    except Exception as ex:
      # thro_err = True
      print("\nMessage is too long. Retry.")

  responses.append(stripped_resp)

  return responses

def add_to_csv(list_of_lists):
  num_of_next_data_line = len(extract_csv_content())

  rows = list_of_lists

  curr_csv = find_csv_file_location()
  csv_file = open(curr_csv, mode='a', encoding='utf-8')
  csv_wrtr = csv.writer(csv_file)

  for row in rows:
    row[0] = str(num_of_next_data_line).zfill(2)

    csv_wrtr.writerow(row)

    num_of_next_data_line += 1

  csv_file.flush()
  os.fsync(csv_file.fileno())
  csv_file.close()

def get_max_width_of_each_column_in_csv(csv_dayta = extract_csv_content()):
  max_width_of_each_column_in_csv = get_max_width_of_each_column(csv_dayta)
  return max_width_of_each_column_in_csv

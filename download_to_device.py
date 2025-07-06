import os, re, datetime, zipfile, shutil, csv
import streamlit as st

from file_methods.csv_file_methods import find_csv_file_location, extract_csv_content

def delete_pychache():
  pass

def delete_zip_files():
  curr_dir = os.getcwd()
  for folders, _, files in os.walk(curr_dir):
    for file in files:
      if re.search(r'^zippy_', file):
        try:
          os.remove(os.path.join(folders, file))
        except Exception as e:
          st.warning(f"Error deleting {file}: {e}")

def cleanup_pycache_and_temp_files():
  delete_pychache()
  delete_zip_files()

def download_all_files_flat_to_downloads():
  zipper_file_name = "zippy_repo_backup.zip"
  curr_dir = os.getcwd()

  with zipfile.ZipFile(zipper_file_name, 'w') as zippy:
    for folders, sub_f, files in os.walk(curr_dir):
      sub_f[:] = [d for d in sub_f if d not in ("__pycache__", ".git")]
      for file in files:
        if file.lower() in ["readme.md", "readme.txt", "readme.rst"] or re.match(r'^zippy_', file):
          continue
        full_path = os.path.join(folders, file)
        zippy.write(full_path, arcname=os.path.basename(full_path), compress_type=zipfile.ZIP_DEFLATED)

  # Offer the zip for download in the browser
  with open(zipper_file_name, "rb") as f:
    clicked = st.download_button(
      label="Download All Files as ZIP",
      data=f,
      file_name=zipper_file_name,
      mime="application/zip"
    )
  os.remove(zipper_file_name)
  return clicked

def download_file(file_to_download=None):
  if file_to_download is None:
    st.info("No file specified, defaulting to CSV.")
    file_to_download = find_csv_file_location()

  only_file_name = os.path.basename(file_to_download)
  extension = os.path.splitext(only_file_name)[1].lower()

  # Check if file exists
  if not os.path.isfile(file_to_download):
    st.error(f"File does not exist: {only_file_name}")
    return False

  # CSV: extract content and offer as download
  if extension == '.csv':
    data_lines = extract_csv_content(file_to_download)
    csv_content = "".join(",".join(map(str, row)) + "\n" for row in data_lines)
    clicked = st.download_button(
      label=f"Download CSV",
      data=csv_content,
      file_name=only_file_name,
      mime='text/csv'
    )
    return clicked

  # TXT, PY, PDF, MD: direct download
  elif extension in ['.txt', '.py', '.pdf', '.md']:
    with open(file_to_download, "rb") as f:
      mime_type = 'application/pdf' if extension == '.pdf' else 'text/plain'
      clicked = st.download_button(
        label=f"Download {extension[1:].upper()}",
        data=f,
        file_name=only_file_name,
        mime=mime_type
      )
    return clicked

  # Other files: zip and offer download
  else:
    zipper_file_name = f"zippy_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(zipper_file_name, 'w') as zippy:
      zippy.write(file_to_download, arcname=only_file_name, compress_type=zipfile.ZIP_DEFLATED)
    with open(zipper_file_name, 'rb') as f:
      clicked = st.download_button(
        label=f"Download ZIP",
        data=f,
        file_name=zipper_file_name,
        mime='application/zip'
      )
    os.remove(zipper_file_name)
    return clicked

import os

def find_md_file_location():
  curr_md = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[len(file)-3 : len(file)] == '.md':
        curr_md = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break

  return curr_md

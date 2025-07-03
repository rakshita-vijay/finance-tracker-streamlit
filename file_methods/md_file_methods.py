import os, glob

def find_md_file_location():
  curr_md = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[len(file)-3 : len(file)] == '.md':
        curr_md = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break

  return curr_md  

def save_and_cleanup_md_report(md_content, md_filename="md_report.md", saved_files_dir="saved_files"):
  for f in os.walk(saved_files_dir):
    if f[0:9] == "md_report":
      os.remove(f) 
    
  md_path = os.path.join(saved_files_dir, md_filename)
  with open(md_path, "w") as f:
    f.write(md_content) 
  return md_path

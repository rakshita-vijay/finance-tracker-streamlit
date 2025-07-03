import os, glob

def find_md_file_location():
  curr_md = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[len(file)-3 : len(file)] == '.md':
        curr_md = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break

  return curr_md  

def save_and_cleanup_md_report(md_content, timestamp, md_filename="md_report.md", saved_files_dir="saved_files"):
  md_path = os.path.join(saved_files_dir, md_filename)
  with open(md_path, "w") as f:
    f.write(f"### Report Generated On: {str(timestamp)}") 
    f.write(" \n\n--- \n")
    f.write(md_content) 
  return md_path

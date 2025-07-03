import os, glob

def find_md_file_location():
  curr_md = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[len(file)-3 : len(file)] == '.md':
        curr_md = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break

  return curr_md 

def delete_old_md_reports(saved_files_dir="saved_files"):
    # Find all .md files in the directory
    md_files = glob.glob(os.path.join(saved_files_dir, "*.md"))
    if not md_files:
        return
    # Sort files by modification time, newest last
    md_files.sort(key=os.path.getmtime, reverse=True)
    # Keep the newest file, delete the rest
    for old_file in md_files[1:]:
        try:
            os.remove(old_file)
        except Exception as e:
            print(f"Could not delete {old_file}: {e}") 

import os, sys, re, datetime, csv, zipfile, shutil
from file_methods.csv_file_methods import find_csv_file_location
from file_methods.csv_file_methods import extract_csv_content

def delete_pychache():
  for root, dirs, files in os.walk(os.getcwd()):
    for dir_name in dirs:
      if dir_name == "__pycache__":
        pycache_path = os.path.join(root, dir_name)
        try:
          shutil.rmtree(pycache_path)
        except Exception as e:
          print(f"Error deleting {pycache_path}: {e}")

def delete_zip_files():
  curr_dir = os.getcwd()
  for folders, _, files in os.walk(curr_dir):
    for file in files:
      if re.search(r'^zippy_', file):
        os.remove(os.path.join(folders, file))
  # print("Zip files deleted from repo.")

def find_downloads_folder():
  downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
  if os.path.isdir(downloads_path):
    pass
  else:
    # make our own path
    os.makedirs(os.path.join(os.path.expanduser("~"), "Downloads"), exist_ok=True)
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

  return downloads_path

def download_all_files_flat_to_downloads():
  zipper_file_name = "zippy_repo_backup.zip"
  curr_dir = os.getcwd()
  with zipfile.ZipFile(zipper_file_name, 'w') as zippy:
    for folders, sub_f, files in os.walk(curr_dir):
      # Skip __pycache__ directories
      sub_f[:] = [d for d in sub_f if d not in ("__pycache__", ".git")]
      for file in files:
        # Skip README files and zip files starting with zippy_
        if file.lower() in ["readme.md", "readme.txt", "readme.rst"] or re.match(r'^zippy_', file):
          continue
        full_path = os.path.join(folders, file)
        # Write file to zip with arcname as basename (flat structure)
        zippy.write(full_path, arcname=os.path.basename(full_path), compress_type=zipfile.ZIP_DEFLATED)

  # Step 2: Extract the zip file to the Downloads folder
  downloads_path = find_downloads_folder()
  with zipfile.ZipFile(zipper_file_name, 'r') as unzippy:
    unzippy.extractall(path=downloads_path)

  print(f"\nDownload of file: {zipper_file_name} complete! Check your downloads folder :)")

  # Step 3: Delete the zip file from the repo
  delete_zip_files()

def download_file(file_to_download = None):
  # print("file_to_download: ", file_to_download)

  if file_to_download == None:
    print("Nothing has been passed into the file_to_download variable. \nThus, downloading csv file :)")
    file_to_download = find_csv_file_location()
    only_file_name = (((file_to_download.strip('C:')).split('/')[-1]).split('\\')[-1]).split('\\\\')[-1]
    extension = 'csv'

  else: # something has been passed into the file_to_download variable
    only_file_name = (((file_to_download.strip('C:')).split('/')[-1]).split('\\')[-1]).split('\\\\')[-1]

    exists = False

    curr_dir = os.getcwd()
    for folders, _, files in os.walk(curr_dir):
      for file in files:
        if file == only_file_name:
          exists = True
          # print("FILE FOUND!")
          break
      if exists == True:
        break

    if exists == False:
      print("\nCannot download file as it doesn't exist :(")
      print("Thus, downloading csv file :)")
      only_file_name = find_csv_file_location()
      extension = 'csv'

    try:
      extension = re.search(r'\.([^.]+)$', only_file_name).group(1)
    except:
      print("Cannot download file as it is not a csv, py, or txt :(")
      print("Thus, downloading csv file :)")
      only_file_name = find_csv_file_location()
      extension = 'csv'

  downloads_path = find_downloads_folder()

  print(f"\nDownloading .{extension} file now...")

  todai = datetime.datetime.today()
  rn = f"{todai.day}-{todai.month}-{todai.year}_{todai.hour}-{todai.minute}-{todai.second}"

  # for csv only
  file_name_in_downloads = f"Transactions_To_Date_{rn}.{extension}"
  path_to_file_in_downloads = os.path.join(downloads_path, file_name_in_downloads)

  if extension == 'csv':
    #extract csv content first
    fp_for_extraction = os.path.join('./saved_files/', only_file_name)

    data_lines = extract_csv_content(fp_for_extraction)

    f = open(path_to_file_in_downloads, mode='w', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerows(data_lines)
    f.close()

    print(f"\nDownload of file: {file_name_in_downloads} complete! Check your downloads folder :)")

  else: # if extension == 'py' or 'txt'
    zipper_file_name = f"zippy_{rn}.zip"

    # finding full path
    ful_pat = only_file_name
    for folders, _, files in os.walk(os.getcwd()):
      for file in files:
        if file == only_file_name:
          ful_pat = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
          break
      if ful_pat != only_file_name:
        break

    zippy = zipfile.ZipFile(zipper_file_name, 'w')
    zippy.write(ful_pat, arcname=os.path.basename(ful_pat), compress_type = zipfile.ZIP_DEFLATED)
    zippy.close()

    unzippy = zipfile.ZipFile(zipper_file_name, 'r')
    unzippy.extractall(path = downloads_path)
    unzippy.close()

    print(f"\nDownload of file: {only_file_name} complete! Check your downloads folder :)")

  # deletion of zip files
  delete_zip_files()

if __name__ == "__main__":
  if len(sys.argv) > 1:
    if sys.argv[1].lower() == "all":
      download_all_files_flat_to_downloads()
    else:
      download_file(sys.argv[1])
  else:
    download_file()
  delete_pychache()

  # line_demarcator = "\n{}\n".format("~" * 120)
  # download_file()
  # print(line_demarcator)
  # download_file("tbh")
  # print(line_demarcator)
  # download_file("tbh.py")
  # print(line_demarcator)
  # download_file("tbh.csv")
  # print(line_demarcator)
  # download_file("csv_26_06_2025_3_48_10.csv")
  # print(line_demarcator)
  # print(line_demarcator)
  # download_file("/Users/rakshita/dev/rakshita/finance-tracker/file_methods/csv_file_methods.py")
  # print(line_demarcator)
  # download_file("main_interface.py")
  # print(line_demarcator)
  # download_file(r"C:\\Users\\Public\\Documents")
  # print(line_demarcator)

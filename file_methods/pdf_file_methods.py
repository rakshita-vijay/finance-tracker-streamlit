import os
from fpdf import FPDF

def find_pdf_file_location():
  curr_pdf = ""

  for folders, _, files in os.walk("./saved_files"):
    for file in files:
      if file[len(file)-4 : len(file)] == '.pdf':
        curr_pdf = ''.join(os.path.join(os.getcwd(), os.path.join(folders, file)).split('./'))
        break

  return curr_pdf

def txt_to_pdf(txt_file, pdf_file):
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Courier", size=8)

  with open(txt_file, "r", encoding="utf-8") as f:
    for line in f:
      pdf.cell(0, 10, txt=line.strip(), ln=True)

  pdf.output(pdf_file)
  # print(f"PDF saved to {pdf_file}")

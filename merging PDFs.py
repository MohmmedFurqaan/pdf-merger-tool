import os
import sys
from pypdf import PdfWriter

def combine_pdfs(pdf_list):
    merger = PdfWriter()

    for pdf_file in pdf_list:
        if os.path.exists(pdf_file) and pdf_file.lower().endswith('.pdf'):
            try:
                merger.append(pdf_file)
            except Exception as e:
                print(f"Error appending {pdf_file}: {e}")
        else:
            print(f"File not found or not a PDF: {pdf_file}")

    if len(merger.pages) > 0:
        output_file = 'Merged.pdf'
        merger.write(output_file)
        merger.close()
        print(f"PDFs merged successfully into {output_file}")
    else:
        print("No valid PDFs to merge.")

if __name__ == "__main__":
    inputs = sys.argv[1:]
    if inputs:
        combine_pdfs(inputs)
    else:
        print("No PDF files provided. Usage: python script.py file1.pdf file2.pdf ...")

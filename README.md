# 📄 PDF Merger using Python

Stop using online tools! Merge multiple PDFs quickly and securely using Python with `pypdf`. 🚀

## 📌 Features
- ✅ Merge multiple PDFs into a single file
- ✅ No internet required – runs locally
- ✅ Simple and lightweight
- ✅ Error handling for invalid or missing PDFs

---

## 🛠️ Installation
Ensure you have Python installed (>=3.x), then install `pypdf`:

```sh
pip install pypdf
```

---

## 🚀 Usage
Run the script with the PDF files you want to merge:

```sh
python pdf_merger.py file1.pdf file2.pdf file3.pdf
```

This will merge the PDFs into a single file named `Merged.pdf`.

---

## 📜 Code
```python
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
```

---

## 🎯 Why Use This?
- No need for third-party online tools that might store your files
- Works **offline** for full privacy
- Super **lightweight** and **fast**

📌 **Save this & try it yourself!**

---

## 📢 Connect
Follow for more Python automation scripts! 🚀

#Python #PDFMerge #CodeTips #PythonAutomation #LearnToCode


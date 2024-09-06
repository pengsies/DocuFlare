import os
import zipfile
import comtypes.client
from tkinter import Tk, Label, Button, filedialog, Text, END


def extract_zip(zip_file, extract_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Files extracted to {extract_dir}")
    return extract_dir

def convert_docx_to_pdf(docx_path, pdf_path, status_text):
    docx_path = os.path.abspath(docx_path)
    pdf_path = os.path.abspath(pdf_path)
    
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False 
    doc = word.Documents.Open(docx_path)
    
    try:
        doc.SaveAs(pdf_path, FileFormat=17) 
        status_text.insert(END, f"Successfully converted {docx_path} to {pdf_path}\n")
    except Exception as e:
        status_text.insert(END, f"Failed to convert {docx_path} to PDF: {e}\n")
    finally:
        doc.Close()
        word.Quit()

def convert_single_docx(docx_file, status_text):
    output_pdf_dir = os.path.abspath('pdf_files') 
    if not os.path.exists(output_pdf_dir):
        os.makedirs(output_pdf_dir)

    pdf_file = os.path.join(output_pdf_dir, f"{os.path.splitext(os.path.basename(docx_file))[0]}.pdf")
    status_text.insert(END, f"Converting {docx_file} to {pdf_file}\n")
    convert_docx_to_pdf(docx_file, pdf_file, status_text)

def convert_all_docx_to_pdf(input_dir, output_dir, status_text):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.docx'):
                docx_file = os.path.join(root, file)
                pdf_file = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.pdf")
                status_text.insert(END, f"Converting {docx_file} to {pdf_file}\n")
                convert_docx_to_pdf(docx_file, pdf_file, status_text)

def select_file_and_convert(status_text):
    file_path = filedialog.askopenfilename(title="Select ZIP or DOCX file", filetypes=[("ZIP and DOCX files", "*.zip *.docx")])

    if not file_path:
        status_text.insert(END, "No file selected. Exiting.\n")
        return

    if file_path.endswith('.zip'):
        extract_to_dir = 'extracted_files'
        output_pdf_dir = 'pdf_files'

        extract_zip(file_path, extract_to_dir)

        convert_all_docx_to_pdf(extract_to_dir, output_pdf_dir, status_text)

    elif file_path.endswith('.docx'):
        convert_single_docx(file_path, status_text)

    else:
        status_text.insert(END, "Unsupported file type. Please select a ZIP or DOCX file.\n")

    status_text.insert(END, "Conversion completed.\n")



def create_gui():
    window = Tk()
    window.title("DOCX to PDF Converter")
    window.geometry("500x300")  # Set the window size
    
    label = Label(window, text="Convert DOCX or ZIP (containing DOCX) to PDF", font=("Arial", 14))
    label.pack(pady=10)
    
    convert_button = Button(window, text="Select File and Convert", command=lambda: select_file_and_convert(status_text))
    convert_button.pack(pady=10)
    
    status_text = Text(window, height=10, width=50)
    status_text.pack(pady=10)
    
    window.mainloop()


if __name__ == '__main__':
    create_gui()

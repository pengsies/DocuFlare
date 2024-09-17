from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document

def convert_docx_to_pdf(docx_path, pdf_output):
    c = canvas.Canvas(pdf_output, pagesize=letter)
    width, height = letter
    margin = 50
    y_position = height - margin

    doc = Document(docx_path)

    for para in doc.paragraphs:
        text = para.text
        text_height = 12

        if y_position < margin + text_height:
            c.showPage()
            y_position = height - margin

        c.drawString(margin, y_position, text)
        y_position -= text_height + 10

    c.save()
    print(f"Successfully converted {docx_path} to {pdf_output}")

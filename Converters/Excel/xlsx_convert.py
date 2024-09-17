import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_xlsx_to_pdf(xlsx_path, pdf_output_path):

    df = pd.read_excel(xlsx_path)

    c = canvas.Canvas(pdf_output_path, pagesize=letter)
    width, height = letter
    margin = 72  # 1 inch margin
    x_offset = margin
    y_offset = height - margin

    for index, row in df.iterrows():
        text = ' | '.join(str(cell) for cell in row)
        c.drawString(x_offset, y_offset, text)
        y_offset -= 15  # Move to the next line; adjust as needed for your data

        if y_offset < margin:
            c.showPage()
            y_offset = height - margin

    c.save()

    print(f"Successfully converted {xlsx_path} to {pdf_output_path}")

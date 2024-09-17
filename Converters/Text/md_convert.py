import markdown2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_md_to_pdf(md_path, pdf_output_path):

    with open(md_path, 'r') as file:
        markdown_text = file.read()

    html_content = markdown2.markdown(markdown_text)

    c = canvas.Canvas(pdf_output_path, pagesize=letter)
    y_offset = 750
    x_offset = 50
    line_height = 15

    for line in html_content.splitlines():
        c.drawString(x_offset, y_offset, line)
        y_offset -= line_height
        if y_offset < 50:
            c.showPage()
            y_offset = 750

    c.save()

    print(f"Successfully converted {md_path} to {pdf_output_path}")

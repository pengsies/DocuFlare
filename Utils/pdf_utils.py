from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def setup_pdf(pdf_output_path):
    """
    Create and return a ReportLab canvas for PDF generation.
    """
    return canvas.Canvas(pdf_output_path, pagesize=letter)

def add_text_to_pdf(c, text, x_offset=50, y_offset=750, line_height=15, max_height=50):
    """
    Add text to the PDF canvas and handle page breaks.
    """
    width, height = letter
    for line in text.splitlines():
        c.drawString(x_offset, y_offset, line)
        y_offset -= line_height
        if y_offset < max_height:
            c.showPage()  # New page if less than max_height units remain
            y_offset = height - 50
    return y_offset

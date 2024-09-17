from reportlab.pdfgen import canvas

def convert_txt_to_pdf(txt_path, pdf_output_path):

    with open(txt_path, 'r') as file:
        text = file.readlines()

    c = canvas.Canvas(pdf_output_path)
    y_offset = 750
    x_offset = 50
    line_height = 15

    for line in text:
        c.drawString(x_offset, y_offset, line.strip())
        y_offset -= line_height
        if y_offset < 50:
            c.showPage()
            y_offset = 750

    c.save()

    print(f"Successfully converted {txt_path} to {pdf_output_path}")

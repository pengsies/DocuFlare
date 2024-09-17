from PIL import Image
from reportlab.lib.pagesizes import letter
from Utils.pdf_utils import setup_pdf

def convert_image_to_pdf(image_path, pdf_output_path):

    img = Image.open(image_path)
    c = setup_pdf(pdf_output_path)

    img_width, img_height = img.size
    max_width, max_height = letter
    scaling_factor = min(max_width / img_width, max_height / img_height)

    img_width = int(img_width * scaling_factor)
    img_height = int(img_height * scaling_factor)

    # Center the image on the PDF page
    x_position = (max_width - img_width) / 2
    y_position = (max_height - img_height) / 2

    c.drawImage(image_path, x_position, y_position, width=img_width, height=img_height)
    c.save()

    print(f"Successfully converted {image_path} to {pdf_output_path}")

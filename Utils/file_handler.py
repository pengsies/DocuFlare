from Converters import (
    convert_xlsx_to_pdf,
    convert_pptx_to_pdf,
    convert_docx_to_pdf,
    convert_md_to_pdf,
    convert_txt_to_pdf,
    convert_image_to_pdf
)

class FileHandler:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert_file(self):
        """
        Converts the input file based on its file extension.
        """
        try:
            if self.input_file.endswith('.xlsx') or self.input_file.endswith('.csv'):
                convert_xlsx_to_pdf(self.input_file, self.output_file)
            elif self.input_file.endswith('.pptx'):
                convert_pptx_to_pdf(self.input_file, self.output_file)
            elif self.input_file.endswith('.docx'):
                convert_docx_to_pdf(self.input_file, self.output_file)
            elif self.input_file.endswith('.md'):
                convert_md_to_pdf(self.input_file, self.output_file)
            elif self.input_file.endswith('.txt'):
                convert_txt_to_pdf(self.input_file, self.output_file)
            elif self.input_file.endswith(('.jpg', '.png')):
                convert_image_to_pdf(self.input_file, self.output_file)
            else:
                raise ValueError("Unsupported file format")
            return True, "Conversion successful!"
        except Exception as e:
            return False, str(e)

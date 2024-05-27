from .base_converter import BaseConverter
from PIL import Image
import os

class ImageToPDFConverter(BaseConverter):
    def convert(self):
        image = Image.open(self.input_path)
        pdf_path = f"{os.path.splitext(self.input_path)[0]}.pdf"
        image.convert('RGB').save(pdf_path)
        return pdf_path

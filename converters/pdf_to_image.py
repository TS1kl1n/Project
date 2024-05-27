from .base_converter import BaseConverter
from pdf2image import convert_from_path
import os

class PDFToImageConverter(BaseConverter):
    def convert(self):
        images = convert_from_path(self.input_path)
        output_paths = []
        for i, image in enumerate(images):
            output_path = f"{os.path.splitext(self.input_path)[0]}_page_{i + 1}.png"
            image.save(output_path, 'PNG')
            output_paths.append(output_path)
        return output_paths[0] if len(output_paths) == 1 else output_paths

from .base_converter import BaseConverter
import fitz
import os

class PDFToImageConverter(BaseConverter):
    def convert(self):
        pdf_document = fitz.open(self.input_path)
        
        output_paths = []
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            
            pix = page.get_pixmap()
            
            output_path = f"{os.path.splitext(self.input_path)[0]}_page_{page_num + 1}.png"
            
            pix.save(output_path)
            
            output_paths.append(output_path)
        
        return output_paths[0] if len(output_paths) == 1 else output_paths

from flask import Flask, request, render_template, send_file
from converters.pdf_to_image import PDFToImageConverter
from converters.image_to_pdf import ImageToPDFConverter
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    file = request.files['file']
    conversion_type = request.form['conversion_type']
    
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        if conversion_type == 'pdf_to_image':
            converter = PDFToImageConverter(filepath)
        elif conversion_type == 'image_to_pdf':
            converter = ImageToPDFConverter(filepath)
        else:
            return "Invalid conversion type", 400
        
        output_path = converter.convert()
        if isinstance(output_path, list):
            output_path = output_path[0]
        return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

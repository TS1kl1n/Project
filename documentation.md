# Documentation

## Overview
This web application allows users to convert files between different formats. Currently supported conversions:
- PDF to Image
- Image to PDF

## Structure
- `app.py`: Main Flask application.
- `converters/`: Directory containing converter classes.
- `templates/`: HTML templates for the Flask app.
- `static/`: Static files (CSS).
- `README.md`: Project overview and instructions.
- `docs/`: Additional documentation.

## Converters
- `BaseConverter`: Abstract base class for converters.
- `PDFToImageConverter`: Converts PDF files to images.
- `ImageToPDFConverter`: Converts images to PDF files.

## Usage
To use the application, run `app.py` and upload a file through the web interface to convert it.

## Development
When contributing, please follow the code style guidelines and ensure that your commit messages clearly describe the changes.

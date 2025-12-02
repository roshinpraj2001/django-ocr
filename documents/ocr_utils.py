import pytesseract
from PIL import Image
from pdf2image import convert_from_path


POPPLER_PATH = r"C:\Users\Lenovo\Desktop\Release-25.11.0-0\poppler-25.11.0\Library\bin"  


def extract_ocr_text(file_path):
    text = ""

    if file_path.lower().endswith(".pdf"):
        pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)

        for page in pages:
            text += pytesseract.image_to_string(page)

    else:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)

    return text

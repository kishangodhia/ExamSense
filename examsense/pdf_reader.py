import fitz
import pytesseract
from PIL import Image
import io
import pytesseract
import os

if os.path.exists("/usr/bin/tesseract"):
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
class PDFReader:
    def read_uploaded_files(self, uploaded_files):
        texts = []
        for file in uploaded_files:
            file_bytes = file.read()
            texts.append(self._read_pdf(file_bytes))
        return "\n".join(texts)

    def _read_pdf(self, file_bytes):
        text = ""
        with fitz.open(stream=file_bytes, filetype="pdf") as doc:
            for page in doc:
                extracted = page.get_text().strip()

                # If text exists, use it
                if extracted:
                    text += extracted + "\n"
                else:
                    # OCR fallback
                    text += self._ocr_page(page)

        return text

    def _ocr_page(self, page):
        try:
            pix = page.get_pixmap()
            img_bytes = pix.tobytes("png")
            image = Image.open(io.BytesIO(img_bytes))

            ocr_text = pytesseract.image_to_string(image)
            return ocr_text + "\n"

        except Exception as e:
            return "[OCR failed]\n"
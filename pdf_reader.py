from PyPDF2 import PdfReader
from pathlib import Path


class PDFReader:
    def extract_text(self, pdf_path):
        reader = PdfReader(pdf_path)
        content = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                content.append(text)

        return "\n".join(content)

    def read_all_pdfs(self, folder_path):
        pdf_texts = {}

        for pdf_file in Path(folder_path).glob("*.pdf"):
            pdf_texts[pdf_file.stem] = self.extract_text(pdf_file)

        return pdf_texts
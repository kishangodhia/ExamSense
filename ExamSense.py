from pdf_reader import PDFReader
from exam_analyzer import ExamAnalyzer
from ai_engine import AIEngine
from pathlib import Path


class ExamSense:
    def __init__(self):
        self.reader = PDFReader()
        self.analyzer = ExamAnalyzer()
        self.ai = AIEngine()

    def analyze_papers(self):
        papers = self.reader.read_all_pdfs("past_papers")

        for name, text in papers.items():
            prompt = self.analyzer.build_prompt(text)
            analysis = self.ai.generate(prompt)

            output_file = Path("output") / f"{name}_analysis.txt"
            output_file.write_text(analysis, encoding="utf-8")

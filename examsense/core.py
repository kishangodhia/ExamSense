from examsense.pdf_reader import PDFReader
from examsense.accomplish_engine import AccomplishEngine
from examsense.ai_engine import AIEngine


class ExamSense:
    def __init__(self):
        self.reader = PDFReader()
        self.accomplish = AccomplishEngine()
        self.engine = AIEngine()

    def run(self, uploaded_files):
        raw_text = self.reader.read_uploaded_files(uploaded_files)

        questions = self.accomplish.extract_questions(raw_text)
        cleaned = self.accomplish.clean_text(questions)
        topics = self.accomplish.detect_topics(cleaned)
        study_plan = self.accomplish.generate_study_plan(topics)

        insights = self.engine.analyze_exam_pattern(cleaned)

        report = f"""
ExamSense Report

Topic Frequency
{topics}

Study Plan
{study_plan}

AI Insights
{insights}
"""
        return report, {"used_local": self.engine.used_local}
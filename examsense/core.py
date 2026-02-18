from examsense.ai_engine import AIEngine

class ExamSense:
    def __init__(self, ai_provider):
        self.engine = AIEngine(ai_provider)

    def run(self, text):
        return self.engine.analyze_exam_pattern(text)

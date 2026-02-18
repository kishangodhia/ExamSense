class ExamAnalyzer:
    def build_prompt(self, exam_text):
        return f"""
You are an exam pattern analyst.

Analyze the following past exam content and identify:
- Repeating topics
- Frequently asked concepts
- High-weightage areas
- Any noticeable patterns

Exam Content:
{exam_text}
"""

import os
import google.generativeai as genai

class AIEngine:
    def __init__(self, provider):
        self.provider = provider
        self._setup()

    def _setup(self):
        if self.provider == "gemini":
            genai.configure(api_key=os.getenv("AIzaSyAbbkwgVLR0DZ4vGe6F0KwQlJC-gZ2RZ04"))
            self.model = genai.GenerativeModel("gemini-pro")

    def analyze_exam_pattern(self, text):
        prompt = f"""
        Analyze the following exam paper text.
        Identify:
        - Repeated topics
        - Question patterns
        - High-weight chapters
        - Common question types

        Text:
        {text}
        """

        response = self.model.generate_content(prompt)
        return response.text

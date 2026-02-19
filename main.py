from examsense.core import ExamSense

if __name__ == "__main__":
    app = ExamSense(ai_provider="gemini")
    result = app.run("sample exam text")
    print(result)

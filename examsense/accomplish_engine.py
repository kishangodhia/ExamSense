import re
from collections import Counter

STOPWORDS = {
    "what","which","when","where","who","why","how",
    "explain","write","answer","question","questions",
    "each","following","define","short","notes","give",
    "the","is","are","was","were","and","or","to","of",
    "in","on","for","with","a","an","by","from","that",
    "this","these","those","should","scan","scanned",
    "book","one","two","three","you","any","marks",
    "part","parts","section","attempt","all"
}

NOISE_PATTERNS = [
    r"camscanner",
    r"page \d+",
    r"\d{4}",
    r"www\.",
]


class AccomplishEngine:
    def extract_questions(self, text: str):
        for pattern in NOISE_PATTERNS:
            text = re.sub(pattern, " ", text, flags=re.IGNORECASE)
        parts = re.split(r"[?.!]\s+", text)
        return [p.strip() for p in parts if len(p.split()) > 5]

    def clean_text(self, questions):
        if isinstance(questions, list):
            text = " ".join(questions)
        else:
            text = str(questions)
        text = re.sub(r"\s+", " ", text)
        return text.lower().strip()

    def detect_topics(self, text: str, top_k=10):
        return self.extract_topics(text, top_k)

    def extract_topics(self, text: str, top_k=10):
        words = re.findall(r"[a-zA-Z]{4,}", text)
        filtered = [w for w in words if w not in STOPWORDS]
        freq = Counter(filtered)
        strong = {k: v for k, v in freq.items() if v >= 2}
        return dict(sorted(strong.items(), key=lambda x: x[1], reverse=True)[:top_k])

    def generate_study_plan(self, topics: dict):
        return self.build_study_plan(topics)

    def build_study_plan(self, topics: dict):
        if not topics:
            return "No strong topics detected."
        lines = ["Smart Study Plan:\n"]
        for topic, count in topics.items():
            lines.append(f"Focus on '{topic}' (appears {count} times)")
        lines.append("\nPrioritize high-frequency concepts first.")
        return "\n".join(lines)
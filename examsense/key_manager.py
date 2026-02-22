import os
from dotenv import load_dotenv

load_dotenv()

class GeminiKeyManager:
    def __init__(self):
        raw = os.getenv("GEMINI_KEYS", "")
        self.keys = [k.strip() for k in raw.split(",") if k.strip()]
        self.exhausted = set()
        self.index = 0

    def get_key(self):
        available = [k for k in self.keys if k not in self.exhausted]
        if not available:
            raise RuntimeError("All API keys exhausted")

        key = available[self.index % len(available)]
        self.index += 1
        return key

    def mark_exhausted(self, key):
        self.exhausted.add(key)
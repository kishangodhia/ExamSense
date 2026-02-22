import os
from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai
except ImportError:
    genai = None


class AIEngine:
    def __init__(self):
        self.used_local = False
        self.clients = self._build_clients()

    def _get_keys(self):
        keys = []
        env_multi = os.getenv("GEMINI_API_KEYS")
        if env_multi:
            keys = [k.strip() for k in env_multi.split(",") if k.strip()]
        if not keys:
            single = os.getenv("GEMINI_API_KEY")
            if single:
                keys = [single]
        try:
            import streamlit as st
            if "GEMINI_API_KEYS" in st.secrets:
                keys = list(st.secrets["GEMINI_API_KEYS"])
        except Exception:
            pass
        return keys

    def _build_clients(self):
        if not genai:
            return []
        clients = []
        for key in self._get_keys():
            try:
                clients.append(genai.Client(api_key=key))
            except Exception:
                continue
        return clients

    def analyze_exam_pattern(self, text: str) -> str:
        return self._run(text)

    def analyze(self, text: str) -> str:
        return self._run(text)

    def _run(self, prompt: str) -> str:
        self.used_local = False
        for client in self.clients:
            try:
                resp = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
                text = getattr(resp, "text", "").strip()
                if text:
                    return text
            except Exception as e:
                print("Gemini error:", e)
                continue
        self.used_local = True
        return self._fallback()

    def _fallback(self):
        return (
            "Fallback mode active.\n\n"
            "Cloud AI unavailable. Basic analysis generated locally.\n\n"
            "Focus on repeated topics, high-weight chapters, and past papers."
        )
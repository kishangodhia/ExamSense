import subprocess


class LocalEngine:
    def analyze(self, text: str) -> str:
        try:
            prompt = f"""
Analyze exam papers and generate:

- Repeated topics
- Important areas
- Study tips

Content:
{text[:6000]}
"""

            result = subprocess.run(
                ["ollama", "run", "mistral"],
                input=prompt,
                capture_output=True,
                text=True,
                timeout=60
            )

            return result.stdout.strip()

        except Exception as e:
            return "Local AI unavailable. Please install Ollama."
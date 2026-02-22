import streamlit as st
from examsense.core import ExamSense
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import io

st.title("ExamSense")
st.caption("Built with hybrid AI: Accomplish + Gemini + Local fallback")

with st.expander("How ExamSense works (Accomplish + AI)"):
    st.markdown("""
    Hybrid Intelligence for Smarter Preparation This app analyzes exam papers using a hybrid pipeline Lightweight NLP for repeated topics Gemini for deeper analysis Local model fallback if API limits are hit

**Accomplish Intelligence**
- Reads raw exam papers directly (even messy or scanned ones)
- Extracts meaningful content from unstructured PDFs
- Cleans noisy formatting and removes irrelevant text
- Detects repeated topics across multiple papers
- Builds a fast topic importance map locally
- Identifies patterns without needing heavy cloud AI

**AI Deep Analysis**
- Uses advanced language models for semantic understanding
- Finds hidden patterns in question trends
- Identifies high-scoring areas and preparation focus zones
- Generates structured exam insights automatically

**Designed for Real Students**
- Works with scanned papers and messy PDFs
- No manual tagging or formatting needed
- Handles multiple subjects and formats

**Reliable by Design**
- Uses cloud AI for deep insights
- Falls back to local intelligence if needed
- Ensures uninterrupted analysis

ExamSense turns past papers into actionable preparation insights using hybrid intelligence.
""")

files = st.file_uploader(
    "Upload exam PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if files:
    if st.button("Run Analysis"):
        with st.spinner("Reading papers..."):
            app = ExamSense()
            report, meta = app.run(files)

        if meta.get("used_local"):
            st.warning("Gemini unavailable. Used local model instead.")
        else:
            st.success("Analysis complete")

        st.markdown(report)

        def build_pdf(text):
            buf = io.BytesIO()
            doc = SimpleDocTemplate(buf, pagesize=A4)
            styles = getSampleStyleSheet()
            story = []

            for line in text.split("\n"):
                story.append(Paragraph(line, styles["Normal"]))
                story.append(Spacer(1, 0.15 * inch))

            doc.build(story)
            buf.seek(0)
            return buf

        pdf = build_pdf(report)

        st.download_button(
            "Download Report",
            pdf,
            f"ExamSense_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        )
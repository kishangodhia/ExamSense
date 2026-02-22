---

# 📚 ExamSense

ExamSense is a smart exam paper analyzer that helps students identify **important topics, trends, and high-scoring areas** from past exam papers.

Built for hackathons and real student use, it combines lightweight NLP with AI models to generate structured exam insights automatically.

---

## ✨ What it does

Upload past exam papers → get:

* Most repeated topics
* Important chapters
* Question trends
* High scoring areas
* Smart preparation tips
* Downloadable analysis report (PDF)

No manual analysis needed.

---

## 🧠 How ExamSense Works

ExamSense uses a **hybrid AI pipeline** designed to be fast, affordable, and reliable.

### 1️⃣ Accomplish-style Local Analysis (Primary Layer)

This runs locally and is always available.

It:

* Extracts text from PDFs (including scanned papers with OCR)
* Cleans and normalizes content
* Detects repeated keywords and topics
* Ranks concepts by frequency
* Builds a basic study plan

This ensures the app **works even without internet or API limits**.

---

### 2️⃣ Gemini AI (Deep Analysis Layer)

Once the local analysis is done, the cleaned data is sent to Gemini for deeper insights.

Gemini provides:

* Conceptual trend detection
* High scoring strategy insights
* Pattern-based preparation advice
* Structured exam breakdown

This layer adds **intelligence and depth** to the report.

---

### 3️⃣ Automatic Fallback (Reliability Layer)

If Gemini:

* Hits quota limits
* Is unavailable
* API key fails

ExamSense automatically falls back to:

👉 Local analysis only

This ensures the app **never breaks during demos or judging**.

---

## 🧰 Tech Stack

* Python
* Streamlit (UI)
* OCR (Tesseract + PyMuPDF)
* ReportLab (PDF reports)
* Gemini API (optional AI layer)

---

## 🚀 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ExamSense.git
cd ExamSense
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

pip install -r requirements.txt
```

---

### 4. Add your Gemini API key (optional but recommended)

Create a `.env` file in the **project root**:

```
GEMINI_API_KEY=your_key_here
```

If no key is provided, the app will still work using local analysis.

---

### 5. Run the app

```bash
streamlit run app.py
```

Open the local URL shown in terminal (usually):

```
http://localhost:8501
```

---

## 📤 Using the App

1. Upload one or more exam PDFs
2. Click **Analyze Papers**
3. View insights instantly
4. Download the report as PDF

---

## 🎯 Why This Project

Students often waste hours trying to understand:

* What topics repeat
* What chapters matter
* Where to focus

ExamSense turns **years of papers into instant strategy**.

It’s built to:

* Save study time
* Improve scoring efficiency
* Help students study smarter, not harder

---

## 🛡 Reliability Design

* Works offline (local analysis)
* Handles API limits gracefully
* No data stored permanently
* Uploaded PDFs processed in-memory

---

import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline
import io
# Page setup
st.set_page_config(page_title="LegalGPT", page_icon="📄", layout="centered")

# Custom styles
st.markdown("""
    <style>
    .main {
        background-color: #f4f4f4;
        padding: 20px;
        border-radius: 10px;
    }
    .block-container {
        padding-top: 2rem;
    }
    .stButton>button {
        background-color: #007acc;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stTextInput>div>div>input {
        background-color: #fff0f5;
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Instructions
st.title("📄 LegalGPT – AI Legal Document Assistant")
st.subheader("🧠 Understand Legal PDFs in Plain English")
st.markdown("""
Upload your legal contract, agreement, or document.  
LegalGPT will summarize it and highlight risky clauses like **termination**, **auto-renew**, and **penalties**.
""")

# Summarizer - Fast Hugging Face version
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="t5-small")

summarizer = load_summarizer()

# Extract text from PDF

def extract_text(pdf_file):
    try:
        # Rewind the uploaded file and create BytesIO stream
        pdf_file.seek(0)
        byte_stream = io.BytesIO(pdf_file.read())
        doc = fitz.open(stream=byte_stream, filetype="pdf")
        return "\n".join(page.get_text() for page in doc)

    except Exception as e:
        st.error("❌ Failed to open the PDF file. It may be corrupted or not a valid PDF.")
        st.error(f"Error: {e}")
        return ""


# Summarize text (fast and clean)
def summarize(text):
    chunks = [text[i:i+800] for i in range(0, len(text), 800)]
    summary = ""
    for chunk in chunks[:2]:
        out = summarizer(chunk, max_length=120, min_length=30, do_sample=False)
        summary += out[0]['summary_text'] + "\n"
    return summary

# Detect risky terms
def detect_risks(text):
    keywords = ["termination", "penalty", "arbitration", "auto-renew", "non-compete"]
    return [k for k in keywords if k.lower() in text.lower()]

# File upload
uploaded_file = st.file_uploader("📎 Upload PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("🔍 Reading PDF..."):
        text = extract_text(uploaded_file)
        st.success("✅ Text Extracted")

    st.subheader("📜 Preview of Extracted Text")
    st.text(text[:800] + "...")

    if st.button("🧠 Analyze Document"):
        with st.spinner("🤖 Summarizing..."):
            summary = summarize(text)
            risks = detect_risks(text)

        st.subheader("📝 Summary")
        st.success(summary)

        st.subheader("⚠️ Risky Terms Found")
        if risks:
            for r in risks:
                st.markdown(f"⚠️ **Risky Term Detected:** `{r}`", unsafe_allow_html=True)
        else:
            st.info("✅ No risky terms found.")

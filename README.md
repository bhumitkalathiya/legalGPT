📘 LegalGPT – AI-Powered Legal Document Assistant
LegalGPT is a lightweight, intelligent assistant that helps users understand legal documents by summarizing them and detecting risky clauses — all in plain English. Built with Streamlit and Hugging Face's t5-small model, it offers a fast, easy-to-use legal document analysis tool directly in your browser.

🚀 Features
📄 Upload any legal PDF document

🧠 Get an AI-powered summary using a pre-trained t5-small model

⚠️ Automatically detects risky terms like termination, penalty, auto-renew, etc.

⚡ Clean, interactive Streamlit web interface

💻 Works offline – no API key needed

🛠️ Tech Stack
Feature	Technology
Web Interface	Streamlit
AI Summarization	Hugging Face Transformers (t5-small)
PDF Text Extraction	PyMuPDF (fitz)
Language	Python

📦 Installation


# 1. Clone the repository
git clone https://github.com/yourusername/legalgpt.git
cd legalgpt

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run legalgpt.py
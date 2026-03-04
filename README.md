# Rag_bot
An AI-powered Assistant that uses **RAG (Retrieval-Augmented Generation)** to answer questions based on a company Notion Wiki. Built with **LangChain**, **ChromaDB**, and **Ollama**.

## 🚀 Features
- **Local LLM:** Runs entirely on your machine using Ollama (Mistral 7B).
- **Dual Data Sources:** Processes Markdown files (Wiki) and CSV files (Tickets).
- **Feedback Loop:** "Like" a response in the UI to save it as a verified ticket in the CSV.
- **Privacy First:** Your data never leaves your local network.

---

## 🛠️ Prerequisites
Before running, ensure you have the following installed:
1. **Python 3.10+**
2. **Ollama:** [Download here](https://ollama.com/)

---

## 🏃 Getting Started

### 1. Clone the Repo & Setup
```bash
git clone [https://github.com/YOUR_USERNAME/my-rag-project.git](https://github.com/YOUR_USERNAME/my-rag-project.git)
cd my-rag-project

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

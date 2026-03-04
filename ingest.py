import os
from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

WIKI_PATH = "data/wiki_export"
TICKETS_PATH = "data/tickets.csv"
DB_PATH = "./chroma_db"

def ingest_data():
    all_docs = []

    # 1. Load Notion Markdown Files (Robust version)
    if os.path.exists(WIKI_PATH):
        print(f"Loading files from {WIKI_PATH}...")
        for file in os.listdir(WIKI_PATH):
            if file.endswith(".md"):
                try:
                    file_path = os.path.join(WIKI_PATH, file)
                    # TextLoader is much more stable than Unstructured for simple MD
                    loader = TextLoader(file_path, encoding='utf-8')
                    all_docs.extend(loader.load())
                    print(f" Successfully loaded: {file}")
                except Exception as e:
                    print(f" Skipping {file} due to error: {e}")

    # 2. Load Support Tickets (CSV)
    if os.path.exists(TICKETS_PATH):
        print("Loading tickets...")
        csv_loader = CSVLoader(file_path=TICKETS_PATH)
        all_docs.extend(csv_loader.load())

    if not all_docs:
        print("No documents found! Check your folders.")
        return

    # 3. Chunking & Embedding
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(all_docs)

    print(f"Embedding {len(chunks)} chunks into ChromaDB...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model="nomic-embed-text"),
        persist_directory=DB_PATH
    )
    print("DONE! You can now run app.py")

if __name__ == "__main__":
    ingest_data()

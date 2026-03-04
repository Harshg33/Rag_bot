import gradio as gr
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
# Modern 2026 Import Paths
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# --- SETUP RAG COMPONENTS ---
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
llm = ChatOllama(model="mistral", streaming=True) # Enabled streaming

# 1. Define the System Prompt
system_prompt = (
    "You are Wyrd's AI Wiki Assistant. Use the context below to answer questions. "
    "Be concise and professional. If the answer isn't in the context, say so."
    "\n\nContext:\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# 2. Build the Chain
qa_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(vectorstore.as_retriever(), qa_chain)

# --- GRADIO INTERFACE ---
def chat_function(message, history):
    print("--- Searching Database ---")
    response_text = ""
    for chunk in rag_chain.stream({"input": message}):
        if "answer" in chunk:
            response_text += chunk["answer"]
            yield response_text  # This 'yield' sends the text to the UI bit-by-bit
    print("--- Generating Answer ---")

# --- GRADIO INTERFACE ---

# --- GRADIO INTERFACE ---

view = gr.ChatInterface(
    fn=chat_function,
    title="Wyrd Wiki Bot 🌲",
    description="Ask me anything about company policy or previous support tickets.",
    examples=["What is Wyrd Media?"],
    # DELETE the 'type' line entirely
)

if __name__ == "__main__":
    view.launch(theme="soft")

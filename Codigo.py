import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.chat_models import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

# Configuração da chave da API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Função para carregar documentos PDF
def carregar_documentos(pasta="./docs"):
    documentos = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pasta, arquivo))
            documentos.extend(loader.load())
    return documentos

# Função para criar base vetorial
def criar_base(documentos):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=80)
    chunks = splitter.split_documents(documentos)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )
    db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_storage")
    return db

# Interface Streamlit
st.title("🤖 Assistente Inteligente de Documentos")
st.write("Agente de IA com RAG para responder dúvidas com base em documentos internos.")

# Carregar documentos e preparar base
documentos = carregar_documentos()
db = criar_base(documentos)

# Configurar modelo de linguagem
modelo = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
qa = RetrievalQA.from_chain_type(
    llm=modelo,
    retriever=db.as_retriever(),
    return_source_documents=True
)

# Campo de pergunta
pergunta = st.text_input("Digite sua pergunta:")
if pergunta:
    resposta = qa(pergunta)
    st.write("### Resposta")
    st.write(resposta["result"])

    st.write("### Fontes utilizadas:")
    for doc in resposta["source_documents"]:
        st.write(f"- {doc.metadata.get('source', 'Documento interno')}")

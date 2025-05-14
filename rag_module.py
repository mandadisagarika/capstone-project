from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

# Load and split documents
def load_docs(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)
    return docs

# Create FAISS vectorstore with HuggingFace embeddings
def create_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

# Build the full RAG chain (retriever + HuggingFace text generator)
def get_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    
    qa_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        tokenizer="google/flan-t5-base",
        max_length=512
    )
    
    llm = HuggingFacePipeline(pipeline=qa_pipeline)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    
    return qa_chain

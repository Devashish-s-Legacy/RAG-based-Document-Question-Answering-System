from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_retriever():
    # ✅ Define embeddings properly
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    return retriever
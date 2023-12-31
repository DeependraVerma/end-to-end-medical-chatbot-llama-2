from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Extract the data from the pdf book
def load_data(data):
    loader = DirectoryLoader(data,
    glob="*.pdf",
    loader_cls=PyPDFLoader)

    documents = loader.load()
    return documents

#create text Chunks
def text_split(extracted_pdf):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                   chunk_overlap=20)
    text_chunks=text_splitter.split_documents(extracted_pdf)
    return text_chunks 


#download embedding model
def download_huggingfaceembedding():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding

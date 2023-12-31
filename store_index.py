from src.helper import load_data, text_split, download_huggingfaceembedding
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_API_ENV = os.environ.get("PINECONE_API_ENV")

#print(PINECONE_API_KEY)
#print(PINECONE_API_ENV)

extracted_pdf = load_data("Data/")
text_chunks = text_split(extracted_pdf)
embedding = download_huggingfaceembedding()

pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)


index_name="medical-chatbot"
docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embedding, index_name=index_name)


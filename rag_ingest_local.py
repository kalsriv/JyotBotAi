import os
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader


working_dir = os.path.dirname(os.path.abspath(__file__))
doc_folder = os.path.join(working_dir, "doc_to_upload")

for file in os.listdir(doc_folder):
    if file.endswith(".pdf"):
        file_path = os.path.join(doc_folder, file)
        print(f"Processing {file_path}")
        process_document_to_chroma_db(file_path)

print("Vectorstore built successfully.")

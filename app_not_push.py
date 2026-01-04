import os
import streamlit as st
from rag_helper_utility_not_push import process_document_to_chroma_db, answer_question

# Set working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

st.title("SupplyBhai - Local Ingestion Mode 🛠️")
st.subheader("This version builds the Chroma vectorstore locally. Do NOT push this file.")

# -------------------------------
# 1. AUTO-LOAD ALL PDFs FROM FOLDER
# -------------------------------

st.markdown("""
<style>
.small-text {
    font-size: 0.8rem;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="small-text">⏳ Processing PDFs…</p>', unsafe_allow_html=True)

doc_folder = os.path.join(working_dir, "doc_to_upload")

# Ensure folder exists
if not os.path.exists(doc_folder):
    st.error(f"Folder not found: {doc_folder}")
else:
    for file in os.listdir(doc_folder):
        if file.endswith(".pdf"):
            file_path = os.path.join(doc_folder, file)
            st.write(f"Processing: {file}")
            process_document_to_chroma_db(file_path)

st.markdown(
    "<p style='color: green; font-size: 0.8rem;'>✔️ Vectorstore built/updated locally!</p>",
    unsafe_allow_html=True
)

# -------------------------------
# 2. USER QUESTION INPUT
# -------------------------------

user_question = st.text_area("Ask a question about the ingested documents")

if st.button("Answer"):
    answer = answer_question(user_question)

    st.markdown("### SupplyBhai says:")
    st.markdown(answer)

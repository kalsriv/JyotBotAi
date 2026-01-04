import os
import streamlit as st
from rag_helper_utility_push import process_document_to_chroma_db, answer_question

# Set working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #FDF6EC;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #FAEED1;
}

/* Change font globally */
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

/* Style buttons */
.stButton>button {
    background-color: #FF6F00;
    color: white;
    border-radius: 8px;
    padding: 0.6rem 1.2rem;
    font-size: 1rem;
    border: none;
}

.stButton>button:hover {
    background-color: #E65100;
}

/* Style subheaders */
h2, h3 {
    color: #6A1B9A;
}
</style>
""", unsafe_allow_html=True)


st.title("JyotBot - Your Vedic Astrology Assistant 🌞")
st.subheader("Ask questions related to Vedic Astrology based on the knowledgebase.")


# -------------------------------
# 1. AUTO-LOAD ALL PDFs FROM FOLDER
# -------------------------------

# st.subheader("Loading Please wait ...  ")

st.markdown("""
<style>
.small-text {
    font-size: 0.8rem;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="small-text">⏳ Loading…</p>', unsafe_allow_html=True)


st.markdown(
    "<p style='color: green; font-size: 0.8rem;'>✔️ Knowledgebase updated!</p>",
    unsafe_allow_html=True
)

# -------------------------------
# 2. USER QUESTION INPUT
# -------------------------------

user_question = st.text_area("Ask your question about the knowledgebase")

if st.button("Answer"):
    answer = answer_question(user_question)

    st.markdown("JyotBot says")
    st.markdown(answer)

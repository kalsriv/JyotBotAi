import os
import streamlit as st
from rag_helper_utility_push import process_document_to_chroma_db, answer_question

# Set working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #5A8F7B;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #A7E8E1;
}

/* Change font globally */
html, body, [class*="css"] { 
            font-family: 'Cormorant Garamond', serif; 
}

/* Style buttons */
.stButton>button {
    background-color: #FF6F00;
    color: black;
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
# 2. AHOROSCOPE API DISPLAY
# -------------------------------
st.subheader("Birth Details for Horoscope Chart")

col1, col2, col3 = st.columns(3)
with col1:
    year = st.number_input("Year", min_value=1900, max_value=2100, value=1990)
with col2:
    month = st.number_input("Month", min_value=1, max_value=12, value=1)
with col3:
    date = st.number_input("Date", min_value=1, max_value=31, value=1)

col4, col5, col6 = st.columns(3)
with col4:
    hours = st.number_input("Hour", min_value=0, max_value=23, value=12)
with col5:
    minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0)
with col6:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0)

col7, col8 = st.columns(2)
with col7:
    latitude = st.number_input("Latitude", value=17.38333)
with col8:
    longitude = st.number_input("Longitude", value=78.4666)

timezone = st.number_input("Timezone (e.g., 5.5)", value=5.5)


from rag_helper_utility_push import get_horoscope_chart_svg

if st.button("Generate Horoscope Chart"):
    svg_code = get_horoscope_chart_svg(
        year, month, date, hours, minutes, seconds,
        latitude, longitude, timezone
    )

    st.subheader("Your Horoscope Chart (SVG)")

    # Debug output
    # st.write("Raw API Response:")
    # st.code(svg_code[:500])

    # Try rendering
    st.markdown(svg_code, unsafe_allow_html=True)

    # print("STATUS:", response.status_code)
    # print("RAW:", response.text)

# -------------------------------
# 2. USER QUESTION INPUT
# -------------------------------

user_question = st.text_area("Ask your question about the knowledgebase")

if st.button("Answer"):
    answer = answer_question(user_question)

    st.markdown("JyotBot says")
    st.markdown(answer)




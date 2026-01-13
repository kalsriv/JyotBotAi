import os
import streamlit as st
from rag_helper_utility_push import process_document_to_chroma_db, answer_question, get_horoscope_chart_svg, get_horoscope_data_text

# Set working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize session state for the chart and data
if "svg_code" not in st.session_state:
    st.session_state.svg_code = None
if "birth_data" not in st.session_state:
    st.session_state.birth_data = None

# --- STYLING (Keep your existing CSS) ---
st.markdown("""
<style>
.stApp { background-color: #5A8F7B; }
[data-testid="stSidebar"] { background-color: #A7E8E1; }
html, body, [class*="css"] { font-family: 'Cormorant Garamond', serif; }
.stButton>button {
    background-color: #FF6F00; color: black;
    border-radius: 8px; padding: 0.6rem 1.2rem;
    font-size: 1rem; border: none;
}
h2, h3 { color: #6A1B9A; }
</style>
""", unsafe_allow_html=True)

st.title("JyotBot - Your Vedic Astrology Assistant 🌞")
st.subheader("Ask questions related to Vedic Astrology based on the knowledgebase.")

# --- KNOWLEDGEBASE STATUS ---
st.markdown('<p style="font-size: 0.8rem; color: gray;">⏳ Loading...</p>', unsafe_allow_html=True)
st.markdown("<p style='color: green; font-size: 0.8rem;'>✔️ Knowledgebase updated!</p>", unsafe_allow_html=True)

# --- 1. BIRTH DETAILS INPUT ---
st.subheader("Birth Details for Horoscope Chart")

col1, col2, col3 = st.columns(3)
with col1: year = st.number_input("Year", min_value=1900, max_value=2100, value=1990)
with col2: month = st.number_input("Month", min_value=1, max_value=12, value=1)
with col3: date = st.number_input("Date", min_value=1, max_value=31, value=1)

col4, col5, col6 = st.columns(3)
with col4: hours = st.number_input("Hour", min_value=0, max_value=23, value=12)
with col5: minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0)
with col6: seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0)

col7, col8 = st.columns(2)
with col7: latitude = st.number_input("Latitude", value=17.38333)
with col8: longitude = st.number_input("Longitude", value=78.4666)

timezone = st.number_input("Timezone (e.g., 5.5)", value=5.5)

# --- 2. GENERATE CHART LOGIC ---
# We only use the button ONCE here
if st.button("Generate Horoscope Chart"):
    # Save inputs to session state
    st.session_state.birth_data = {
        "year": year, "month": month, "date": date,
        "hours": hours, "minutes": minutes, "seconds": seconds,
        "latitude": latitude, "longitude": longitude, "timezone": timezone
    }
    # Fetch SVG
    with st.spinner("Drawing your chart..."):
        st.session_state.svg_code = get_horoscope_chart_svg(**st.session_state.birth_data)

# Display the chart if it exists in state
if st.session_state.svg_code:
    st.subheader("Your Horoscope Chart")
    st.markdown(st.session_state.svg_code, unsafe_allow_html=True)

st.divider()

# --- 3. QUESTION & ANSWER LOGIC ---
user_question = st.text_area("Ask JyotBot about the knowledgebase or your chart:")

if st.button("Answer"):
    if not user_question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Consulting the scriptures..."):
            # Check if we have chart data to append
            if st.session_state.birth_data:
                # Fetch text positions of planets
                chart_text = get_horoscope_data_text(**st.session_state.birth_data)
                # Combine data with question
                full_query = f"CHART DATA: {chart_text}\n\nUSER QUESTION: {user_question}"
                answer = answer_question(full_query)
            else:
                # Just ask the question without chart data
                answer = answer_question(user_question)
            
            st.markdown("### JyotBot says")
            st.info(answer)
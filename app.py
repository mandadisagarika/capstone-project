import streamlit as st
import fitz  # PyMuPDF for PDF display
from rag_module import get_recommendation

st.set_page_config(page_title="Laptop Accessory Recommender", page_icon="💻")

st.title("💻 Laptop Accessory Recommendation System")

st.subheader("📘 Accessory Manual Browser")
uploaded_pdf = st.file_uploader("Upload an accessory manual (PDF)", type="pdf")

if uploaded_pdf is not None:
    doc = fitz.open(stream=uploaded_pdf.read(), filetype="pdf")
    with open("accessory_manual.txt", "w", encoding="utf-8") as f:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            st.markdown(f"### 📄 Page {page_num + 1}")
            st.text(text)
            f.write(text + "\n")

st.markdown("Ask about an accessory (e.g., Best mouse for coding)")
user_query = st.text_input("Enter your question")
laptop_model = st.text_input("Laptop Model", placeholder="e.g., mac, dell, hp")
interest = st.selectbox("Interest", ["gaming", "design", "typing", "portability", "multimedia", "general"])

if st.button("Get Recommendation"):
    if user_query and laptop_model:
        recommendation = get_recommendation(user_query, laptop_model, interest)
        st.subheader("🔍 Recommendation")
        st.write(recommendation)
    else:
        st.warning("Please enter both a question and a laptop model.")

st.subheader("📊 Feedback")
feedback = st.radio("How was the recommendation?", ["👍 Positive", "👎 Negative"])
st.success(f"Thank you for your feedback: {feedback}")

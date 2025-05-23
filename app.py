import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="Laptop Accessory Recommendation", layout="centered")

# 🌟 Title
st.title("💻 Laptop Accessory Recommendation System")

# 📂 File Upload
manual_file = st.file_uploader("📂 Upload your laptop manual (TXT or PDF)", type=["txt", "pdf"])

# 🧠 Accessory Query
query = st.text_input("🔍 Ask about an accessory (e.g., Best mouse for coding)")

# 💻 Laptop Model
laptop_model = st.text_input("💼 Enter your laptop model")

# 🎯 Interest
interest = st.selectbox("🎯 Choose your interest", ["Work", "Gaming", "Design", "Coding", "Casual"])

# 🚀 Recommendation Button
if st.button("Get Recommendation"):
    if not manual_file or not query or not laptop_model or not interest:
        st.warning("⚠️ Please complete all fields before generating a recommendation.")
    else:
        # 📄 Read file content
        file_content = ""
        if manual_file.type == "text/plain":
            file_content = manual_file.read().decode("utf-8")
        elif manual_file.type == "application/pdf":
            reader = PdfReader(manual_file)
            for page in reader.pages:
                file_content += page.extract_text() or ""

        # 🧠 Simple Recommendation Logic
        if "headphone" in query.lower() or "zoom" in query.lower():
            recommendation = "Sony WH-1000XM5 or Bose QC45"
        elif "mouse" in query.lower() or "coding" in interest.lower():
            recommendation = "Logitech MX Master 3"
        elif "design" in interest.lower():
            recommendation = "XP-Pen Deco Tablet or Apple Magic Mouse"
        else:
            recommendation = "USB Hub, Cooling Pad, Laptop Stand"

        # 📌 Show Recommendation
        st.subheader("📌 Recommendation")
        st.success(recommendation)

        # 📊 Feedback
        st.subheader("📊 Feedback")
        feedback = st.radio("Was this recommendation helpful?", ["👍 Yes", "👎 No"])

        # 🌐 HTML Output (Stylish Card)
        st.subheader("🌐 HTML Output Preview")
        html_output = f"""
        <div style='
            border: 2px solid #4CAF50;
            padding: 20px;
            border-radius: 15px;
            background-color: #f9f9f9;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            font-family: Arial;
        '>
            <h3 style='color:#4CAF50;'>Accessory Recommendation</h3>
            <p><strong>Query:</strong> {query}</p>
            <p><strong>Laptop:</strong> {laptop_model}</p>
            <p><strong>Interest:</strong> {interest}</p>
            <p><strong>Suggested Accessory:</strong> <span style='color:#1E88E5;'>{recommendation}</span></p>
            <p><strong>Feedback:</strong> {feedback}</p>
        </div>
        """
        st.markdown(html_output, unsafe_allow_html=True)


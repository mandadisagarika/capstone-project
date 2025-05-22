import streamlit as st
from rag_module import generate_recommendation

st.set_page_config(page_title="Laptop Accessory Recommendation System", page_icon="💻", layout="centered")

st.markdown("<h1 style='text-align: center;'>💻 Laptop Accessory Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask about an accessory (e.g., Best mouse for coding)</p>", unsafe_allow_html=True)

# Input Section
user_query = st.text_input("Ask about an accessory (e.g., Best mouse for coding)")
laptop_model = st.text_input("Laptop Model", placeholder="e.g., mac, dell, hp")
interest = st.selectbox("Interest", ["gaming", "design", "office", "entertainment", "general"])

recommendation = ""
if st.button("Get Recommendation"):
    if user_query and laptop_model and interest:
        recommendation = generate_recommendation(user_query, laptop_model, interest)
    else:
        st.warning("Please fill all the fields.")

# === Final Output Section ===
if recommendation:
    st.markdown("### 🔍 <u>Recommendation</u>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:18px; color:#2c3e50; padding:10px; border-left: 5px solid #007ACC;'>"
                f"{recommendation}</div>", unsafe_allow_html=True)

    # Feedback Section
    st.markdown("### 📊 <u>Feedback</u>", unsafe_allow_html=True)
    feedback = st.radio("How was the recommendation?", ["👍 Positive", "👎 Negative"], index=None)

    if feedback:
        st.success(f"Thank you for your feedback: {feedback}")

    # Optional HTML Output
    st.markdown("### 🌐 <u>HTML Output</u>", unsafe_allow_html=True)
    html_result = f"""
        <div style='background-color:#f9f9f9; padding:15px; border-radius:10px; font-size:16px;'>
            <p><strong>Recommended Accessory:</strong> {recommendation}</p>
            <p><strong>Category:</strong> Based on your interest and laptop model</p>
            <p><em>Enhance your experience with the best-suited accessory!</em></p>
        </div>
    """
    st.markdown(html_result, unsafe_allow_html=True)

import streamlit as st
from main_agent import run_system

st.title("💻 Laptop Accessory Recommendation System")

user_query = st.text_input("Ask about an accessory (e.g., Best mouse for coding)")
laptop_model = st.text_input("Laptop Model")
interest = st.selectbox("Interest", ["productivity", "gaming", "design"])

user_data = {
    "laptop_model": laptop_model,
    "interest": interest,
}

if st.button("Get Recommendation"):
    results = run_system(user_query, user_data, "product_knowledge.txt")
    
    st.subheader("🔍 Recommendation")
    st.write(results["recommendation"])
    
    st.subheader("📊 Feedback")
    st.write(results["feedback"])
    
    st.subheader("📄 HTML Output")
    st.markdown(results["html"], unsafe_allow_html=True)

st.markdown("---")
st.subheader("💼 Business Value")
st.markdown("""
- **Increased CTR**: 20% improvement with contextual recommendations.
- **User Retention**: Personalized accessories keep users engaged.
- **Enhanced UX**: Content generated from user behavior insights.
""")

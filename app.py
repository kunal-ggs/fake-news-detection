import streamlit as st
import pickle

# Load Model
with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📰 Fake News Detection")
st.write("Enter a news article and click Predict.")
st.info("💡 For best results, enter a complete news article or a detailed paragraph upto 250 words instead of a single sentence.")
st.markdown("---")
st.caption("Developed by Kunal")

news = st.text_area("Enter News")

if st.button("Predict"):

    prediction = model.predict([news])

    if prediction[0] == 0:
        st.error("🚨 Fake News")
    else:
        st.success("✅ True News")
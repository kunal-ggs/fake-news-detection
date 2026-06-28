import streamlit as st
import pickle

# Load Model
with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📰 Fake News Detection")

st.write("Enter a news article and click Predict.")

st.caption("🤖 Model: Passive Aggressive Classifier + TF-IDF")

st.info("💡 For best results, paste a complete news article instead of a single sentence or headline.")

st.warning("""
⚠️ Disclaimer

• This model is trained on a historical dataset.
• Predictions are based only on the input text and are not 100% accurate.
• The model may not recognize recent events or newly emerging news.
• Please verify important news from trusted sources before making any decisions.

This project is developed for educational and demonstration purposes.
""")

st.markdown("---")

news = st.text_area("Enter News", height=200)

if st.button("Predict"):

    if news.strip() == "":
        st.warning("⚠ Please enter a news article.")
    else:
        prediction = model.predict([news])

        if prediction[0] == 0:
            st.error("🚨 Fake News")
        else:
            st.success("✅ True News")

st.markdown("---")
st.markdown("**Developed By:** Kunal Turkar")
st.markdown("🔗 GitHub: https://github.com/kunal-ggs/fake-news-detection")  
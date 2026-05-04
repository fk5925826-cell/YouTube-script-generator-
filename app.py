import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Aapki API Key yahan set kar di gayi hai
genai.configure(api_key="AIzaSyA_nvMb8sdEUMu5eUwnv59QkmtTsf5ubIQ")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="AI YouTube Script Writer", page_icon="🎬")

# --- UI DESIGN ---
st.title("🎬 Professional YouTube Script Generator")
st.markdown("Apna topic likhein aur AI aapke liye professional script likh dega.")

# Input Section
topic = st.text_input("Video ka Topic:", placeholder="Yahan likhein (e.g. Benefits of Green Tea)")

# Professional Options
col1, col2 = st.columns(2)
with col1:
    tone = st.selectbox("Script ka style:", ["Professional", "Funny", "Storytelling", "Educational"])
with col2:
    length = st.selectbox("Video ki length:", ["Short (1 min)", "Medium (5 min)", "Long (10+ min)"])

# --- GENERATION LOGIC ---
if st.button("Generate Script ✨"):
    if topic:
        with st.spinner('AI Script likh raha hai...'):
            prompt = f"""
            Write a highly professional YouTube script for the topic: {topic}.
            The tone should be {tone} and the video length is roughly {length}.
            Include:
            1. An eye-catching Hook.
            2. Introduction.
            3. Detailed Main Content (Body).
            4. Call to Action (Subscribe, etc).
            5. Outro.
            Language: Urdu/Hindi mixed with English (Hinglish) so it sounds natural and professional.
            """
            
            try:
                response = model.generate_content(prompt)
                st.success("Aapki Script Taiyar Hai! ✅")
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle koi topic toh likhein!")

st.markdown("---")
st.caption("Powered by Gemini AI | Created by Your Name")

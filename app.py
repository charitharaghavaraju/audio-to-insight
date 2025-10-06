import streamlit as st
from audio_insight import run_pipeline

st.title("🎧 Audio-to-Insight Assistant")

audio_file = st.file_uploader("Upload your meeting audio", type=["mp3", "wav", "m4a"])
user_query = st.text_input("Ask a question about the meeting")

if st.button("Analyze"):
    if audio_file and user_query:
        with open("temp_audio.mp3", "wb") as f:
            f.write(audio_file.read())
        answer = run_pipeline("temp_audio.mp3", user_query)
        st.write(answer)
    else:
        st.warning("Please upload an audio file and enter a query.")


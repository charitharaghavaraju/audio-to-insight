# 🎧 Audio-to-Insight Assistant (Offline)

A local **AI-powered meeting/audio assistant** that converts speech to text, analyzes the content, and answers questions about the audio — all on your MacBook Air M4 **without internet or API costs**.

This project combines **speech-to-text**, **semantic search**, and **local LLM reasoning** to provide actionable insights from audio files like meeting recordings, lectures, or podcasts.

---

## 🚀 Features

- **Audio Transcription**: Converts `.mp3` or `.wav` or `.m4a` audio into text using [Faster Whisper](https://github.com/guillaumekln/faster-whisper).  
- **Text Chunking**: Splits transcripts into manageable pieces for better embedding and semantic search.  
- **Semantic Search**: Uses [Sentence Transformers](https://www.sbert.net/) + [ChromaDB](https://www.trychroma.com/) to find relevant parts of the transcript.  
- **Local LLM Question Answering**: Uses [Ollama](https://ollama.com/) with LLaMA 3 / Mistral for reasoning and generating human-like answers.  
- **Interactive Web UI**: Built with [Streamlit](https://streamlit.io/) for uploading audio and asking questions directly in your browser.  
- **Fully Offline**: No OpenAI or cloud API costs — everything runs locally.

---

## 🛠️ Tech Stack

| Component                  | Technology / Library                   |
|-----------------------------|--------------------------------------|
| Audio Transcription         | `faster-whisper`                     |
| Embeddings & Semantic Search| `sentence-transformers` + `chromadb` |
| LLM Reasoning               | `ollama` (local LLaMA 3 / Mistral)  |
| Pipeline Orchestration      | `langchain`                          |
| Web Interface               | `streamlit`                          |
| Language                     | Python 3.11+                          |

---

## ⚡ Setup Guide (MacBook Air M4)

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/audio-to-insight.git
cd audio-to-insight
```

### 2️⃣ Create a virtual environment
```bash 
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install --upgrade pip
pip install faster-whisper sentence-transformers chromadb langchain streamlit tiktoken
```

### 4️⃣ Install Ollama (local LLM)
1. Download Ollama: https://ollama.com/download

2. Pull a local model, e.g., LLaMA 3:
```bash 
ollama pull llama3
```

### 5️⃣ Prepare your audio
Add a small .mp3 or .wav or .m4a file to the project folder (e.g., meeting.mp3).

### 🏃 Running the App
## Run via Streamlit:
```bash
streamlit run app.py
```

1. Open the Streamlit page in your browser.

2. Upload your audio file.

3. Enter a question about the meeting or lecture.

4. Click Analyze — the AI answer appears instantly on the page.

## Run via Terminal (Optional):
```bash
python3 audio_insight.py
```

## Example query:
```bash
"Summarize the main discussion points and next steps."````



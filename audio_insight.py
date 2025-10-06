from transcribe import transcribe_audio
from chunk_text import chunk_text
from query_engine import query_meeting
from embed_store import create_vector_store

def run_pipeline(audio_file, user_query):
    print("🎧 Transcribing audio...")
    transcript = transcribe_audio(audio_file)
    print("✅ Transcription complete!")

    print("🧩 Chunking and embedding...")
    chunks = chunk_text(transcript)
    _, collection = create_vector_store(chunks)

    print("💬 Querying model...")
    answer = query_meeting(collection, user_query)
    print("\n🧠 AI Answer:\n", answer)

    return answer

if __name__ == "__main__":
    run_pipeline("meeting.m4a", "Summarize the main discussion points and next steps.")
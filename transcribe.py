from faster_whisper import WhisperModel

def transcribe_audio(file_path: str) -> str:
    model = WhisperModel("base", device="cpu")
    segments, _ = model.transcribe(file_path)
    transcript = " ".join([seg.text.strip() for seg in segments])
    return transcript

if __name__ == "__main__":
    text = transcribe_audio("meeting.m4a")
    print(text[:500])
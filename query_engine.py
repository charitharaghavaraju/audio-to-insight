from sentence_transformers import SentenceTransformer
import chromadb
import subprocess

def query_meeting(collection, user_query, n_results=3):
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    query_emb = embedder.encode([user_query])[0]
    results = collection.query(query_embeddings=[query_emb], n_results=n_results)
    retrieved_text = " ".join(results["documents"][0])

    prompt = f"""
        You are an assistant analyzing a meeting transcript.
        Use the provided context to answer clearly and briefly.

        Context:
        {retrieved_text}

        Question: {user_query}
        Answer:
        """

    cmd = ["ollama", "run", "llama3", prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

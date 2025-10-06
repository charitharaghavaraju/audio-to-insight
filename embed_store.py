from sentence_transformers import SentenceTransformer
import chromadb

def create_vector_store(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.Client()
    collection = client.create_collection(name="meeting_notes")

    embeddings = model.encode(chunks)

    collection.add(documents=chunks,
            embeddings=embeddings,
            ids=[str(i) for i in range(len(chunks))]
        )
    
    return client, collection
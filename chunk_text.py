from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text: str, chunk_size = 500, chunk_overlap = 100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_text(text)
    return chunks
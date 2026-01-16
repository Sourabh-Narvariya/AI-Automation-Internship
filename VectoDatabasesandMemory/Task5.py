
from google.colab import files
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
import uuid

uploaded = files.upload()   # upload: sample.pdf
pdf_name = list(uploaded.keys())[0]
pdf_path = f"/content/{pdf_name}"

def load_pdf(path):
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start:start + chunk_size].strip()
        if len(chunk) > 30:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

pdf_text = load_pdf(pdf_path)
chunks = chunk_text(pdf_text)

print("Total chunks:", len(chunks))

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks).tolist()

client = chromadb.Client()
collection = client.get_or_create_collection("pdf_vectors")

collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[str(uuid.uuid4()) for _ in range(len(chunks))]
)

print("PDF vector index created.")

query = "What is this PDF about?"
query_embedding = model.encode([query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

print("Top Matching Chunks:\n")
for doc in results["documents"][0]:
    print(doc[:200])
    print("----")
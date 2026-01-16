from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Machine learning is transforming the world",
    "Artificial intelligence is changing industries",
    "Deep learning is a subset of machine learning",
    "I love playing badminton",
    "Sports improve physical and mental health"
]

embeddings = model.encode(documents)


dimension = embeddings.shape[1]  # 384
index = faiss.IndexFlatL2(dimension)  # L2 distance

index.add(embeddings)

print("Total vectors in index:", index.ntotal)


query = "AI and machine learning"
query_embedding = model.encode([query])

k = 3  # top results
distances, indices = index.search(query_embedding, k)

print("Query:", query)
print("\nTop results:")
for idx in indices[0]:
    print("-", documents[idx])
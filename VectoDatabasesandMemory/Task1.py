from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Machine learning is transforming the world",
    "Artificial intelligence is changing industries",
    "I love playing badminton"
]
embeddings = model.encode(sentences)

print("Number of sentences:", len(embeddings))
print("Embedding size:", len(embeddings[0]))
print("First embedding (first 10 values):", embeddings[0][:10])

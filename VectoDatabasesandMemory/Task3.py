from sentence_transformers import SentenceTransformer
import chromadb
from transformers import pipeline

documents = [
    "Machine learning is a field of AI that allows systems to learn from data.",
    "Deep learning is a subset of machine learning using neural networks.",
    "RAG stands for Retrieval Augmented Generation.",
    "ChromaDB is a vector database used to store embeddings.",
    "Sentence transformers generate semantic embeddings."
]

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection(name="rag_collection")

embeddings = model.encode(documents).tolist()
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[str(i) for i in range(len(documents))]
)

query = "What is RAG?"
query_embedding = model.encode([query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=2
)

retrieved_docs = results["documents"][0]

print("Retrieved context:")
for doc in retrieved_docs:
    print("-", doc)

context = "\n".join(retrieved_docs)

prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}

Answer:
"""

print("\nFINAL PROMPT SENT TO LLM:\n")
print(prompt)

generator = pipeline(
    task="text-generation",
    model="openai-community/gpt2",
    max_new_tokens=80,
    temperature=0.7,
    do_sample=False
)

outputs = generator(prompt)
full_text = outputs[0]["generated_text"]

gen = full_text[len(prompt):].strip()

gen = gen.split("Question:")[0].strip()

print("\nRAG ANSWER:\n", gen)
# Vector Databases and Memory

This module covers vector embeddings, vector databases (FAISS, ChromaDB), and building RAG (Retrieval Augmented Generation) systems for AI applications.

## 📚 What I Learned

- Creating text embeddings with Sentence Transformers
- Vector similarity search
- FAISS (Facebook AI Similarity Search) for efficient indexing
- ChromaDB for vector storage
- RAG (Retrieval Augmented Generation) implementation
- PDF document processing and chunking
- Building semantic search systems

## 🎯 Learning Resources

- Sentence Transformers Documentation
- FAISS Official Guide
- ChromaDB Documentation
- RAG Systems Best Practices
- Vector Database Concepts

## 📝 Tasks Completed

### Task 1: Create Text Embeddings
**File:** `Task1.py`

Generate semantic embeddings using Sentence Transformers:
- Load pre-trained embedding model (all-MiniLM-L6-v2)
- Convert text sentences to vector embeddings
- Display embedding dimensions and values
- Understand vector representation of text

**Features:**
- 384-dimensional embeddings
- Fast encoding
- Semantic meaning capture

**Run:**
```bash
python Task1.py
```

**Output:**
- Number of sentences encoded
- Embedding size (384)
- Sample embedding values

### Task 2: FAISS Vector Search
**File:** `Task2.py`

Build a vector search system using FAISS:
- Create embeddings for multiple documents
- Build FAISS index with L2 distance
- Perform similarity search
- Retrieve top-k most relevant documents

**Features:**
- Fast vector similarity search
- L2 (Euclidean) distance metric
- Efficient indexing for large datasets
- Query-based retrieval

**Example:**
```python
Query: "AI and machine learning"
Results:
- Machine learning is transforming the world
- Artificial intelligence is changing industries
- Deep learning is a subset of machine learning
```

**Run:**
```bash
python Task2.py
```

### Task 3: RAG System with ChromaDB
**File:** `Task3.py`

Build a complete RAG (Retrieval Augmented Generation) system:
- Store documents in ChromaDB vector database
- Perform semantic search on query
- Retrieve relevant context
- Generate answers using retrieved context
- Use text generation pipeline

**RAG Pipeline:**
1. **Store:** Documents → Embeddings → ChromaDB
2. **Retrieve:** Query → Similar documents
3. **Generate:** Context + Query → LLM → Answer

**Features:**
- Persistent vector storage
- Semantic retrieval
- Context-aware generation
- Question answering

**Example Flow:**
```
Query: "What is RAG?"
Retrieved Context:
- RAG stands for Retrieval Augmented Generation
- ChromaDB is a vector database used to store embeddings
Generated Answer: [Based on context]
```

**Run:**
```bash
python Task3.py
```

### Task 5: PDF Vector Index and Search
**File:** `Task5.py`

Advanced RAG system for PDF documents:
- Upload and read PDF files
- Extract text from all pages
- Chunk text with overlap for better context
- Create vector embeddings for chunks
- Store in ChromaDB
- Perform semantic search on PDF content

**Features:**
- PDF text extraction
- Smart chunking (300 chars with 50 overlap)
- UUID-based document IDs
- Multi-chunk retrieval
- PDF question answering

**Process:**
1. Upload PDF via Colab interface
2. Extract and chunk text
3. Generate embeddings
4. Store in vector database
5. Query and retrieve relevant sections

**Run (in Google Colab):**
```python
# Upload PDF file when prompted
python Task5.py
```

**Example:**
```
Query: "What is this PDF about?"
Returns: Top 3 most relevant chunks from PDF
```

## 🚀 How to Run All Tasks

### Prerequisites
```bash
pip install sentence-transformers faiss-cpu chromadb
pip install transformers pypdf
```

**Note:** For GPU acceleration:
```bash
pip install faiss-gpu
```

### Individual Task Execution

**Task 1:** Create Embeddings
```bash
python Task1.py
```

**Task 2:** FAISS Vector Search
```bash
python Task2.py
```

**Task 3:** RAG with ChromaDB
```bash
python Task3.py
```

**Task 5:** PDF RAG System (Run in Google Colab)
```python
# In Colab
%run Task5.py
# Upload PDF when prompted
```

## 💡 Key Concepts

### Vector Embeddings
- Convert text to numerical vectors (384 dimensions)
- Capture semantic meaning
- Enable similarity comparison

### Vector Databases
- **FAISS:** Fast similarity search, in-memory
- **ChromaDB:** Persistent storage, easy to use
- Both support similarity metrics (L2, cosine)

### RAG System Components
1. **Retrieval:** Find relevant documents using vector search
2. **Augmentation:** Add retrieved context to query
3. **Generation:** LLM generates answer from context

### Text Chunking
- Break long documents into smaller pieces
- Add overlap to preserve context
- Optimal chunk size: 200-500 characters
- Overlap: 10-20% of chunk size

## 🎨 Practical Applications

1. **Semantic Search:** Find similar documents, articles, code
2. **Question Answering:** Build chatbots with document knowledge
3. **Document Analysis:** Search through PDFs, books, papers
4. **Recommendation Systems:** Content, product recommendations
5. **Knowledge Base:** Company documentation, FAQs
6. **Research Assistant:** Academic paper search and summarization

## 📊 Technologies Used

| Technology | Purpose | Type |
|------------|---------|------|
| Sentence Transformers | Text Embeddings | Model |
| FAISS | Vector Search | Database |
| ChromaDB | Vector Storage | Database |
| PyPDF | PDF Processing | Library |
| Transformers | Text Generation | Framework |

## 🔧 Model Details

**all-MiniLM-L6-v2:**
- Size: 22M parameters
- Embedding dimension: 384
- Speed: Very fast
- Quality: Good for most tasks
- Use case: General-purpose embeddings

## ⚠️ Important Notes

1. **Memory:** FAISS indexes stored in RAM
2. **Persistence:** ChromaDB can persist to disk
3. **Chunk Size:** Affects retrieval quality
4. **Overlap:** Prevents context loss between chunks
5. **Colab Required:** Task 5 uses Colab file upload
6. **Model Download:** First run downloads embedding model (~80MB)

## 🔍 Performance Tips

- Use `faiss-gpu` for large-scale search
- Adjust chunk size based on document type
- Increase overlap for complex documents
- Use appropriate similarity metrics
- Consider hybrid search (vector + keyword)

## 📈 Comparison: FAISS vs ChromaDB

| Feature | FAISS | ChromaDB |
|---------|-------|----------|
| Speed | Very Fast | Fast |
| Persistence | In-memory | Disk storage |
| Setup | Complex | Easy |
| Scale | Billions | Millions |
| Metadata | No | Yes |
| Best For | Large scale | Small to medium |

---

**Module Status:** ✅ Completed (4/4 tasks)  
**Next Steps:** Build production RAG systems, explore Pinecone, Weaviate, implement hybrid search

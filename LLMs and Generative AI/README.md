# LLMs and Generative AI

This module covers Large Language Models (LLMs) and Generative AI technologies, including working with Hugging Face, Google Gemini, text generation, and image generation.

## 📚 What I Learned

- Understanding Large Language Models (LLMs)
- Hugging Face Transformers library
- Google Gemini API integration
- Text generation with transformers
- Image generation with Stable Diffusion
- Prompt engineering and optimization
- Building chatbots with LLMs
- Multi-modal AI applications

## 🎯 Learning Resources

- Hugging Face Official Documentation
- Google Generative AI API Guide
- Transformers Library Tutorial
- Diffusers Library Documentation
- Prompt Engineering Best Practices

## 📝 Tasks Completed

### Task 1: Explore Hugging Face and List 5 LLMs
**File:** `3_Task1.txt`

Research and documentation of 5 popular LLMs on Hugging Face:

1. **Llama** (Meta)
   - Parameters: 7B to 405B
   - Use Cases: Research, chat applications, code generation
   - Features: Efficient inference, rotary positional embeddings

2. **Mistral** (Mistral AI)
   - Example: Mistral 7B
   - Use Cases: Conversational AI, instruction-following, multilingual tasks
   - Strength: High performance on leaderboards

3. **Gemma** (Google)
   - Parameters: 2B and 7B variants
   - Use Cases: Lightweight deployment, mobile, edge devices
   - Ideal For: Summarization, question-answering, instruction-tuning

4. **Phi** (Microsoft)
   - Model: Phi-2 (2.7B parameters)
   - Use Cases: Educational tools, logical reasoning, NLP
   - Strength: Strong common sense reasoning

5. **Qwen** (Alibaba)
   - Features: Multilingual support (12 languages)
   - Use Cases: Exams, translation, math tasks
   - Integration: Works with Hugging Face Transformers

### Task 2: Text Generation with Hugging Face Pipeline
**File:** `3_Task2.py`

Simple text generation using Transformers pipeline:
- Load GPT-2 model
- Generate text from a prompt
- Parameters: max_tokens, temperature, sampling
- Output: Contextual continuation of input text

**Run:**
```bash
python 3_Task2.py
```

**Sample Output:**
```
Input: "the future of AI development in india is"
Output: "the future of AI development in india is very bright and full of opportunities..."
```

### Task 3: Gemini API - Simple Prompt Response
**File:** `3_Task3.py`

Interactive prompt-response using Google Gemini API:
- Configure Gemini API key
- Load Gemini 2.5 Flash model
- Accept user input as prompt
- Generate and display response

**Setup:**
1. Get API key from: https://aistudio.google.com/
2. Replace `YOUR_API_KEY` in code
3. Install: `pip install google-generativeai`

**Run:**
```bash
python 3_Task3.py
Enter your prompt: What is artificial intelligence?
```

### Task 4: Prompt Engineering with Gemini
**File:** `3_Task4.py`

Advanced prompt engineering demonstrating template variations:
- Create prompt templates with placeholders
- Test multiple variations (role, topic, style, audience, length)
- Compare outputs from different prompt configurations

**Variations Tested:**
1. **Variation 1:** AI engineer explaining AI to school students (simple, short)
2. **Variation 2:** Data Scientist explaining ML to college students (technical, medium)
3. **Variation 3:** Teacher explaining Deep Learning to beginners (easy, detailed)

**Features:**
- Template-based prompt generation
- Role-based explanations
- Style variation (simple, technical, easy)
- Audience-specific content
- Length control (short, medium, detailed)

**Run:**
```bash
python 3_Task4.py
```

### Task 5: Gemini Chatbot with Conversation History
**File:** `3_Task5.py`

Interactive chatbot with multi-turn conversations:
- Start chat session with Gemini
- Maintain conversation history
- Send/receive messages in a loop
- Exit command to end conversation

**Features:**
- Real-time conversation
- Automatic context preservation
- Natural dialogue flow
- Exit option

**Run:**
```bash
python 3_Task5.py

Gemini Chatbot
Type 'exit' to end the conversation.

You: Hello, what can you do?
Chatbot: I can help you with...
```

### Task 6: Multi-Modal AI - Text and Image Generation
**File:** `3_Task6.py`

Combined text and image generation using multiple models:
- **Text Generation:** GPT-2 for text
- **Image Generation:** Stable Diffusion v1.5
- User input for both modalities
- GPU acceleration support

**Models Used:**
- Text: `gpt2` (Hugging Face)
- Image: `runwayml/stable-diffusion-v1-5`

**Features:**
- Text prompt for text generation
- Image prompt for image generation
- CUDA support for faster processing
- Display generated images

**Requirements:**
```bash
pip install transformers diffusers torch
```

**Run:**
```bash
python 3_Task6.py
Enter text prompt: The future of technology
Describe image to generate: A futuristic city with AI robots
```

**Note:** Requires GPU for image generation (CUDA compatible)

## 🚀 How to Run All Tasks

### Prerequisites
```bash
pip install transformers
pip install google-generativeai
pip install diffusers
pip install torch
```

### Individual Task Execution

**Task 1:** Read the documentation file
```
View: 3_Task1.txt
```

**Task 2:** Text generation with Transformers
```bash
python 3_Task2.py
```

**Task 3:** Simple Gemini API
```bash
# Set up API key first
python 3_Task3.py
```

**Task 4:** Prompt engineering variations
```bash
python 3_Task4.py
```

**Task 5:** Interactive chatbot
```bash
python 3_Task5.py
```

**Task 6:** Multi-modal AI (requires GPU)
```bash
python 3_Task6.py
```

## 🔑 API Keys Needed

### Google Gemini API
1. Visit: https://aistudio.google.com/
2. Click "Get API Key"
3. Create new API key
4. Replace `YOUR_API_KEY` in files

### Hugging Face (Optional)
1. Visit: https://huggingface.co/
2. Create account
3. Generate token in settings
4. Use for private models

## 💡 Key Learnings

- ✅ Understanding LLM capabilities and use cases
- ✅ Using Hugging Face Transformers for inference
- ✅ API integration with Google Gemini
- ✅ Prompt engineering best practices
- ✅ Multi-turn conversation management
- ✅ Multi-modal AI (text + image generation)
- ✅ Model selection and optimization
- ✅ API key management and security

## 🎨 Practical Applications

1. **Chatbots:** Customer support, virtual assistants
2. **Content Generation:** Blog posts, summaries, translations
3. **Image Generation:** Creative content, prototyping, design
4. **Code Generation:** Development assistance, debugging
5. **Data Analysis:** Data interpretation, insights generation
6. **Education:** Personalized learning, tutoring

## 📊 Model Comparison

| Model | Provider | Parameters | Speed | Accuracy | Cost |
|-------|----------|-----------|-------|----------|------|
| Llama | Meta | 7B-405B | Fast | High | Free/Paid |
| Mistral | Mistral | 7B+ | Fast | High | Free |
| Gemini | Google | Large | Medium | Very High | Paid |
| GPT-2 | OpenAI | 1.5B | Fast | Good | Free |
| Phi | Microsoft | 2.7B | Very Fast | Good | Free |

## ⚠️ Important Notes

1. **API Keys:** Keep your API keys secret and never commit them to GitHub
2. **Rate Limits:** Gemini API has rate limits; handle errors gracefully
3. **GPU Requirements:** Image generation requires GPU for reasonable performance
4. **Model Size:** Large models require significant disk space
5. **Internet:** API calls require stable internet connection

---

**Module Status:** ✅ Completed (6/6 tasks)  
**Next Steps:** Integrate LLMs with web applications, build advanced RAG systems

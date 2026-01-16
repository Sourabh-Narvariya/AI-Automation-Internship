# Hugging Face and Advanced Features

This module covers advanced Hugging Face features including sentiment analysis, text-to-speech, Telegram bot integration, dataset handling, Gradio interfaces, and model fine-tuning.

## 📚 What I Learned

- Hugging Face Transformers pipelines
- Sentiment analysis with DistilBERT
- Text-to-Speech with SpeechT5
- Telegram bot with Gemini AI integration
- Loading and exploring datasets
- Building Gradio interfaces
- Fine-tuning models with Trainer API

## 🎯 Learning Resources

- Hugging Face Transformers Documentation
- Hugging Face Datasets Library
- Gradio Official Guide
- Python Telegram Bot Documentation
- Model Fine-tuning Best Practices

## 📝 Tasks Completed

### Task 1: Sentiment Analysis with Transformers
**File:** `Task1.py`

Sentiment analysis using Hugging Face pipeline:
- Load DistilBERT model for sentiment analysis
- Analyze multiple text samples
- Display sentiment labels (POSITIVE/NEGATIVE) with confidence scores

**Run:**
```bash
python Task1.py
```

### Task 2: Text-to-Speech with SpeechT5
**File:** `Task2.py`

Convert text to speech using Microsoft's SpeechT5:
- Load SpeechT5 TTS model and processor
- Generate speech from text input
- Apply vocoder for audio generation
- Normalize and display audio in Jupyter/Colab

**Requirements:**
```bash
pip install transformers torch IPython
```

### Task 3: Telegram Bot with Gemini AI
**File:** `Task3.py`

Build an AI-powered Telegram bot:
- Integrate Google Gemini API
- Handle commands (/start, /help)
- Process user messages and generate AI responses
- Support group chats with bot mentions
- Error handling and async operations

**Setup:**
1. Get Telegram Bot token from @BotFather
2. Get Gemini API key from Google AI Studio
3. Update tokens in code

**Requirements:**
```bash
pip install python-telegram-bot nest-asyncio google-generativeai
```

### Task 4: Loading Datasets from Hugging Face
**File:** `Task4.py`

Explore Hugging Face datasets:
- Load IMDB movie review dataset
- Display sample data with labels
- Understand dataset structure
- Preview text content

**Run:**
```bash
python Task4.py
```

### Task 5: Gradio Text Generation Interface
**File:** `Task5.py`

Interactive text generation with Gradio:
- Load GPT-2 model and tokenizer
- Build web UI with Gradio
- Generate text from user prompts
- Configure generation parameters (temperature, top_p, etc.)
- Share interface with public link

**Features:**
- Real-time text generation
- Web-based interface
- Adjustable generation settings
- Public shareable link

**Run:**
```bash
python Task5.py
```

### Task 6: Fine-tuning a Model
**File:** `Task6.py`

Fine-tune DistilBERT on IMDB dataset:
- Load and preprocess IMDB dataset
- Tokenize text with DistilBERT tokenizer
- Set up TrainingArguments
- Use Trainer API for fine-tuning
- Evaluate with accuracy and F1 metrics
- Train on small subset for demo

**Features:**
- Custom tokenization function
- Training configuration
- Evaluation metrics
- Model saving

**Requirements:**
```bash
pip install transformers datasets scikit-learn
```

## 🚀 How to Run All Tasks

### Prerequisites
```bash
pip install transformers torch datasets gradio
pip install python-telegram-bot nest-asyncio google-generativeai
pip install scikit-learn IPython
```

### Individual Task Execution

**Task 1:** Sentiment Analysis
```bash
python Task1.py
```

**Task 2:** Text-to-Speech (Run in Colab/Jupyter)
```python
# In Jupyter/Colab
%run Task2.py
```

**Task 3:** Telegram Bot
```bash
# Update API keys first
python Task3.py
```

**Task 4:** Load Dataset
```bash
python Task4.py
```

**Task 5:** Gradio Interface
```bash
python Task5.py
# Opens web interface
```

**Task 6:** Fine-tuning
```bash
python Task6.py
```

## 🔑 API Keys Required

### Telegram Bot (Task 3)
1. Message @BotFather on Telegram
2. Create new bot with /newbot
3. Get bot token
4. Update `TOKEN` in Task3.py

### Google Gemini (Task 3)
1. Visit: https://aistudio.google.com/
2. Get API key
3. Update `GEMINI_API_KEY` in Task3.py

## 💡 Key Learnings

- ✅ Using Hugging Face pipelines for quick inference
- ✅ Loading pre-trained models (DistilBERT, GPT-2, SpeechT5)
- ✅ Building chatbots with AI integration
- ✅ Working with large datasets efficiently
- ✅ Creating interactive ML demos with Gradio
- ✅ Fine-tuning models on custom data
- ✅ Evaluation metrics for classification

## 🎨 Practical Applications

1. **Sentiment Analysis:** Product reviews, social media monitoring
2. **Text-to-Speech:** Accessibility tools, audiobooks, voice assistants
3. **Chatbots:** Customer support, virtual assistants
4. **Dataset Exploration:** Research, model training
5. **Gradio Demos:** Model showcases, prototyping
6. **Fine-tuning:** Custom domain adaptation, specialized models

## 📊 Models Used

| Task | Model | Purpose | Size |
|------|-------|---------|------|
| Task 1 | DistilBERT | Sentiment Analysis | 66M params |
| Task 2 | SpeechT5 | Text-to-Speech | 80M params |
| Task 3 | Gemini 2.5 | Chat/Generation | Large |
| Task 5 | GPT-2 | Text Generation | 124M params |
| Task 6 | DistilBERT | Fine-tuning | 66M params |

## ⚠️ Important Notes

1. **GPU Recommended:** Tasks 2, 5, 6 benefit from GPU acceleration
2. **API Limits:** Gemini API has rate limits
3. **Model Size:** Models download on first run (requires internet)
4. **Memory:** Fine-tuning requires adequate RAM
5. **Gradio Share:** Share links expire after 72 hours

---

**Module Status:** ✅ Completed (6/6 tasks)  
**Next Steps:** Deploy models, build production apps, explore more advanced architectures

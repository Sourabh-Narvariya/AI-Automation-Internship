# Multi-Step Agent: Extract → Summarize → Email

A sophisticated multi-step agent system that demonstrates workflow orchestration using LangGraph.

## 🎯 Features

This agent performs three sequential steps:

1. **Data Extraction** - Retrieves information from Wikipedia about any topic
2. **Summarization** - Uses LLM to create a concise, well-structured summary
3. **Email Delivery** - Sends the summary via email with professional formatting

## 🏗️ Architecture

The agent uses **LangGraph's StateGraph** to create a sequential workflow:

```
┌─────────────┐     ┌──────────────┐     ┌───────────┐
│   Extract   │ --> │  Summarize   │ --> │   Email   │
│    Data     │     │     Data     │     │   Send    │
└─────────────┘     └──────────────┘     └───────────┘
```

Each step:
- Receives state from the previous step
- Performs its operation
- Updates the state
- Passes control to the next step

## 🚀 Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Required
GROQ_API_KEY=your_groq_api_key

# Optional (for email functionality)
SENDER_EMAIL=your_email@gmail.com
RECIPIENT_EMAIL=recipient@example.com
EMAIL_PASSWORD=your_app_password
```

**Note:** For Gmail, use an [App Password](https://myaccount.google.com/apppasswords), not your regular password.

### 3. Run the Agent

```bash
python AG_task2.py
```

## 📝 Usage

### Basic Usage

```python
from AG_task2 import run_multi_step_agent

# Run the agent on any topic
result = run_multi_step_agent("Artificial Intelligence")
```

### Customize Topics

Edit the `topics` list in the main block:

```python
if __name__ == "__main__":
    topics = [
        "Climate Change",
        "Quantum Computing",
        "SpaceX",
    ]
    
    for topic in topics:
        result = run_multi_step_agent(topic)
```

## 🔧 How It Works

### State Management

The agent uses a typed state dictionary that flows through all steps:

```python
class AgentState(TypedDict):
    topic: str           # Input topic
    raw_data: str        # Extracted data
    summary: str         # Generated summary
    email_sent: bool     # Email status
    error: str           # Error messages
```

### Step 1: Data Extraction

- Uses Wikipedia API via LangChain
- Creates a ReAct agent with Wikipedia tool
- Extracts comprehensive information about the topic

### Step 2: Summarization

- Takes raw data from Step 1
- Uses Groq LLM (llama-3.1-8b-instant)
- Generates a 200-300 word structured summary
- Formats with bullet points and key facts

### Step 3: Email Delivery

- Creates professional HTML email
- Includes timestamp and topic metadata
- Sends via SMTP (Gmail, Outlook, etc.)
- Falls back to preview mode if credentials not configured

## 📧 Email Configuration

### Gmail Setup

1. Enable 2-Factor Authentication
2. Generate App Password: https://myaccount.google.com/apppasswords
3. Use App Password in `.env` file

### Other Email Providers

**Outlook/Hotmail:**
```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
```

**Yahoo:**
```env
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
```

## 🎨 Output Example

```
############################################################
MULTI-STEP AGENT STARTED
############################################################
Topic: Artificial Intelligence
Timestamp: 2026-01-15 10:30:00

============================================================
STEP 1: DATA EXTRACTION
============================================================
Topic: Artificial Intelligence

Extracted 2453 characters of data
Preview: Artificial Intelligence (AI) is the simulation of human...

============================================================
STEP 2: SUMMARIZATION
============================================================

Generated summary (287 characters)
Preview:
# Artificial Intelligence Summary

Artificial Intelligence (AI) represents a transformative...

============================================================
STEP 3: EMAIL DELIVERY
============================================================

✅ Email sent successfully!
   From: your_email@gmail.com
   To: recipient@example.com

############################################################
MULTI-STEP AGENT COMPLETED
############################################################
✓ Data extracted: 2453 characters
✓ Summary generated: 287 characters
✓ Email sent: True
```

## 🛠️ Customization

### Add Custom Data Sources

Extend the extraction node to include additional sources:

```python
@tool
def extract_from_custom_api(topic: str) -> str:
    """Extract data from your custom API."""
    # Your custom extraction logic
    pass
```

### Modify Summary Format

Adjust the summarization prompt in `summarization_node()`:

```python
summarization_prompt = f"""
    Create a technical deep-dive summary with:
    - Executive summary
    - Key technical concepts
    - Future implications
    ...
"""
```

### Add More Steps

Insert additional nodes in the workflow:

```python
workflow.add_node("translate", translation_node)
workflow.add_edge("summarize", "translate")
workflow.add_edge("translate", "email")
```

## 🔍 Troubleshooting

### Email Not Sending

- Check `.env` configuration
- Verify App Password (for Gmail)
- Check SMTP server and port
- Review firewall settings

### Wikipedia Extraction Fails

- Check internet connection
- Verify topic name is searchable
- Try alternative phrasing

### LLM Errors

- Verify GROQ_API_KEY in `.env`
- Check API quota/limits
- Ensure langchain-groq is installed

## 📚 Dependencies

- **langchain** - LLM framework
- **langchain-community** - Community tools (Wikipedia)
- **langchain-groq** - Groq LLM integration
- **langgraph** - Workflow orchestration
- **python-dotenv** - Environment configuration
- **wikipedia** - Wikipedia API wrapper

## 🎓 Learning Points

This project demonstrates:

1. **Multi-step agent workflows** using LangGraph
2. **State management** across agent steps
3. **Tool integration** (Wikipedia, Email)
4. **LLM-powered summarization**
5. **Error handling** and graceful degradation
6. **Professional email formatting**
7. **Environment-based configuration**

## 📄 License

MIT License - Feel free to modify and use as needed!

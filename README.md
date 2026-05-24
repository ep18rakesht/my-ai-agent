# My AI Agent 🤖

A fully local AI chatbot with a web interface — no internet required, 
no API keys, 100% free and private.

## What it does
- Answers any question you ask
- Remembers the full conversation (has memory)
- Runs entirely on your own laptop
- Works through a beautiful browser chat interface

## Tech stack
- Python
- Ollama (local AI runner)
- Llama 3.2 (free, open-source AI model by Meta)
- Flask (web server)
- HTML + CSS + JavaScript (chat interface)

## Project structure
my-ai-agent/
│
├── agent.py          ← Terminal version of the chatbot
├── app.py            ← Flask web server
├── templates/
│   └── index.html    ← Browser chat interface
└── requirements.txt

## How to run it

### Prerequisites
- Python 3.x installed
- Ollama installed from https://ollama.com

### 1. Clone this repo
```bash
git clone https://github.com/ep18rakesht/my-ai-agent.git
cd my-ai-agent
```

### 2. Install Ollama and download the model
```bash
ollama pull llama3.2
```

### 3. Create virtual environment and install dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install ollama flask
```

### 4. Run the terminal version
```bash
python agent.py
```

### 5. Run the web chat interface
```bash
python app.py
```
Then open your browser at **http://127.0.0.1:5000**

## How to use it
- Type any question and press Enter or click the send button
- The agent remembers the full conversation
- Click "Clear chat" to start a fresh conversation
- Type `quit` to exit the terminal version

## Built by
Rakesh Tiwari — built from scratch in one day! 🚀

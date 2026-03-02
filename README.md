# 📄 PDF Q&A Chatbot

A conversational AI chatbot that reads documents and answers questions about them — built from scratch using Python and LLM APIs.

## 🚀 What it does
- Reads any text document
- Lets you ask multiple questions about it in a conversation
- Maintains conversation history so answers stay in context
- Powered by LLaMA 3.3 via Groq API

## 🧠 How it works
1. Loads document content from a `.txt` file
2. Sends it as context to the LLM via system prompt
3. Keeps full conversation history so the AI remembers previous questions
4. Returns accurate, context-aware answers

## 🛠️ Tech Stack
- Python 3.13
- Groq API (LLaMA 3.3 70B)
- python-dotenv

## ⚙️ Setup & Run

1. Clone the repo
```bash
git clone https://github.com/Yadu080/pdf-qa.git
cd pdf-qa
```

2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install groq python-dotenv
```

4. Create a `.env` file and add your Groq API key
```
GROQ_API_KEY=your_key_here
```

5. Add your document content to `sample.txt` and run
```bash
python3 main.py
```

## 💬 Example
```
You: What is AWAAJ?
AI: AWAAJ is a real-time AI-based mobile app that translates Indo-Pakistani 
    Sign Language to English text or voice.

You: How accurate is it?
AI: Based on preliminary testing, it achieves 82% accuracy in translation.
```

## 📌 What I learned building this
- How LLM APIs work under the hood
- Why conversation history is needed (LLMs have no memory by default)
- How to structure a Python project professionally with venv and .env
- Git basics — version controlling a real project

## 🗺️ What's next
- Adding PDF support (not just .txt files)
- Implementing vector embeddings for smarter retrieval
- Building a full RAG pipeline
- Wrapping it in a FastAPI backend

---
*Part of my AI/ML internship preparation roadmap — building real projects from scratch.*

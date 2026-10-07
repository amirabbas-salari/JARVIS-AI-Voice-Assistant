# JARVIS — AI Voice Assistant

A lightweight, extensible AI voice assistant inspired by **JARVIS from Iron Man**.

This project is currently an early-stage prototype focused on building the core voice-to-AI pipeline using local speech recognition, n8n, OpenRouter, and NVIDIA's Nemotron model.

---

## 🚀 Current Architecture

```text
Microphone
    │
    ▼
Silero VAD
    │
    ▼
Faster-Whisper
    │
    ▼
Python Voice Service
    │
    ▼
n8n Webhook
    │
    ▼
n8n AI Agent
    │
    ├── NVIDIA Nemotron 3 Super
    │       │
    │       └── OpenRouter
    │
    ├── Tools
    │
    └── Memory
    │
    ▼
AI Response
    │
    ▼
Text-to-Speech
    │
    ▼
Speaker
```

---

## ✨ Current Features

- 🎤 Voice input through microphone
- 🗣️ Speech detection using **Silero VAD**
- 📝 Speech-to-text using **Faster-Whisper**
- 🇮🇷 Persian speech recognition
- 🧠 AI Agent powered by **n8n**
- 🤖 NVIDIA **Nemotron 3 Super** through OpenRouter
- 🔧 AI Agent Tool Calling
- 🧠 Conversation Memory
- 🔊 Text-to-Speech response
- 🐍 Python-based local voice service
- 🔄 Communication between Python and n8n through Webhooks

---

## 🧩 Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Speech Detection | Silero VAD |
| Speech Recognition | Faster-Whisper |
| AI Orchestration | n8n |
| AI Agent | n8n AI Agent |
| LLM Provider | OpenRouter |
| AI Model | NVIDIA Nemotron 3 Super |
| Voice Output | Text-to-Speech |
| Communication | HTTP / Webhook |
| Environment | Windows / Python Virtual Environment |

---

## 📁 Project Structure

```text
JARVIS/
│
├── main.py
├── n8n_client.py
├── requirements.txt
│
├── ai/
│   └── ...
│
├── audio/
│   └── ...
│
├── stt/
│   └── ...
│
├── tts/
│   └── ...
│
├── .env
├── .gitignore
└── README.md
```

> The exact directory structure may evolve as the project grows.

---

## ⚙️ How It Works

### 1. Voice Input

The user speaks through the microphone.

Silero VAD detects when speech starts and ends.

```text
Microphone
    ↓
Silero VAD
    ↓
Speech detected
```

### 2. Speech-to-Text

The recorded audio is processed by Faster-Whisper.

Example:

```text
User:
"خودت رو معرفی کن"

        ↓

Whisper:

"خودت رو معرفی کن"
```

### 3. Sending the Request to n8n

The Python service sends the recognized text to the n8n Webhook:

```json
{
  "text": "خودت رو معرفی کن"
}
```

### 4. AI Agent

n8n receives the message and passes it to the AI Agent.

The Agent uses:

- NVIDIA Nemotron 3 Super
- OpenRouter
- Tools
- Conversation Memory

The Agent can decide when a tool should be used.

### 5. Response

The AI response is returned to Python.

Python then sends the response to the Text-to-Speech system.

```text
AI Response
    ↓
TTS
    ↓
Speaker
```

---

## 🧠 AI Model

The current LLM is:

**NVIDIA Nemotron 3 Super**

The model is accessed through:

**OpenRouter**

This architecture allows the LLM provider/model to be changed later without redesigning the entire voice service.

---

## 🔧 n8n

n8n is used as the orchestration and AI-agent layer.

The current workflow contains:

```text
Webhook
   ↓
AI Agent
   ├── Chat Model
   ├── Memory
   └── Tools
   ↓
Respond to Webhook
```

The Python application communicates with n8n through HTTP.

---

## 🧠 Memory

The current version uses n8n's memory functionality to maintain conversation context.

For example:

```text
User:
My name is Javid.

Jarvis:
Nice to meet you, Javid.

User:
What is my name?

Jarvis:
Your name is Javid.
```

Long-term persistent memory is planned for a future version.

---

## 🔧 Tools

The AI Agent supports tool calling.

This allows JARVIS to move beyond simply generating text and eventually perform real actions.

Planned examples include:

```text
Open applications
Search the web
Get current time
Control the operating system
Manage files
Execute useful local actions
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/JARVIS.git
cd JARVIS
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
N8N_WEBHOOK_URL=http://localhost:5678/webhook/jarvis
```

> Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Running JARVIS

Start n8n according to your local setup.

For an npx-based installation:

```powershell
npx n8n
```

Then start the Python voice service:

```powershell
python main.py
```

You should see:

```text
==================================================
        JARVIS Voice Service
==================================================

Press Enter to speak
Press Ctrl+C to exit
```

Press Enter and start speaking.

---

## 🔐 Environment Variables

The project may use environment variables for sensitive configuration.

Example:

```env
OPENROUTER_API_KEY=...
N8N_WEBHOOK_URL=...
```

These values should never be committed to GitHub.

---

## 🗺️ Roadmap

The project is intentionally being developed incrementally.

### Phase 1 — Core Voice Assistant

- [x] Microphone input
- [x] Silero VAD
- [x] Faster-Whisper STT
- [x] Python voice service
- [x] n8n Webhook
- [x] n8n AI Agent
- [x] OpenRouter
- [x] NVIDIA Nemotron
- [x] Tool Calling
- [x] Conversation Memory
- [x] Text-to-Speech

### Phase 2 — System Control

- [ ] Open applications
- [ ] Close applications
- [ ] Open websites
- [ ] File operations
- [ ] System information
- [ ] Basic Windows control

### Phase 3 — Intelligent Assistant

- [ ] Web search
- [ ] Weather
- [ ] Calendar
- [ ] Reminders
- [ ] Better task planning
- [ ] Multi-step tool execution

### Phase 4 — Persistent Memory

- [ ] Long-term memory
- [ ] User preferences
- [ ] Persistent conversation history
- [ ] Database-backed memory
- [ ] Semantic memory / vector database

### Phase 5 — JARVIS Experience

- [ ] Wake word detection
- [ ] Continuous listening
- [ ] Faster response pipeline
- [ ] Interruptible conversations
- [ ] More natural TTS
- [ ] Vision capabilities
- [ ] Screen understanding
- [ ] Computer control

---

## 🎯 Project Goal

The long-term goal is to build a modular personal AI assistant capable of:

```text
Listen
  ↓
Understand
  ↓
Reason
  ↓
Remember
  ↓
Use Tools
  ↓
Perform Actions
  ↓
Respond
```

The project is being developed incrementally, starting with a simple voice assistant and gradually evolving toward a more capable personal AI agent.

---

## 📌 Project Status

**Current status: Early Prototype / Active Development**

The core voice → AI Agent → response pipeline is functional.

The next major milestone is adding **real system-control tools**, allowing JARVIS to perform actions on the local computer instead of only responding conversationally.

---

## 📄 License

This project is currently under development.

License information will be added in a future release.
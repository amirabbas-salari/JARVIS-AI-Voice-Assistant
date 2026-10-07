# 🤖 JARVIS — AI Voice Assistant

A local, voice-controlled AI assistant inspired by **JARVIS from Iron Man**.

JARVIS combines **Speech-to-Text, Large Language Models, n8n AI Agents, Memory, Tool Calling, Text-to-Speech, and Computer Control** to create a modular personal AI assistant.

The project is currently in an early development stage and is designed to be gradually extended with more tools and capabilities.

---

## ✨ Current Features

- 🎤 Voice input
- 🗣️ Speech-to-Text using **Faster-Whisper**
- 🧠 Local Voice Activity Detection using **Silero VAD**
- 🤖 LLM-powered conversations
- 🧩 n8n AI Agent
- 🚀 NVIDIA Nemotron through **OpenRouter**
- 🧠 Conversation Memory
- 🛠️ AI Agent Tool Calling
- 🖥️ Computer interaction through n8n Computer Use
- 📁 File and folder operations
- 📝 File creation
- 🔊 Text-to-Speech
- 🇮🇷 Persian language support
- 🇬🇧 English language support
- 🐳 n8n running with Docker
- 🔌 Modular architecture

---

# 🏗️ Architecture

The current architecture is divided into two main parts:

### Voice Service

Responsible for:

- Capturing microphone audio
- Detecting speech
- Transcribing speech
- Sending user requests to n8n
- Receiving the AI response
- Converting the response to speech

### AI Automation Layer

n8n handles:

- AI Agent
- LLM communication
- Memory
- Tool calling
- Computer interaction
- External integrations

### Overall Architecture

```text
                         ┌──────────────────────┐
                         │      Microphone      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     Silero VAD       │
                         │ Speech Detection     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Faster-Whisper    │
                         │    Speech-to-Text    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Python Service    │
                         └──────────┬───────────┘
                                    │ HTTP
                                    ▼
                    ┌──────────────────────────────┐
                    │        n8n - Docker           │
                    │                              │
                    │          Webhook             │
                    │             │                │
                    │             ▼                │
                    │         AI Agent             │
                    │             │                │
                    │      ┌──────┼───────┐        │
                    │      │      │       │        │
                    │      ▼      ▼       ▼        │
                    │    LLM   Memory   Tools      │
                    │             │       │        │
                    │             │       ▼        │
                    │             │ Computer Use   │
                    │             │       │        │
                    └─────────────┼───────┼────────┘
                                  │       │
                                  ▼       ▼
                              Response  Computer
                                  │
                                  ▼
                         ┌──────────────────────┐
                         │    Text-to-Speech    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                               🔊 JARVIS
```

---

# 🧠 AI Model

The project uses **NVIDIA Nemotron** models through **OpenRouter**.

The LLM is responsible for:

- Understanding user requests
- Maintaining conversation context
- Deciding when a tool is required
- Calling the appropriate tool
- Generating the final response

The architecture is model-agnostic, so the LLM can be changed later without redesigning the entire project.

---

# 🎙️ Speech Recognition

## Faster-Whisper

Speech recognition is handled using Faster-Whisper.

Current configuration:

```text
Model: base
Device: CPU
Compute Type: int8
```

### Why Faster-Whisper?

Faster-Whisper is an optimized implementation of Whisper based on CTranslate2.

It provides:

- Good transcription quality
- Lower resource usage
- CPU inference support
- Multiple language support
- Good performance for local applications

---

# 🎤 Voice Activity Detection

The project uses **Silero VAD** to detect when the user starts and stops speaking.

This prevents the application from continuously sending microphone audio to Whisper.

Current flow:

```text
Microphone
     ↓
Silero VAD
     ↓
Speech detected
     ↓
Record audio
     ↓
Speech ends
     ↓
Whisper
```

The VAD configuration can be adjusted later to improve pause detection and prevent the assistant from cutting off sentences too early.

---

# 🔗 n8n

n8n is used as the orchestration and AI automation layer.

The current workflow contains:

```text
Webhook
   ↓
AI Agent
   ├── Chat Model
   ├── Memory
   └── Tools
   ↓
Response
```

Using n8n makes it possible to add new capabilities without rewriting the core Python voice service.

---

# 🧠 Memory

JARVIS currently uses n8n Memory to maintain conversational context.

For example:

```text
User:
My name is Javid.

JARVIS:
Nice to meet you, Javid.

User:
What is my name?

JARVIS:
Your name is Javid.
```

### Current Memory

The current implementation provides **conversation memory**.

Long-term persistent memory is planned for a future version.

---

# 🖥️ Computer Use

One of the main capabilities of the current version is computer interaction through n8n's Computer Use / Local Gateway architecture.

JARVIS can interact with the local computer through tools provided by the automation layer.

Examples include:

```text
Open a folder
Create a file
Read files
Write files
Interact with the local filesystem
```

The Computer Use layer is intentionally separated from the Python voice service.

This allows the AI Agent to decide what action should be performed while the local computer gateway handles the actual operation.

---

# 🔊 Text-to-Speech

The final response generated by the AI Agent is sent back to the Python voice service and converted to speech.

Current flow:

```text
User Speech
     ↓
Whisper
     ↓
n8n
     ↓
AI Agent
     ↓
Response
     ↓
TTS
     ↓
JARVIS Voice
```

The TTS layer is separated from the AI logic so it can be replaced or upgraded later.

---

# 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Speech-to-Text | Faster-Whisper |
| Voice Activity Detection | Silero VAD |
| LLM | NVIDIA Nemotron |
| LLM Gateway | OpenRouter |
| AI Orchestration | n8n |
| Workflow Runtime | Docker |
| Memory | n8n Memory |
| Computer Control | n8n Computer Use |
| API Communication | HTTP / Webhook |
| Text-to-Speech | Local TTS |
| Platform | Windows |

---

# 📁 Project Structure

A simplified project structure:

```text
JARVIS/
│
├── main.py
├── n8n_client.py
│
├── audio/
│   ├── ...
│
├── ai/
│   ├── ...
│
├── config/
│   └── ...
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> The exact structure may change as the project evolves.

---

# ⚙️ Requirements

Before running the project, install:

- Python 3.10+
- Docker Desktop
- Node.js / npm
- Working microphone
- Working audio output
- OpenRouter API key

A GPU is **not required** for the current speech recognition configuration.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/JARVIS.git
cd JARVIS
```

---

## 2. Create Python virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\activate
```

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

# 🐳 Run n8n

Start n8n using Docker:

```powershell
docker run -d `
  --name n8n `
  -p 5678:5678 `
  -v n8n_data:/home/node/.n8n `
  n8nio/n8n:latest
```

n8n should then be available at:

```text
http://localhost:5678
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

> Never commit your `.env` file to GitHub.

The actual API key must remain private.

---

# 🔧 n8n Configuration

Create the required workflow in n8n.

The basic workflow is:

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

The AI Agent receives the user's message from the Webhook.

Example input:

```json
{
  "text": "What time is it?"
}
```

The User Prompt should use an n8n Expression:

```javascript
{{ $json.body.text }}
```

This allows every voice request to be dynamically passed to the AI Agent.

---

# ▶️ Running JARVIS

Start the Python voice service:

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

Example:

```text
You:
What is 12 plus 25?

JARVIS:
37
```

Or:

```text
You:
My name is Javid.

JARVIS:
Nice to meet you, Javid.
```

Or a computer-related request:

```text
You:
Create a new file in my folder.
```

The AI Agent can decide to use the appropriate computer/file tool.

---

# 🔄 Request Lifecycle

A typical request follows this pipeline:

```text
1. User speaks
       ↓
2. Microphone captures audio
       ↓
3. Silero VAD detects speech
       ↓
4. Faster-Whisper transcribes audio
       ↓
5. Python sends text to n8n
       ↓
6. n8n Webhook receives request
       ↓
7. AI Agent processes request
       ↓
8. LLM decides whether a tool is required
       ↓
9. Tool executes the requested action
       ↓
10. AI generates final response
       ↓
11. n8n returns response
       ↓
12. Python receives response
       ↓
13. TTS generates speech
       ↓
14. JARVIS speaks
```

---

# 🔒 Security

This project interacts with the local computer, so security is important.

Never expose the local n8n instance or Computer Use Gateway directly to the public internet without proper authentication and access control.

Important rules:

- Keep API keys in `.env`
- Do not commit secrets
- Do not expose n8n unnecessarily
- Limit Computer Use permissions
- Keep Shell execution disabled unless required
- Review tools before giving them to the AI Agent

---

# 🚧 Current Limitations

The current version is intentionally an early prototype.

Current limitations include:

- No wake word yet
- Session management is not fully implemented
- Long-term persistent memory is not implemented
- Limited computer tools
- No autonomous background tasks
- No vision system
- No multi-agent architecture
- Voice interruption handling can still be improved
- Tool permissions require further refinement

---

# 🗺️ Roadmap

## Phase 1 — Core Assistant ✅

- [x] Voice input
- [x] Speech-to-Text
- [x] LLM integration
- [x] n8n AI Agent
- [x] OpenRouter
- [x] NVIDIA Nemotron
- [x] Conversation Memory
- [x] Tool Calling
- [x] Text-to-Speech

## Phase 2 — Computer Control 🚧

- [x] Local filesystem interaction
- [x] File creation
- [x] Folder interaction
- [x] Computer Use
- [ ] Application launching
- [ ] Browser automation
- [ ] Keyboard automation
- [ ] Mouse automation
- [ ] Screenshot understanding

## Phase 3 — Smarter JARVIS

- [ ] Session management
- [ ] Long-term memory
- [ ] User preferences
- [ ] Personal knowledge base
- [ ] Web search
- [ ] Weather
- [ ] Calendar
- [ ] Email
- [ ] Notifications

## Phase 4 — Voice Experience

- [ ] Wake word
- [ ] Continuous listening
- [ ] Interrupt JARVIS while speaking
- [ ] Better VAD
- [ ] Faster response time
- [ ] Natural conversational pauses

## Phase 5 — Vision

- [ ] Screenshot analysis
- [ ] Camera input
- [ ] Object detection
- [ ] Face recognition
- [ ] OCR
- [ ] Screen understanding

## Phase 6 — Advanced JARVIS

- [ ] Autonomous task execution
- [ ] Multi-step planning
- [ ] Multi-agent architecture
- [ ] Personal knowledge graph
- [ ] Proactive notifications
- [ ] Smart home integration
- [ ] IoT integration
- [ ] Advanced computer control

---

# 🎯 Project Goal

The ultimate goal of this project is to build a modular personal AI assistant inspired by **JARVIS from Iron Man**.

The assistant should eventually be able to:

```text
Listen
   ↓
Understand
   ↓
Think
   ↓
Remember
   ↓
Use Tools
   ↓
Control Computer
   ↓
Search the Web
   ↓
See and Understand the Environment
   ↓
Execute Multi-step Tasks
   ↓
Respond Naturally
```

The project is intentionally being developed incrementally so that every component can be tested and improved independently.

---

# 📌 Development Philosophy

JARVIS is designed around three principles:

### 1. Modular

Each major capability should be replaceable without rewriting the entire system.

### 2. Local-first

Voice processing and computer interaction should remain local whenever practical.

### 3. Tool-driven AI

The LLM should not directly perform system operations.

Instead:

```text
LLM
 ↓
Decision
 ↓
Tool
 ↓
Action
```

This makes the system easier to control, debug, and secure.

---

# 📄 License

This project is currently under development.

License information will be added in a future release.

---

## ⭐ Status

**Early Development / Prototype**

The core voice assistant, LLM integration, memory, tool calling, and local computer interaction are currently working.

More capabilities will be added incrementally.

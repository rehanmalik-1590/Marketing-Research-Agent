# Marketing-Research-Agent
# 📊 Marketing Research Agent

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🧠 Overview

**Marketing Research Agent** ek AI-powered chatbot/agent framework hai jo *market trends, consumer behavior, competitive analysis* aur *marketing strategies* par deep insights provide karta hai.  
Iska maksad hai marketing professionals, startup founders, aur digital marketers ko rapid, data-driven guidance dena.

Ye system banaya gaya hai using:

- **CrewAI** (Agents, Tasks, Crew orchestration)  
- **LangChain + Groq LLM** (GPT-like model backend)  
- **Streamlit** for chat-based UI  

---

## 🚀 Key Features & Benefits

| Feature | Description | Benefit |
|--------|-------------|---------|
| **Specialized Agent Role** | “Marketing Research Agent” with a defined goal & backstory | Ensures responses stay focused on marketing topics |
| **Modular Task System** | Each user query becomes a `Task` handled by agents via `Crew` | Scalable — can add more agents (data collector, summarizer, etc.) later |
| **Powerful LLM backend** | Uses **Groq’s LLaMA3 model** via `langchain_groq` | High-quality, fluent responses with deep knowledge |
| **Interactive Web UI** | Chat interface powered by **Streamlit** | Easy for users to ask questions and see results in real time |
| **Session History** | Maintains conversation state across user interactions | Better UX, context-aware responses |

---

## 🧩 Architecture & How It Works

1. **User sends a marketing question** via Streamlit UI  
2. The question is passed to `process_question_with_agent(...)`  
3. A **Task** object is created, describing the research task  
4. A **Crew** is instantiated (with 1 or more agents)  
5. `crew.kickoff()` triggers the agents to act:  
   - The **Marketing Research Agent** uses the LLM backend (Groq / LLaMA3)  
   - Generates a detailed, well-researched answer  
6. Response is returned and displayed in the chat UI  
7. Chat history is stored in `st.session_state.messages` so conversation persists  

Here’s a simplified flow:

User ➜ Streamlit UI ➜ process_question_with_agent ➜ Task ➜ Crew ➜ Agent uses LLM ➜ Response ➜ UI

markdown
Copy code

---

## 🛠️ Dependencies & Setup

### Requirements

- Python 3.10 or newer  
- `crewai`  
- `langchain_groq`  
- `streamlit`  
- Other dependencies as per `requirements.txt`

### Setup Instructions

1. Clone this repository  
   ```bash
   git clone https://github.com/MRizwanMalik/Marketing-Research-Agent.git
   cd Marketing-Research-Agent
Create a virtual environment and activate it

```bash
Copy code
python -m venv venv
source venv/bin/activate     # on Linux / macOS
venv\Scripts\activate        # on Windows
Install dependencies

```bash
Copy code
pip install -r requirements.txt
Configure your Groq API key (set in env var or code)
e.g.

```bash
Copy code
export GROQ_API_KEY="your_api_key_here"
Run the Streamlit app

```bash
Copy code
streamlit run app.py
###📚 Usage & Examples
Once the app is running, you can open your browser to see the chat interface. Sample questions you can ask:

“What are the emerging trends in digital marketing in 2025?”

“Compare consumer behavior in USA vs Europe for e-commerce.”

“What marketing strategies work best for B2B SaaS startups?”

Each query will be processed and you'll get a structured, insightful answer backed by the AI model.


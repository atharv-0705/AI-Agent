# 🚀 Understanding Use of Agents

A hands-on repository documenting my journey of learning **LangChain**, **LLMs**, **Runnables**, **Tool Calling**, and **AI Agents** using Python. This repository contains practical examples that build the foundation for creating intelligent AI applications and autonomous agents.

---

## 📖 About

This repository is a collection of beginner-to-intermediate examples exploring the core concepts of LangChain. Each script focuses on a specific feature, helping understand how modern LLM-powered applications are built.

Topics covered include:

- 🔗 LangChain Runnables
- ⚡ Runnable Sequences
- 🔀 Parallel Runnables
- 🛠️ Tool Calling
- 🤖 AI Agents
- 📰 News Summarization
- 🌦️ External API Integration
- 💬 Chat Models (Mistral AI)

---

## 📂 Project Structure

```text
.
├── Agents.py                  # AI Agent examples using LangChain
├── newssummarizer.py          # News summarization using LLM
├── owntool.py                 # Creating and using custom tools
├── parallelrunnable.py        # Parallel Runnable examples
├── runnablepassthrough.py     # RunnablePassthrough examples
├── sequencerrunnable.py       # RunnableSequence examples
├── toolcalling.py             # Tool Calling with LangChain
├── requirements.txt
└── .gitignore
```

---

## 📚 Concepts Covered

### 🔹 RunnableSequence

- Prompt Templates
- Chaining components
- Output Parsers
- LLM invocation

---

### 🔹 RunnableParallel

- Running multiple chains simultaneously
- Parallel execution
- Combining outputs

---

### 🔹 RunnablePassthrough

- Passing original inputs
- Combining transformed and original data

---

### 🔹 Tool Calling

- Creating custom tools
- `@tool` decorator
- Binding tools to LLMs
- Executing tool calls

---

### 🔹 AI Agents

- Agent creation
- Multi-tool support
- Weather Tool
- News Tool
- Middleware
- Human approval before tool execution

---

### 🔹 External APIs

- OpenWeatherMap API
- Tavily Search API

---

## 🛠️ Tech Stack

- Python
- LangChain
- Mistral AI
- Tavily API
- OpenWeatherMap API
- Requests
- python-dotenv
- Rich

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/atharv-0705/Understanding-Use-of-Agents.git
```

Navigate into the project

```bash
cd Understanding-Use-of-Agents
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key
OPENWEATHER_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

## ▶️ Running Examples

Runnable Sequence

```bash
python sequencerrunnable.py
```

Parallel Runnable

```bash
python parallelrunnable.py
```

Runnable Passthrough

```bash
python runnablepassthrough.py
```

Tool Calling

```bash
python toolcalling.py
```

Agent

```bash
python Agents.py
```

---

## 🎯 Learning Outcomes

Through this repository I learned:

- LangChain architecture
- Prompt engineering basics
- Runnable interfaces
- Custom tool development
- Tool Calling
- Agent workflows
- Middleware usage
- External API integration
- Building AI-powered assistants

---

## 🚀 Future Improvements

- LangGraph examples
- Memory integration
- RAG implementation
- Multi-Agent Systems
- Streamlit UI
- MCP Integration
- Vector Databases
- AI Workflows
- Deployment examples

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is intended for learning and educational purposes.

---

## 👨‍💻 Author

**Atharv Gupta**

- GitHub: https://github.com/atharv-0705
- LinkedIn: www.linkedin.com/in/atharv-gupta-995339263

---

⭐ If you found this repository useful, consider giving it a **Star**!

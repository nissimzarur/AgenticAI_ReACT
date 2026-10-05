# ReACT Agent

An interactive ReACT (Reasoning + Acting) agent built with LangGraph and Ollama, running a local Qwen LLM with tool calling support.

## Architecture

```
START → [Reasoning] → (tool needed?) → [Acting] → [Reasoning] → ... → END
```

- **Reasoning** — LLM decides whether to call a tool or respond directly
- **Acting** — Executes the selected tool and returns the result
- **Memory** — Conversation history is preserved across turns via MemorySaver

## Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com) installed and running
- Qwen model pulled locally

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/nissimzarur/AgenticAI_ReACT.git
   cd AgenticAI_ReACT
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or with [uv](https://docs.astral.sh/uv/):
   ```bash
   uv sync
   ```

3. **Pull the Ollama model**
   ```bash
   ollama pull qwen3:8b
   ```

4. **Start Ollama** (if not already running)
   ```bash
   ollama serve
   ```

5. **Run the agent**
   ```bash
   python main.py
   ```

## Project Structure

```
├── main.py                      # Entry point
├── src/
│   ├── react.py                 # ReACT graph definition and chat loop
│   ├── state.py                 # Graph state schema
│   ├── ui.py                    # Terminal UI styling
│   └── tools/
│       └── code_translator.py   # Custom tools for the agent
├── requirements.txt
└── pyproject.toml
```

## Adding Custom Tools

Create a new function with the `@tool` decorator in `src/tools/` and register it in `src/react.py`:

```python
from langchain_core.tools import tool

@tool
def my_tool():
    """Description of what this tool does"""
    return "result"
```

Then add it to the `tools` list in `src/react.py`.

## Usage

Type your messages at the `root@react>` prompt. The agent will reason about your input, call tools when needed, and respond.

Type `quit`, `exit`, or `q` to end the session.

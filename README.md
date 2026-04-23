# IA Agent Tutorial

A beginner-friendly AI research agent built with LangChain and Claude, designed to answer research queries and return structured, parsed responses.

## Objective

Demonstrate how to build a LangChain agent that:
- Takes a natural language research question
- Uses Claude as the underlying LLM
- Returns a structured JSON response with topic, summary, sources, and tools used

## Requirements

- Python 3.8+
- An Anthropic API key

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root with your API key:

```
ANTHROPIC_API_KEY=your_api_key_here
```

## How to Use

```bash
python main.py
```

The agent will run a hardcoded research query and print the structured response to the console. To change the query, edit line 35 of `main.py`:

```python
raw_response = agent_executor.invoke({"query": "Your question here"})
```

## Architecture

```
main.py
├── ResearchResponse       Pydantic model defining the output schema
├── ChatAnthropic (LLM)    Claude Haiku via langchain-anthropic
├── ChatPromptTemplate     System + human prompt with format instructions
├── PydanticOutputParser   Parses raw LLM output into a structured object
├── create_tool_calling_agent  LangChain agent wired to the LLM and prompt
└── AgentExecutor          Runs the agent and returns the final response

tools.py
└── DuckDuckGoSearchRun    Web search tool (ready to plug into the agent)
```

## Project Structure

```
IA agent Tutorial/
├── main.py           Agent definition and entry point
├── tools.py          Tool definitions (web search)
├── requirements.txt  Python dependencies
└── .env              API keys (not committed)
```

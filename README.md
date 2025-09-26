# LangGraph Project Boilerplate

A comprehensive boilerplate generator for creating LangGraph applications with FastAPI integration, Docker support, and a well-organized project structure.

## 🚀 Quick Start

1. **Navigate to your project directory**:
   ```bash
   cd your-project-directory
   ```

2. **Run the setup script**:
   ```bash
   python setup_langgraph.py
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the application**:
   ```bash
   uvicorn server:app --reload
   ```

## 📁 Project Structure

```
your-project/
├── src/                     # Core application modules
│   ├── __init__.py
│   ├── agent.py            # LangGraph agent implementation
│   ├── tools.py            # Custom tools for your graph
│   ├── nodes.py            # Node functions for graph execution
│   ├── schemas.py          # State definitions and data models
│   ├── config.yaml         # Application configuration
│   └── utils.py            # Utility functions and config loader
├── server.py               # FastAPI web server
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── langgraph.json         # LangGraph configuration
└── Dockerfile             # Docker configuration
```

## 🔧 Configuration

### Environment Variables (.env)

```bash
# API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

# Optional: LangSmith tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=your_project_name
```

### Application Configuration (src/config.yaml)

The boilerplate includes a YAML configuration file for managing application settings:

```yaml
models:
  default: gpt-4
  fallback: gpt-3.5-turbo

endpoints:
  base_url: https://api.example.com
  timeout: 30

logging:
  level: INFO
  file: logs/app.log
```

## 🏗️ Core Components

### 1. Agent (`src/agent.py`)
The main LangGraph agent implementation. Customize this file to define your graph structure and logic.

```python
from langgraph import StateGraph
from .schemas import State
from .nodes import your_node_function

def create_agent():
    """Create and return your LangGraph agent"""
    workflow = StateGraph(State)
    workflow.add_node("node_name", your_node_function)
    # Add more nodes and edges
    return workflow.compile()
```

### 2. State Management (`src/schemas.py`)
Define your application's state structure and data models.

```python
from typing import Annotated, TypedDict
from langgraph.graph import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]
    # Add your custom state fields
```

### 3. Tools (`src/tools.py`)
Implement custom tools that your agent can use.

```python
from langchain.tools import tool

@tool
def your_custom_tool(query: str) -> str:
    """Your tool description"""
    # Implementation here
    return result
```

### 4. Nodes (`src/nodes.py`)
Define the node functions that make up your graph.

```python
def your_node_function(state: State):
    """Process state and return updates"""
    # Node logic here
    return {"field": "updated_value"}
```

## 🌐 API Endpoints

The FastAPI server provides the following endpoints:

- `GET /` - Health check
- `POST /api/query` - Process queries through your LangGraph agent
- `GET /api/health` - Detailed health status

### Example API Usage

```bash
# Test the API
curl -X POST "http://localhost:8000/api/query" \
     -H "Content-Type: application/json" \
     -d '{"query": "Hello, world!", "context": {"user_id": "123"}}'
```

## 🐳 Docker Support

### Build and Run with Docker

```bash
# Build the image
docker build -t your-langgraph-app .

# Run the container
docker run -p 8000:8080 --env-file .env your-langgraph-app
```

### Docker Compose (Optional)

Create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8000:8080"
    env_file:
      - .env
    volumes:
      - ./logs:/code/logs
```

Run with: `docker-compose up`

## 📦 Dependencies

The boilerplate includes all essential LangGraph and LangChain dependencies:

- **LangGraph**: Core graph framework and SDK
- **LangChain**: Community tools and integrations
- **FastAPI**: Web framework for the API server
- **Anthropic/OpenAI**: LLM integrations
- **Tavily**: Search tool integration
- **LangSmith**: Observability and debugging

## 🔄 Development Workflow

1. **Customize your agent** in `src/agent.py`
2. **Define your state** in `src/schemas.py`
3. **Implement tools** in `src/tools.py`
4. **Create node functions** in `src/nodes.py`
5. **Update configuration** in `src/config.yaml`
6. **Test via API** using the FastAPI endpoints
7. **Deploy** using Docker

## 🚀 LangGraph Studio Integration

The boilerplate is configured for LangGraph Studio with `langgraph.json`:

```bash
# Start LangGraph Studio
langgraph dev
```

This will launch the interactive development environment where you can:
- Visualize your graph structure
- Debug execution flows
- Test different inputs
- Monitor performance

## 🛠️ Customization Tips

### Adding New Tools

1. Define the tool in `src/tools.py`
2. Import and use in your nodes (`src/nodes.py`)
3. Register with your agent in `src/agent.py`

### Environment-Specific Configuration

Use the configuration loader in `src/utils.py`:

```python
from src.utils import load_yaml_config

config = load_yaml_config("src/config.yaml")
model_name = config["models"]["default"]
```

### Error Handling

The FastAPI server includes basic error handling. Extend it in `server.py` for your specific needs.

## 📚 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)

## 🤝 Contributing

This boilerplate is designed to be a starting point. Feel free to customize it for your specific use case and contribute improvements back to the community.

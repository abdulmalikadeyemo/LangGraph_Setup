#!/usr/bin/env python3
import os
import pathlib

def create_directory_structure():
    """
    Creates the LangGraph project directory structure in the current directory.
    """
    print("Creating LangGraph project structure in current directory...")
    
    # Define the structure with files and their content
    structure = {
        "src": {
            "__init__.py": "",
            "agent.py": "# Code for constructing your graph\n\ndef create_agent():\n    \"\"\"Create and return your LangGraph agent\"\"\"\n    pass\n",
            "tools.py": "# Tools for your graph\n\n# Define your tools here\n",
            "nodes.py": "# Node functions for your graph\n\n# Define your node functions here\n",
            "schemas.py": "# State definition of your graph\n\nclass State:\n    \"\"\"Define your state class here\"\"\"\n    pass\n",
            "config.yaml": "# Configuration for your LangGraph application\n\nmodels:\n  default: gpt-4\n  fallback: gpt-3.5-turbo\n\nendpoints:\n  base_url: https://api.example.com\n  timeout: 30\n\nlogging:\n  level: INFO\n  file: logs/app.log\n",
            "utils.py": """# config.py
import os
import yaml

def load_yaml_config(yaml_path: str = "config.yaml") -> dict:
    \"\"\"
    Load the unified YAML configuration from the specified path.
    \"\"\"
    if not os.path.exists(yaml_path):
        raise FileNotFoundError(f"Config file not found at {yaml_path}")
    with open(yaml_path, "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)
    return config_data
"""
        },
        "server.py": """from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Dict, Any, Optional
import os
import yaml
import logging

app = FastAPI(title="LangGraph API")

class QueryInput(BaseModel):
    query: str
    context: Optional[Dict[str, Any]] = None

@app.get("/")
async def root():
    return {"message": "LangGraph API is running"}

@app.post("/api/query")
async def process_query(input_data: QueryInput):
    try:
        # Here you would integrate with your LangGraph agent
        # Example: response = your_agent(input_data.query, input_data.context)
        
        # For now, return a placeholder response
        return {
            "status": "success",
            "response": f"Processed query: {input_data.query}"
        }
    except Exception as e:
        logging.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True)
""",
        "requirements.txt": "langgraph\nlangchain_community\nlanggraph-sdk\nlanggraph-checkpoint\nlangchain-core\nlangsmith\nlangchain_anthropic\ntavily-python\nlangchain_openai\nfastapi\nuvicorn\npydantic\npython-dotenv\nyaml\n",
        ".env": "# Environment variables\n# API keys and other sensitive information\n# OPENAI_API_KEY=your_api_key_here\n# ANTHROPIC_API_KEY=your_api_key_here\n",
        "langgraph.json": "{\n    \"graphs\": {\n        \"agent_v1\": \"./src/agent.py:graph_name\"\n    },\n    \"env\": \".env\",\n    \"python_version\": \"3.11\",\n    \"dependencies\": [\n        \".\"\n    ]\n}",
        "Dockerfile": "FROM python:3.12-slim\n\nWORKDIR /code\n\n# Copy requirements file first for better caching\nCOPY ./requirements.txt .\n\n# Install dependencies\nRUN pip install --no-cache-dir -r requirements.txt\n\n# Copy application code\nCOPY ./src ./src\nCOPY ./server.py ./server.py\n\n# If you have additional packages directory, uncomment the next line\n# COPY ./packages ./packages\n\nEXPOSE 8080\n\n# Run the application\nCMD exec uvicorn server:app --host 0.0.0.0 --port 8080\n"
        }
    # }
    
    # Create the directories and files
    for dir_name, contents in structure.items():
        create_recursive(dir_name, contents)
    
    print("Project structure created successfully!")
    print("Run 'pip install -r requirements.txt' to install dependencies.")

def create_recursive(path, contents):
    """
    Recursively creates directories and files.
    
    Args:
        path: Current path to create
        contents: Dictionary of contents or string for file content
    """
    if isinstance(contents, dict):
        # It's a directory, create it if it doesn't exist
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        
        # Create its contents
        for name, content in contents.items():
            create_recursive(os.path.join(path, name), content)
    else:
        # It's a file, write the content
        with open(path, 'w') as f:
            f.write(contents)

if __name__ == "__main__":
    # Create the directory structure in current directory
    create_directory_structure()
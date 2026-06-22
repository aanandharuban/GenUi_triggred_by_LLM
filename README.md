FastMCP Generative UI (Gen UI) Server
A Python-based Local Server utilizing the FastMCP framework to implement the Generative UI pattern. In this architecture, the Large Language Model (LLM) dynamically generates data payloads and layout parameters at runtime, passing them to the server to instantly render interactive, custom-built interfaces.

Features
LLM-Driven Interfaces: The AI acts as the application state manager, supplying raw data directly to the visualization tools.

Dynamic Rendering: Instantly compiles charts, data tables, and metrics based on the LLM's real-time analytical output.

Zero-Setup Frontend: Leverages FastMCP and Prefab UI to translate backend data structures into rich, sandboxed web components automatically.

Prerequisites
Python 3.10 or higher

Installation
python -m venv venv

.\venv\Scripts\activate

pip install "fastmcp[apps]" prefab-ui

Execution
fastmcp dev apps server.py

How the Generative Pipeline Works
The Prompt: The user asks the LLM to analyze a scenario or generate data.

The Tool Call: The LLM structures the generated data and passes it as arguments to the registered FastMCP tool.

The Compilation: The Python server receives the LLM's data, maps it to Prefab UI components and compiles a PrefabApp.

The Render: The host application renders the fully interactive UI directly inside the chat interface based on the LLM's exact specifications.

Troubleshooting
If the browser hangs on "Waiting for Content":
Perform a hard refresh (Ctrl + F5) to clear the local iframe cache.

If port 8000 is blocked by a background process, use alternate ports:
fastmcp dev apps server.py --mcp-port 8001 --dev-port 8081

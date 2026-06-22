# FastMCP Generative UI (Gen UI) Server

A Python-based local server built using the **FastMCP** framework to implement the **Generative UI (Gen UI)** pattern.

In this architecture, a **Large Language Model (LLM)** dynamically generates data payloads and UI layout parameters at runtime. These are passed to the FastMCP server, which instantly renders interactive, custom-built interfaces using Prefab UI components.

---

## 🚀 Features

### LLM-Driven Interfaces
The LLM acts as the application state manager, supplying structured data directly to visualization components.

### Dynamic Rendering
Automatically generates and renders:

- Charts
- Data Tables
- Metrics Cards
- Interactive Dashboards

based on the LLM's real-time analytical output.

### Zero-Setup Frontend
Uses **FastMCP Apps** and **Prefab UI** to convert backend-generated data structures into rich, sandboxed web components without requiring a separate frontend framework.

---

## 📋 Prerequisites

Before getting started, ensure the following is installed:

- Python 3.10 or higher

Verify installation:

```bash
python --version
```

---

## 📦 Installation

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**Windows**

```bash
.\venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install "fastmcp[apps]" prefab-ui
```

---

## ▶️ Running the Server

Start the FastMCP development server:

```bash
fastmcp dev apps server.py
```

Once running, FastMCP will launch the development environment and make the application available for rendering within supported MCP hosts.

---

## 🏗️ How the Generative UI Pipeline Works

### 1. User Prompt

The user asks the LLM to:

- Analyze a dataset
- Generate metrics
- Create charts
- Build a dashboard
- Visualize structured information

### 2. Tool Invocation

The LLM structures its generated output into a schema and sends it as arguments to a registered FastMCP tool.

### 3. UI Compilation

The FastMCP server:

- Receives the generated data
- Maps it to Prefab UI components
- Builds a `PrefabApp` dynamically

### 4. Rendering

The host application renders the compiled UI directly inside the chat interface, producing an interactive experience driven entirely by the LLM's output.

---

## 📁 Example Flow

```text
User Prompt
      │
      ▼
Large Language Model (LLM)
      │
      ▼
FastMCP Tool Call
      │
      ▼
Python Server
      │
      ▼
Prefab UI Components
      │
      ▼
Rendered Interactive Interface
```

---

## 🛠️ Troubleshooting

### Browser Stuck on "Waiting for Content"

If the application remains on:

```text
Waiting for Content
```

perform a hard refresh:

```text
Ctrl + F5
```

This clears the local iframe cache and reloads the generated application.

---

### Port 8000 Already in Use

If another process is occupying the default FastMCP ports, launch using custom ports:

```bash
fastmcp dev apps server.py --mcp-port 8001 --dev-port 8081
```

---

## 📚 Tech Stack

- Python
- FastMCP
- FastMCP Apps
- Prefab UI
- Generative UI Architecture
- Large Language Models (LLMs)

---

## 🎯 Use Cases

- AI-generated dashboards
- Data visualization assistants
- Interactive analytics applications
- Dynamic reporting tools
- LLM-powered business intelligence interfaces
- Real-time metric exploration

---

## License

This project is intended for educational, research, and prototyping purposes using the FastMCP ecosystem.

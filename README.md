# Arctic Workflow Proof of Concept

This repository provides a backend only demonstration of how an agent based workflow can route user input, evaluate simple intent, call external data integrations, execute multi-agent reasoning through Swarms, and synthesize a final structured reply through an ALM model. This project intentionally excludes all frontend logic, UI components, styling, and any proprietary agent personalities. Its purpose is to illustrate the architecture that supports the larger system.

---

## Purpose

The Arctic Workflow POC is designed to show the operational pipeline of an agent driven system. It demonstrates:

1. How agents are registered using simple structural definitions.
2. How system prompts and user input are combined and sent to an ALM model.
3. How external API integrations enrich agent context.
4. How Swarms multi-agent workflows extend complex task handling.
5. How the interpreter handles routing, summarization, and message reduction.
6. How backend logic can run without any UI dependencies.

This code base is not intended for production use. It serves as a structural and educational reference for research, prototyping, and documentation.

---

## Key Components

### 1. Agent Registry

The registry defines agent identifiers and placeholder system instructions. No personality content is included. This module shows how an application can organize multiple agent types in a consistent and reusable format.

---

### 2. ALM Wrapper

This module prepares the final request sent to the model. It merges:

- the agent system instructions
- short term message context
- user provided input

The wrapper then returns the text response from the model.

---

### 3. Interpreter

The interpreter connects every part of the workflow. It:

- receives raw user input
- applies simple intent checks
- creates structured summaries for model consumption
- calls external integrations
- routes complex tasks into Swarms when appropriate
- maintains short term context
- produces a final reply using the ALM wrapper

The interpreter is the backbone of the entire logic system.

---

### 4. External Integrations

#### Birdeye

Provides basic metadata for a token, such as name, symbol, logo, and website.

#### TikTok

Performs a simple keyword search to estimate whether content related to the token is present on the platform.

#### Helius WebSocket

Listens for balance changes on a specific mint address and emits structured events. This demonstrates how real time blockchain data can be integrated.

---

### 5. Swarms Multi-Agent Integration

The system includes a Python bridge to the Swarms orchestration framework. Multi-step or research-heavy queries can be routed to Swarms, which dynamically constructs a workflow using the Arctic agent definitions.

The Swarms integration provides:

- automatic detection of complex or multi-step intents
- dynamic agent construction based on the Arctic registry
- sequential or other workflow strategies
- extraction of synthesized multi-agent results
- seamless return of results back to the ALM layer

This hybrid model allows Swarms to enhance complex reasoning without replacing the existing Arctic agent structure.

---

## Demo Script

The demo.ts file demonstrates how to run the entire workflow. It shows:

- querying token metadata
- checking trending status
- triggering a Swarms multi-agent workflow
- running a general agent response through ALM

---

## Running the demo

1. Install dependencies
   npm install

2. Build TypeScript
   npm run build

3. Run
   npm start

(Optional) Test the Swarms Python integration:
npm run swarms-test

---

## Python Requirements (Swarms Integration)

The interpreter can route complex or multi-step tasks into a Python-based Swarms workflow.
To enable this, install the dependencies listed in `requirements.txt`:

```
pip install -r requirements.txt
```

If using a virtual environment:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

These Python modules are required:

- integrations/swarms/run_swarms.py
- integrations/swarms/swarmRouter.py
- integrations/swarms/swarms_agents.py
- integrations/swarms/**init**.py

Node will automatically call these modules when Swarms is needed.

---

## Required Environment Variables

A .env file should be created based on .env.example. You must provide:

CLAUDE_KEY
BIRDEYE_KEY
RAPIDAPI_TIKTOK_KEY
HELIUS_KEY

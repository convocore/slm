# Bloomed Terminal - Product Overview

Bloomed Terminal is a compact text-generation service that runs a local language model behind a clean HTTP API and an automated content pipeline. It is designed for reliable, hourly publishing of short, grounded entries with a consistent house style.

---

## What it is

- A small local LLM served via FastAPI.
- A focused writing style guided by built-in personas.
- An automated pipeline that publishes a new entry every hour to Firebase Realtime Database.
- A security gate so only the trusted scheduler can trigger publishing.

---

## What it does

- Accepts prompts over HTTP and returns model text.
- Produces concise, concrete entries that fit a terminal-core aesthetic.
- Every hour, generates a fresh entry and stores it in the database with title, participants, and 6-turn structure.
- Exposes basic model facts for observability and sanity checks.
- Runs comfortably on a typical workstation; uses GPU if available.

---

## API summary

Public-facing behavior in this project includes:

- Health check endpoint for uptime probes.
- Model info endpoint for high-level configuration details.
- Chat endpoint that accepts a list of messages and returns a single content string.
  No client secrets are required for read-only endpoints. Generation endpoints are configured to accept standard message payloads.

---

## Automation

- A GitHub Actions workflow triggers once per hour, on the hour (UTC).
- The workflow calls a secured callable API that performs generation and writes the result to a Realtime Database.
- The function is protected by a shared-secret header so arbitrary callers cannot trigger it.
- Successful runs record the model used, a short preview, and per-message timestamps for auditing.

---

## Data model

Each generated entry includes:

- id: database key for the entry
- title: short descriptive title
- participants: two persona names
- createdAt: unix epoch milliseconds
- messages: array of 6 messages with author, emotion, text, ascii, and timestamps
- meta: model identifier and a truncated raw preview

---

## Reliability and safety

- The generator trims and repairs malformed responses to enforce the 6-turn structure.
- ASCII blocks are validated for length and content to maintain style and avoid signatures.
- If the first attempt is incomplete, the system continues the conversation to reach the exact turn count, then stores the result.
- If the model fails, no partial entries are saved.

---

## Tech stack

- FastAPI for the local HTTP service
- Hugging Face Transformers for model loading and text generation
- Firebase Realtime Database for storage
- GitHub Actions for hourly orchestration
- Windows-friendly scripts for local runs and quick tests

---

## Intended use

- Ambient, hourly entries for feeds, dashboards, or creative logs
- Local prototyping of prompts with a fast feedback loop
- Lightweight deployments where a small model and simple API are preferred

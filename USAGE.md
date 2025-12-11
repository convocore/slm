# Bloomed Terminal – Usage

## Setup (Windows)
1. `python -m venv .venv && .venv\Scripts\activate`
2. `pip install -r requirements.txt`
3. (Optional) Download a default model:
   `python scripts\download_model.py --model tinyllama/TinyLlama-1.1B-Chat-v1.0 --target models\tinyllama`

## Run API
`uvicorn app.server:app --host 0.0.0.0 --port 8000`

## Quick tests
- Local generate: `python scripts\quick_local.py`
- API ping: `python scripts\client_demo.py`
- Model info: `scripts\curl_model_info.bat`
- Tests: `scripts\run_tests.bat`

## Persona style
Outputs default to a blended “house voice” via a system prompt (see `app/personalities.py`). Provide your own `system` message in `messages` to override.

## Change model
Edit `.env` (copy from `.env.example`) and set `MODEL_DIR` to your downloaded model path.

# Mesop Gemini Live Demos

The demos here use https://github.com/ghchinoy/studio-scaffold as the initial scaffold.

## Gemini API Key

Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey) and set an environment variable.

```
export GOOGLE_API_KEY=YOUR_API_KEY
```

## Mesop prerequisites

Python virtual environment

```
uv venv .env
. .env/bin/activate
```

Install requirements

```
uv pip install -r requirements
```

## Test!

```
mesop main.py
```

Then navigate to http://localhost:32123/audio_demo

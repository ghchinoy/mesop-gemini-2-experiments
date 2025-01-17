import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv(override=True)


@dataclass
class Default:
  PROJECT_ID: str = field(default_factory=lambda: os.environ.get("PROJECT_ID"))
  LOCATION: str = os.environ.get("LOCATION", "us-central1")
  MODEL_ID: str = os.environ.get("MODEL_ID", "gemini-2.0-flash-exp")

  # Defaults to Vertex AI Gemini
  INIT_VERTEX: bool = True
  HOST: str = "us-central1-aiplatform.googleapis.com"

  API_KEY: str = os.getenv("GOOGLE_API_KEY")

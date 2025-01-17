from typing import Optional
from dotenv import load_dotenv
from google import genai
from config.default import Default


load_dotenv(override=True)


class ModelSetup:

    @staticmethod
    def init(
        project_id: Optional[str] = None,
        location: Optional[str] = None,
        model_id: Optional[str] = None,
    ):
        config = Default()
        if not project_id:
            project_id = config.PROJECT_ID
        if not location:
            location = config.LOCATION
        if not model_id:
            model_id = config.MODEL_ID
        if None in [project_id, location, model_id]:
            raise ValueError("All parameters must be set.")
        
        # If API_KEY present, use MLDev Gemini
        if config.API_KEY:
            config.INIT_VERTEX = False
            config.HOST = "generativelanguage.googleapis.com"
            
        print(f"initiating genai client with {project_id} in {location}")

        if config.INIT_VERTEX:
            bidi_url = f"wss://{config.HOST}/ws/google.cloud.aiplatform.v1beta1.LlmBidiService/BidiGenerateContent"
            client = genai.Client(
                vertexai=config.INIT_VERTEX,
                project=project_id,
                location=location,
            )
        else:
            bidi_url = f"wss://{config.HOST}/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key={config.API_KEY}"
            client = genai.Client(
                vertexai=config.INIT_VERTEX,
                api_key=config.API_KEY,
            )

        return client, model_id, bidi_url

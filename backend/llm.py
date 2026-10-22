import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
_model_name = os.getenv("GEMINI_MODEL")
_embedder = None  # loaded lazily so startup stays fast


def generate(prompt: str) -> str:
    """Send text to the LLM, get text back."""
    resp = _client.models.generate_content(model=_model_name, contents=prompt)
    return resp.text


def ocr(image_bytes: bytes, mime_type: str = "image/jpeg") -> str:
    """Read text from a photo of a notice using the vision-capable LLM."""
    resp = _client.models.generate_content(
        model=_model_name,
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
            "Extract all text from this image exactly as written. Output only the text.",
        ],
    )
    return resp.text


def embed(text: str) -> list[float]:
    """Turn text into a vector using a free local model."""
    global _embedder
    if _embedder is None:
        from sentence_transformers import SentenceTransformer
        print("Loading embedding model (first time is slow)...")
        _embedder = SentenceTransformer("all-MiniLM-L6-v2")
    return _embedder.encode(text).tolist()
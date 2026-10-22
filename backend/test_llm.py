from llm import generate, embed
import os
from dotenv import load_dotenv
load_dotenv()
print("Model:", repr(os.getenv("GEMINI_MODEL")))
print("Key loaded:", bool(os.getenv("GEMINI_API_KEY")))

print(generate("Say hello in one short sentence."))
v = embed("Exam fee last date is 30 October")
print(len(v), v[:3])
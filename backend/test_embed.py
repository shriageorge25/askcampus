from llm import embed

print("Loading embedder (first time downloads a model, be patient)...")
v = embed("Exam fee last date is 30 October")
print(len(v), v[:3])
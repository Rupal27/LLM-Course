from transformers import pipeline
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

# Load Dolly v2 1B on CPU
generator = pipeline(
    "text-generation",
    model="databricks/dolly-v2-7b",
    trust_remote_code=True,
    device=-1,
    framework="pt"
)
prompt = "Suggest one popular North Indian dish to eat (just the name):"

# Slightly higher max_new_tokens and small positive temperature
response = generator(
    prompt,
    max_new_tokens=20,
    temperature=0.01
)

dish_name = response[0]["generated_text"].strip()
print("Generated dish:", dish_name)

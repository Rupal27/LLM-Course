from transformers import pipeline
import torch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
hf auth login

# Load Dolly v2 1B on CPU
generator = pipeline(
    "text-generation",
    model="databricks/dolly-v2-7b",
    trust_remote_code=True,
    device=-1,
    framework="pt"
)
prompt = "Suggest one popular American POP star to listen to:"

# Slightly higher max_new_tokens and small positive temperature
response = generator(
    prompt,
    max_new_tokens=20,
    temperature=0.001
)

dish_name = response[0]["generated_text"].strip()
print("Generated dish:", dish_name)

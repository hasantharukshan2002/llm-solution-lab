import torch
from transformers import pipeline

# -----------------------------
# Load Model
# -----------------------------
# Check if GPU is available
device = 0 if torch.cuda.is_available() else -1  # 0 for GPU, -1 for CPU
print(f"Using device: {'GPU (CUDA)' if device == 0 else 'CPU'}")

generator = pipeline(
    "text-generation",
    model="gpt2",
    device=device
)

# -----------------------------
# Tools
# -----------------------------
def weather_tool():
    return "Today's weather is sunny."

def calculator_tool(a, b):
    return a + b

def search_tool(query):
    docs = {
        "AI": "Artificial Intelligence enables machines to think.",
        "Python": "Python is widely used in AI."
    }

    return docs.get(query, "No information found.")

# -----------------------------
# Simple Agent
# -----------------------------
def agent(user_input):

    if "weather" in user_input.lower():
        return weather_tool()

    elif "add" in user_input.lower():
        return calculator_tool(5, 3)

    elif "python" in user_input.lower():
        return search_tool("Python")

    else:
        result = generator(
            user_input,
            max_length=50
        )

        return result[0]["generated_text"]

# -----------------------------
# Test Agent
# -----------------------------
print(agent("Tell me about Python"))
print(agent("What is the weather today?"))
print(agent("add numbers"))
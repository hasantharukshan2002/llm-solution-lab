from transformers import pipeline

# -----------------------------
# Load Language Model
# -----------------------------
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# -----------------------------
# Simple Document Database
# -----------------------------
documents = [
    "Python is a programming language.",
    "Transformers are used in NLP.",
    "RAG combines retrieval and generation.",
    "Machine learning enables intelligent systems."
]

# -----------------------------
# Simple Search Function
# -----------------------------
def retrieve_document(query):
    for doc in documents:
        if query.lower() in doc.lower():
            return doc

    return "No relevant document found."

# -----------------------------
# User Query
# -----------------------------
query = "Transformers"

retrieved_doc = retrieve_document(query)

# -----------------------------
# Create Prompt
# -----------------------------
prompt = f"""
Context: {retrieved_doc}

Question: Explain this concept.
Answer:
"""

# -----------------------------
# Generate Response
# -----------------------------
result = generator(
    prompt,
    max_length=100,
    num_return_sequences=1
)

print(result[0]["generated_text"])
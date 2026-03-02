from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("sample.txt", "r") as f:
    text = f.read()

messages = [
    {"role": "system", "content": f"You are a helpful assistant. Answer questions based on this text:\n\n{text}"}
]

print("Ask questions about your document. Type 'quit' to exit.\n")

while True:
    question = input("You: ")
    if question.lower() == "quit":
        break
    
    messages.append({"role": "user", "content": question})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    
    print(f"\nAI: {answer}\n")
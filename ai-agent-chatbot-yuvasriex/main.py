import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = "2023-12-01-preview"

def chat_with_agent():
    print("👋 Welcome to the AI Revision Agent! Type 'exit' to stop.
")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = openai.ChatCompletion.create(
            engine=os.getenv("AZURE_DEPLOYMENT_NAME"),
            messages=[
                {"role": "system", "content": "You are a helpful AI agent that helps students revise topics like biology using quizzes and summaries."},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response['choices'][0]['message']['content']
        print(f"AI: {reply}\n")

if __name__ == "__main__":
    chat_with_agent()

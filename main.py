import os
from sys import argv
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = argv[1:]
    if not args:
        print('Usage: uv run main.py "prompt"')
        print('       python main.py "prompt"')
        exit(1)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages)


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
    )

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()

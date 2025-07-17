import os
from sys import argv
from google import genai
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

    prompt = " ".join(args)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=prompt,
    )

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)


if __name__ == "__main__":
    main()

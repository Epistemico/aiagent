import os
from sys import argv
from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompts import system_prompt


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    verbose = "--verbose" in argv
    args = []

    for arg in argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("===== AI Agent =====")
        print('Usage: uv run main.py "prompt" [--verbose]')
        print('       python main.py "prompt" [--verbose]')
        exit(1)
   
    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    if verbose:
        print("User prompt:", user_prompt)

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config =types.GenerateContentConfig(system_instruction=system_prompt),
    )

    if verbose:
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()

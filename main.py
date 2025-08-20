import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

argv = sys.argv

div = "--------------------------------------"

def main():
    print("Hello from ai-agent!")


    if len(argv) <= 1:
        print(f"missing argument: prompt")
        print(f"argv = {argv}")
        sys.exit(1)

    prompt = argv[1]

    verbose = False
    if "--verbose" in argv:
        verbose = True
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    
    
    if verbose:
        print(f"User prompt: {prompt}")
        print(div)

    print(response.text)
    print(div)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(div)
    

if __name__ == "__main__":
    main()

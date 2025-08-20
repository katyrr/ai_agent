import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

argv = sys.argv

div = "--------------------------------------"

def main():
    print("Hello from ai-agent!")

    if len(argv) != 2:
        print(f"wrong number of arguments: {len(argv)}")
        print(f"argv = {argv}")
        sys.exit(1)

    prompt = argv[1]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)
    print(response.text)
    print(div)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    

if __name__ == "__main__":
    main()

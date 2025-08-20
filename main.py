import os
from dotenv import load_dotenv

from google import genai
client = genai.Client(api_key=api_key)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()

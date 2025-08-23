import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
import sys

from config import *
#sys.path.append("functions")
from functions.get_files_info import get_files_info, schema_get_files_info

#-------------------------------------------------------------------------

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

argv = sys.argv

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

#--------------------------------------------------------------------------

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

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[available_functions]
        ),
    )
    
    print(DIV)
    if verbose:
        print(f"User prompt: {prompt}")
        print(DIV)

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response.text)
    

    print(DIV)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(DIV)
    

if __name__ == "__main__":
    main()

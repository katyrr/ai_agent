import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
import sys

from config import *
#sys.path.append("functions")
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function

#-------------------------------------------------------------------------

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

argv = sys.argv

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_run_python_file,
        schema_get_file_content,
        schema_write_file,
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

    for a in argv[2:]:
        if not a in ALLOWED_ARGS:
            print(f"Warning: ingnoring unexpected arg '{a}'")
    
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
            result = call_function(function_call_part, verbose=True)

            try: text = result.parts[0].function_response.response
            except Exception as me:
                raise Exception(f"Error: {function_call_part} returned no result? {me}")
            
            if verbose:
                print(f"-> {text['result']}")


    else:
        print(response.text)
    

    print(DIV)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(DIV)
    

if __name__ == "__main__":
    main()

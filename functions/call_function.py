from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def call_function(function_call_part, verbose=False):
    '''
    INPUTS:
    -------
    function_call_part : types.FunctionCall
    - properties = .name (string), .args (dict)
    
    '''

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_call_part.args["working_directory"] = "./calculator"

    available_functions = {
        "get_files_info": get_files_info,
        "get_file_content" : get_file_content,
        "write_file" : write_file,
        "run_python_file" : run_python_file
    }

    if function_call_part.name in available_functions:
        result = available_functions[function_call_part.name](**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": result},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
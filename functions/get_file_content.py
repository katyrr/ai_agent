from functions.get_directory import get_directory
from google.genai import types

from config import *

def get_file_content(working_directory, file_path):
    
    full_path = get_directory(working_directory, file_path, "file")
    if full_path.startswith("Error:"):
        return full_path
    
    try:
        with open(full_path, 'r') as f:
            contents = f.read(MAX_CHARACTER_LIMIT)
            if len(contents) == MAX_CHARACTER_LIMIT:
                contents += f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as me:
        return f'Error: {me}'
    
    return contents

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the content of the requested file, specified by the relative file_path from (and constrained to) the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative file path to the desired file, relative to the working directory.",
            ),
        },
    ),
)
from functions.get_directory import get_directory
from google.genai import types

def write_file(working_directory, file_path, content):
    
    full_path = get_directory(working_directory, file_path, "file", create_ok=True)
    if full_path.startswith("Error:"):
        return full_path
    
    try:
        with open(full_path, 'w') as f:
            f.write(content)
    except Exception as me:
        return f"Error: {me}"
    else:
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file, overwriting any existing content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING, 
                description="The relative file path from the working directory to the file being overwritten. If the file doesn't exist, it will be created."
            ),
            "content": types.Schema(
                type=types.Type.STRING, 
                description="The text content which will be written to the file."
            )
        },
    ),
)
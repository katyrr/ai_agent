from functions.get_directory import get_directory
import os

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
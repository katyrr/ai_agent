from functions.get_directory import get_directory

from config import *

def get_file_content(working_directory, file_path):
    
    full_path = get_directory(working_directory, file_path, "file")
    
    try:
        with open(full_path, 'r') as f:
            contents = f.read(MAX_CHARACTER_LIMIT)
            if len(contents) == MAX_CHARACTER_LIMIT:
                contents += f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as me:
        return f'Error: {me}'
    
    return contents

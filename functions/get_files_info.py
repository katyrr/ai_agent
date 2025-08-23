import os
from google.genai import types

from functions.get_directory import get_directory


def get_files_info(working_directory, directory="."):

    full_directory = get_directory(working_directory, directory, "directory")
    if full_directory.startswith("Error:"):
        return full_directory
    
    directory_list = os.listdir(full_directory)
    result = ""

    for i in directory_list:
        path_to_i = os.path.join(full_directory, i)
        size_of_i = os.path.getsize(path_to_i)
        i_is_dir = os.path.isdir(path_to_i)
        result += (f"- {i}: file_size={size_of_i} bytes, is_dir={i_is_dir}\n")
  
    return result

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
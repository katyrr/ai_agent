import os
from functions.get_directory import get_directory

def get_files_info(working_directory, directory="."):

    full_directory = get_directory(working_directory, directory, "directory")
    directory_list = os.listdir(full_directory)
    result = ""

    for i in directory_list:
        path_to_i = os.path.join(full_directory, i)
        size_of_i = os.path.getsize(path_to_i)
        i_is_dir = os.path.isdir(path_to_i)
        result += (f"- {i}: file_size={size_of_i} bytes, is_dir={i_is_dir}\n")
  
    return result
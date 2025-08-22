import os

def get_files_info(working_directory, directory="."):

    try:
        absolute_working_directory = os.path.abspath(working_directory)
        full_directory = os.path.join(working_directory, directory)
        absolute_directory = os.path.abspath(full_directory)
    except Exception as me:
        return f'Error: {me}'

    '''print(full_directory)
    print(absolute_directory)
    print(absolute_working_directory)'''
    
    if not os.path.isdir(full_directory):
        return f'Error: "{directory}" is not a directory'
    if not absolute_directory.startswith(absolute_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    directory_list = os.listdir(full_directory)
    result = ""

    for i in directory_list:
        path_to_i = os.path.join(full_directory, i)
        size_of_i = os.path.getsize(path_to_i)
        i_is_dir = os.path.isdir(path_to_i)
        result += (f"- {i}: file_size={size_of_i} bytes, is_dir={i_is_dir}\n")
  
    return result
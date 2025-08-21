import os

def get_files_info(working_directory, directory="."):
    absolute_working_directory = os.path.abspath(working_directory)
    full_directory = os.path.join(working_directory, directory)
    absolute_directory = os.path.abspath(full_directory)
    print(full_directory)
    print(absolute_directory)
    print(absolute_working_directory)
    
    print(os.listdir(full_directory))
    if absolute_directory.startswith(absolute_working_directory):
        return f'safe'
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
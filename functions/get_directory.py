import os

def get_directory(working_directory, path, expect_type=None, create_ok=False):
    ''' 
    INPUTS
    ------
    working_directory: string
        - a relative path from the location of main.py
        - marks the root of the allowed scope
        - anything within this directory will be accessible by the AI agent

    path: string
        - a relative path from [working_directory]
        - the directory that we want to check: is it within working_directory

    require_type: string (optional)
        - either "directory" or "file"

    OUTPUTS (one of)
    ----------------
    full_path: string
        - a relative path from the location of main.py
        - provides a complete relative path to the requested directory
          by appending [path] onto the end of [working_directory]
        - returned only if [path] is within [working_directory]
    
    error: string
        - if [path] is not a valid path
        - if [path] is expected to be a file, but is not
        - if [path] is expected to be a directory, but is not
        - if [path] is not within [working_directory]
        - if any other miscellaneous error is raised

    '''
    try:
        absolute_working_directory = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, path)
        absolute_path = os.path.abspath(full_path)
    except Exception as me:
        return f'Error: {me}'

    '''print(full_path)
    print(absolute_path)
    print(absolute_working_directory)'''
    
    if not absolute_path.startswith(absolute_working_directory):
        return f'Error: Cannot execute "{path}" as it is outside the permitted working directory'
    
    
            
    if expect_type=="directory" and not os.path.isdir(full_path):
        if create_ok:
            os.makedirs(full_path, exist_ok=True)
        else:
            return f'Error: "{path}" is not a directory'
    elif expect_type=="file" and not os.path.isfile(full_path):
        if create_ok:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
        else:
            return f'Error: File "{path}" not found'
    elif expect_type is None:
        if not os.path.isdir(full_path) or not os.path.isfile(full_path):
            if create_ok:
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
            else:
                return f'Error: relative path {path} does not exist'

    
        

    return full_path

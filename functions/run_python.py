from functions.get_directory import get_directory
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path = get_directory(working_directory, file_path, expect_type="file")
    if full_path.startswith("Error:"):
        return full_path
    if not full_path.endswith(".py"):
        return f"Error: {file_path} is not a Python file"
    
    cmd = ["python3", full_path] + args
    try:
        completed_process = subprocess.run(cmd, timeout=30, capture_output=True)
    except Exception as me:
        return f"Error: executing Python file: {me}"
    
    returncode = completed_process.returncode
    stderr = "STDERR: " + str(completed_process.stderr)
    stdout = "STDOUT: " + str(completed_process.stdout)
    if len(completed_process.stdout) == 0:
        stdout += "No output produced\n"

    result = ""
    if returncode != 0:
        result += f"Process exited with code {returncode}"
    
    result += stdout
    result += stderr

    return result

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the specified python code, constrained to the working directory, with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file": types.Schema(
                type=types.Type.STRING,
                description="The relative file path from the working directory to the file containing the python code to be run.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array containing any number of additional arguments for running the python code.",
                items=types.Schema(
                    type=types.Type.STRING, 
                    description="A single argument for the python file.")
            )
        },
    ),
)
# AI -------------------------------------------------------

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


# constants --------------------------------------------------------

'''the max number of characters to read from a file before truncating
(guards against excessive AI token usage)'''
MAX_CHARACTER_LIMIT = 10_000

'''a list of expected potential args (not required, just possible)'''
ALLOWED_ARGS = ["--verbose"] 

#formatting -------------------------------------------------------

'''for use in printing to console'''
DIV = "-------------------------------------------------"


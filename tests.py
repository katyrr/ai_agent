from functions.get_files_info import get_files_info

cases = [".", "pkg", "/bin", "../"]

for c in cases:
    if c == ".":
        dir = "current"
    else:
        dir = c

    print(f"Result for {dir} directory:")
    print(get_files_info("calculator", c))




'''
get_files_info("calculator", ".")
get_files_info("calculator", "pkg")
get_files_info("calculator", "/bin")
get_files_info("calculator", "../")
'''


from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from config import DIV


def test_get_file_content():
    print(DIV)
    cases = ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]
    
    for c in cases:
        print(f"results for {c}:")
        print(get_file_content("calculator", c))
        print(DIV)
        print()

    print(DIV)

def test_get_files_info():
    print(DIV)
    cases = [".", "pkg", "/bin", "../"]

    for c in cases:
        if c == ".":
            dir = "current"
        else:
            dir = c

        print(f"Result for {dir} directory:")
        print(get_files_info("calculator", c))
        print()

    print(DIV)

#test_get_files_info()
test_get_file_content()



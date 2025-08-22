from config import DIV
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test_run_python():
    print(DIV)
    cases = [
        ("calculator", "main.py"), #(should print the calculator's usage instructions)
        ("calculator", "main.py", ["3 + 5"]), #(should run the calculator... which gives a kinda nasty rendered result)
        ("calculator", "tests.py"),
        ("calculator", "../main.py"), #(this should return an error)
        ("calculator", "nonexistent.py") #(this should return an error)
    ]

    for c in cases:
        print(f"results for run_python{c}:")
        print(run_python_file(*c))
        print()
    
    print(DIV)

def test_write_file():
    print(DIV)
    cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed")
    ]
    
    for c in cases:
        print(f"results for write_content{c}:")
        print(write_file(*c))
        print()

    print(DIV)

def test_get_file_content():
    print(DIV)
    cases = ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]
    
    for c in cases:
        print(f"results for {c}:")
        print(get_file_content("calculator", c)[-100:])
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
#test_get_file_content()
#test_write_file()
test_run_python()



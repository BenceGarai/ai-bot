import unittest
from functions.run_python_file import run_python_file

class TestRunPython(unittest.TestCase):
    def test_run_calculator_usage(self):
        result = run_python_file("calculator", "main.py")
        print(result)
        
    def test_run_calculator(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)
        
    def test_run_calculator_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)
    
    def test_run_error(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
        
    def test_run_nonexistent(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        
    def test_run_lorem(self):
        result = run_python_file("calculator", "lorem.txt")
        print(result)
        
if __name__ == "__main__":
    unittest.main()
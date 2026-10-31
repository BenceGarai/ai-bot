import unittest
from functions.get_file_content import get_file_content

class TestGetFileContent(unittest.TestCase):
    def test_lorem_read(self):
        result = get_file_content("calculator", "lorem.txt")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")
        self.assertStartsWith(result, "Lorem")
    
    def test_main_read(self):
        result = get_file_content("calculator", "main.py")
        print(result)
        # dont want to talk about it
        self.assertStartsWith(result, "#")
        
    def test_pkg_read(self):
        print(get_file_content("calculator", "pkg/calculator.py"))
    
    def test_bin_read(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        self.assertStartsWith(result, "Error")
        
    def test_not_exist_read(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)
        self.assertStartsWith(result, "Error")
    
if __name__ == "__main__":
    unittest.main()
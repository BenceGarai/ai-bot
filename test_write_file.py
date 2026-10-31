import unittest
from functions.write_file import write_file

class TestGetWriteFile(unittest.TestCase):
    def test_lorem_write(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertStartsWith(result, "Successfully")
    
    def test_newfile_write(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertStartsWith(result, "Successfully")
    
    def test_error_write(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertStartsWith(result, "Error")
        
if __name__ == "__main__":
    unittest.main()
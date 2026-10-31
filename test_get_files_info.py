import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_current_dir(self):
        result = get_files_info("calculator", ".")
        print(result)
        self.assertStartsWith(result, "-")
    
    def test_bin_folder(self):
        result = get_files_info("calculator", "/bin")
        print('Cannot list "/bin"')
        self.assertStartsWith(result, "Error: C")
    
    def test_parent_folder(self):
        result = get_files_info("calculator", "../")
        print('Cannot list "../"')
        self.assertStartsWith(result, "Error: C")
    
    def test_main(self):
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertStartsWith(result, "-")
    
if __name__ == "__main__":
    unittest.main()
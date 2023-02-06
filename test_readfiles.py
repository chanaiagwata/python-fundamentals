import unittest
import readfiles

class TeastReadFiles(unittest.TestCase):
    '''
    Class to test the functions on the readfiles module
    Args:
        unittest.TestCase: Class from the Unittest module to create unit tests
    '''
    def test_get_data(self):
        '''
        Test case to confirm that we are getting data from the file
        '''
        with open("test.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data,readfiles.read_file("tests.txt"))




if __name__ == "__main__":
    unittest.main()
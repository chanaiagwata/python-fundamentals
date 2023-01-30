import unittest
from hello import Greeting

class TestGreeting(unittest.TestCase):
    '''
    Test class that defines test cases for the Greeting class behaviors
    Args:
    unittest.Testcase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case        
        '''
        self.new_greeting = Greeting("hello world!")
    
    def test_init(self):
        '''
        test_init test to test if the class is initialized properly
        '''
        self.assertEqual(self.new_greeting.greeting, "hello world!")


if __name__ == '__main__':
    unittest.main()

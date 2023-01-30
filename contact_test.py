import unittest #importing the unittest module
from contact import Contact #importing the contact class

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviors
    Args:
    unittest.Testcase: TestCase class that helps in creating test cases
    '''

    #First thing we're testing is if our objects are being instantiated correctly
    def setUp(self):
        '''
        Set up method to run before each test case        
        '''
        self.new_contact = Contact("James", "Muriuki", "0742363001", "james@gmail.com") #creates a contact object
    
    def test_init(self):
        '''
        test_init case to test if the objects is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0742363001")
        self.assertEqual(self.new_contact.email, "james@gmail.com")

if __name__ == '__main__':
    unittest.main()

#SetUp method allows us to define instructions that will be executed before each test method
#Above, we have used setUp method to create a new instance  of Contact class, before each test method declared, and stores it in an instance variable in the test class self.new_contact
# self.assertEqual is a testcase method that checks for an expected result, first argument is the expected result and second argument is the result actually gotten. I.e checking if the name and description of the new object is what is actually gotten
# if __name__ == '__main__', we are confirming that anything inside the code block should run only if this is the file that is currently being run
#unittest.main provides command line interface that collects all test methods and executes them

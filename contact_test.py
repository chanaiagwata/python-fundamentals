import unittest #importing the unittest module
from contact import Contact #importing the contact class
import pyperclip

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
    
    def tearDown(self):
        '''
        teardown method that does clean up after each test case has run
        '''
        Contact.contact_list = []
    
    def test_init(self):
        '''
        test_init case to test if the objects is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0742363001")
        self.assertEqual(self.new_contact.email, "james@gmail.com")

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

    def test_save_multiple_contact(self):
        '''
        test_save_multipe_contact to check multiple contact objects to our contact_list    
        '''
        self.new_contact.save_contact()

        #Below we create a new contact object called test_contact and save it
        test_contact = Contact("Test", "user", "0712345678", "test@user.com") #new contact

        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from contact list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678", "test@user.com") #new contact
        
        test_contact.save_contact()

        self.new_contact.delete_contact() #Deleting a contact object
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_by_number(self):
        '''
        test_find_contact_by_number to test if we can find a contact by phone number and display the information
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678", "test@user.com") #new contact

        test_contact.save_contact()

        found_contact = Contact.find_by_number("0712345678")
        self.assertEqual(found_contact.email,test_contact.email)
    
    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the contact.
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678", "test@user.com") #new contact
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0712345678")
        self.assertTrue(contact_exists)
    
    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts
        '''
        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

    # def test_copy_email(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found contact
    #     '''

    #     self.new_contact.save_contact()
    #     Contact.copy_email("0712345678")

    #     self.assertEqual(self.new_contact.email,pyperclip.paste())

        


if __name__ == '__main__':
    unittest.main()

#SetUp method allows us to define instructions that will be executed before each test method
#Above, we have used setUp method to create a new instance  of Contact class, before each test method declared, and stores it in an instance variable in the test class self.new_contact
# self.assertEqual is a testcase method that checks for an expected result, first argument is the expected result and second argument is the result actually gotten. I.e checking if the name and description of the new object is what is actually gotten
# if __name__ == '__main__', we are confirming that anything inside the code block should run only if this is the file that is currently being run
#unittest.main provides command line interface that collects all test methods and executes them

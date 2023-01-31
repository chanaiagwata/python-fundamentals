# -classes are blueprints to create objects
# e.g a car has many behaviors-starting,stopping, accelerating, decelerating.
# also a car has many features - heels, seat capacity ,fuel capacity, speed mileage, brand 
# the blueprint of this car will include all the features(attributes) and behaviors(methods)
# this is the template for creating car objects

#an object is an instance of a class

# Creating Classes

# class Contact:
#     """
#     class that generates new instances for contacts objects
#     """

#     pass

# __init__ method
# -Allows us to create new instance of a 
# -Also allows us to pass properties of the new object

# def __init__(self, first_name, last_name, phone_number, email):
#     """
#     __init__ method that enables to define properties for our object
#     Args:
#         first_name: New contact first name.
#         last_name: New contact last name.
#         number: new contact phone number.
#         email: new contact email address.
#     """

# The self variable used in the above __init__ method
# -Methods and functions in python have one major difference
# -Methods have one extra variable added to the beginning of the parameter list (The self variable)
# self is a variable that represents the instance of the object itself

# Therefore

import pyperclip
class Contact:
    """
    class that generates new instances for contacts objects
    """
    
    contact_list = [] #empty contact list

    def __init__(self, first_name, last_name, phone_number, email):
        #Doc strings removed for simplicity
        #Below we create four instance variables that take up the firstname, lastname, number, and email of the new contact
        self.first_name= first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        '''
        save_contact method that saves objects into contact_list
        '''
        Contact.contact_list.append(self)

    def delete_contact(self):
        '''
        delete_contact method deletes a saved contact from contact list 
        '''

        Contact.contact_list.remove(self)
    
    @classmethod #classmethod informs python that this is a method that belongs to the entire class
    
    def find_by_number(cls,number): #cls refers to the entire class, we cannot use self because it only refers to a particular object 
        '''
        Method that takes in a number and returns a contact that matches that number
        
        Args:
            number: phone number to search for
        Returns :
            Contact of person that matches the number
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
            
    @classmethod
    def contact_exist(cls,number):
        '''
        method that checks if a contact exists from the contact list
        Args:
            number: Phone number to search if it exists
        Returns:
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True
        return False
    
    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list
    
    # @classmethod
    # def copy_email(cls,number):
    #     contact_found = Contact.find_by_number(number)
    #     pyperclip.copy(contact_found.email)

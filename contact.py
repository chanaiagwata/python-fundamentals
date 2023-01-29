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
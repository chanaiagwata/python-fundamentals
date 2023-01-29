

# add items to dictionary
# birthdays = {"John":"August 1","Marcus":"April 8"}
# birthdays["mary"] = "June 9"

# print(birthdays)
# print(birthdays.values())

# setdefault() method
# When dealing with dictionaries, it is important to set placeholder values to keys before we do any operation to them to prevent unnecessary errors
# print("Enter a string")
# input_string = input()

# characters = {} #an empty dictionary that stores each individual character and how many times it has been used

# for character in input_string:
#     characters.setdefault(character, 0)
#     characters[character] = characters[character]+1

# used for loop to iterate through character in the input string
#used setdefault() to create  a key for each character if the character does not exist in the dictionary
# set default value for each character as 0
# Lastly we target the key that matches the character and add 1 everytime the character is encountered
# print(characters)

# print("Enter text")

# input_text = input()
# pressOnce = ["a", "d", "g", "j", "m", "p", "t", "w"]
# pressTwice = ["b", "e", "h", "k", "n", "q", "u", "x"]
# pressThrice = ["c", "f", "i", "l", "o", "r", "v", "y"]
# pressFour = ["s", "z"]

# text = {}



# for character in input_text:    
#     if character in pressOnce:
#         text.setdefault(character, 1)
#         continue

#     elif character in pressTwice:
#         text.setdefault(character, 2)
#         continue

#     elif character in pressThrice:
#         text.setdefault(character, 3)
#         continue

#     else:
#         text.setdefault(character, 4)

# print(sum(text.values()))


# alpha = "Illk"
# password = "K34jndnks"
# number_string = "12345"
# tabbs = "       "
# titles = "I Love Cups"
# false_titles = "I love Cups"

# print( alpha.isalpha() )
# print( password.isalnum() )
# print( number_string.isdecimal() )   
# print( tabbs.isspace() )
# print( titles.istitle() )
# print( false_titles.istitle() )

# print("Enter a noun")
# response = input()

# print(f"I don\'t think anyone of us knows what {response} means")

# Type Casting
# is the act of converting one type of data to another so as to manipulate in some other way
# slicing
# getting parts /subsets of strings,lists, tuples

# greet = [3,6,4,7,5,32]

# part_one = greet[0:3]
# print(part_one)


# stringcode = "PYTHONCODE"

# print(stringcode[0:4])
# print(stringcode[2:7])
# print(stringcode[-7:-2])

# print(stringcode[-1:-4:-1]) #slicing in the reverse direction, a third argument -1 must be added to indicate that the program is running in a reverse direction 
# print(stringcode[-3:-7:-1])

# greetings = 'Hello, Moringa!'

# part_one = greetings[4:11]
# print(part_one)

# def funct():
#     print("I have been called")

# funct()

# function is created in python with a key word def
# function must be called to execute the code within them
# for python we don't use the curly brackets to enclose the code within the function, instead we use colons

# Arguments


# def funct(a, b):
#     print(a+b)

# funct(1,4)

#with keyword argument (a=1, b=4), but later evaluates to the values passed to the function when being called
# def func_a(a=1, b=4):
#     print(a+b)

# func_a(a=6, b=7)

#Creating an empty function
#Sometimes we might want to define a function and not put code in it

#Empty function

# def func_a():
#     pass

#functions that return something
# def func_a(a,b):
#     return a+b #return helps us to get the value from the operation being performed in the function

# sum = func_a(4,5)

# print(sum)

# def return_42():
#     return 42 #An explicit return statement


# print(return_42()) #The caller code gets 42

# explicit return statements can be used without a return
# But in this case the function caller will return none

#if an explicit return statement that has a value is used,
#then the return value can be used in any epression

# def return_42():
#     return 42 #An explicit return statement

# num = return_42()*2
# print(num)

# since the caller function return_42() returns a numeric value, mathematical expressions
# can be used to take advantage of the return value


# def get_even(numbers):
#     even_nums = [num for num in numbers if not num%2]
#     return even_nums #results of the above expression used as a return value-common practice

# even_int = get_even([1,2,3,4,5,6])
# print(even_int)

# def mean(sample):
#     return sum(sample)/len(sample)

# result = mean([1,3,5,6,7])
# print(result)

# Returning Vs Printing
# Returning a value and printing a value are not equivalent operations

# def print_greeting():
#     return "Hello, World"

# print(print_greeting())

# def add(a,b):
#     result = a+b
#     return result

# print(add(2,2))

# import statistics as st

# def describe(sample):
#     return st.mean(sample), st.median(sample), st.mode(sample)


# print(describe([10, 2, 4, 7, 9, 3, 9, 8, 6, 7]))
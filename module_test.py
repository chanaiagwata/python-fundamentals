

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

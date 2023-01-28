# Tuples
#They are like lists bu immutable-values cannot be changed once created
# tuple_a = ('a', 'b', 'c', 'd')
# tuple_b = (1,2,3,4,5)
# tuple_c = (1, 'west', 34, 'long')
# d = (1,2,3,4)
# tuple_d = tuple(d)
# print(tuple_d)

# Dictionary
# Empty dictionary
# my_dict = {}

#Dict with keys and values
# my_cat = {
#     'name': 'sniff',
#     'age':10,
#     'color':'black',
# }
# appearance = my_cat['color']
# print(appearance)
# instead of the index used in lists, for dictionaries we access values using their keys
# list example
 
# students = ["jane", "dan", "ken", "faith"]
# teachers = ["Shie", "Kyla", "Jammy"]
# students.extend(teachers)

# print(students)

# one_stud = students[1]
# print(one_stud)

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

print("Enter text")

input_text = input()
characters = ["a", "b", "c", "e" "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"]
pressOnce = ["a", "d", "g", "j", "m", "p", "t", "w"]
pressTwice = ["b", "e", "h", "k", "n", "q", "u", "x"]
pressThrice = ["c", "f", "i", "l", "o", "r", "v", "y"]
pressFour = ["s", "z"]

text = {}



for character in input_text:    
    if character in pressOnce:
        text.setdefault(character, 1)
        continue

    elif character in pressTwice:
        text.setdefault(character, 2)
        continue

    elif character in pressThrice:
        text.setdefault(character, 3)
        continue

    else:
        text.setdefault(character, 4)

print(sum(text.values()))


    


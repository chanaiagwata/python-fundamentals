# greeting = "hello"
# school = "Moringa"

# print(greeting+ ", " + school+ "!")

# from math import sqrt, ceil
# x = sqrt(9)
# print(x)
# y = ceil(x)
# print(y)

# import random
# we can generate a random number using the randit method

# random_number = random.randint(100,6000)

# print(random_number)
# r = random.randint(2, 5)
# p = 3.14
# circumference = 2*p*r
# print(circumference)

# height = 66 #units in inches
# if height>70:
#         print("you are really tall")
# elif height>60:
#         print("you're average height")
    
# else:
#         print("you are really short")

#Checking for nothing
# An empty value is automatically considered to be False
# list_a = []

# if list_a:  #automatically evaluates to false beecause it is empty
#     print("I will not run")
# else:
#     print("I am empty")

# Looping
# Executes code over and over    again
#for loop
# used to repeat something repeatedly
# numbers = [1,2,3,4,5]

# for number in numbers:
#     print(number)
#loops through the number list and stores each individual number in a variable called number

# Range()
# We can use range() in for loops
# range() returns a list for which we can use to loop through
#lets use range() to create a list
# list_a = list(range(0,5))
# print(list_a)

# the list() method converts it to a list
# for i in range(0,7):
#     print(i)

# the str() method converts i into a string to allow easy concatenation with the rest of the stringthe str() method converts i into a string to allow easy concatenation with the rest of the string

# numbers = [1, 2, 3, 4, 5, 6]
# for i in numbers:
#     if i%2 ==0:
#         print(i)
# While loops
# while loops are often used as counters
#  
# players = 11
# player = list(int())

# while players >=5 :
#     print("The remaining number of players are", players)
#     players -=1


# for i in range(0,11):
#     if i >=5:
    
#         print("The remaining number of players are", i)

# numbers = 6

# while True:
#     numbers +=1
#     if numbers == 25:
#         break
#     print (numbers)


#  break statement

# allows code to jump out of the loop after condition has been met

# continue statement
# Allows us to jump back into the loop

# taken numbers
# numTaken = [3,5,7,11,13]

# print("Available numbers")

# #loop
# for i in range(0,20):
#     if i in numTaken:
#         continue
#     print(i)

# players = 11
# while players >=5:
#     players -=1
#     print(players)

# lista = [10,2,-3,4,5]
# listb = ['cat', 'dog']

# # lista.extend(listb)
# # lista.append("key")
# # lista.reverse()
# lista.sort()
# print(lista)

# birthdays = {"John":"August 1","Marcus":"April 8"}
# birthdays["mary"] = "september, 24"
# print(birthdays.values())

print("Enter a string")

input_string = input()

characters = {}

for character in input_string:
    characters.setdefault(character,0)
    characters[character] = characters[character] + 1

print(characters)
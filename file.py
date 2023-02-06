# file_variable = open("filename", "mode")

# filename is the name of the file or path
# mode tells interpereter which way the file will be used
# modes can be:
# r-read only -r is also the default mode
# w -write only
# a - we can add items at the bottom of the file
# r+ -file is on both read and write mode

handle = open("test.txt", "r")

data = handle.read()
counter = 0
for word in data.split():
    if word == "Python":
        counter += 1


print(counter)
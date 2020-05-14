# Steven Thompson Jr
# 5-14-2020
# Assignment 10.1
# Checks for existing directory, retrieves name, address, and phone number from user, saves info into file
# Once saved, the file will be read and the contents dispalyed to the user for verification

import os

#retrieving directory and verifying it exists
found = False
while found != True:
    path = input("Please enter the entire path of the directory where you would like to save your file:\n")
    if os.path.isdir(path) == True:
        break
    else:
        print("I'm sorry.  That directory does not exist.  Please try again.")

#retreiving user info
name = input("Please enter your name: ")
address = input("Please enter your address: ")
phone = input("Please enter your phone number: ")

#writing info to a file.  all info will be in one line seperated by a comma
filename = 'info.txt'
pathName = os.path.join(path, filename)
with open(pathName, 'w') as info:
    info.write(f"{name}, ")
    info.write(f"{address}, ")
    info.write(f"{phone}.")

#reading file and displaying info in file
with open(pathName, 'r') as info:
    information = info.read()
print(information)
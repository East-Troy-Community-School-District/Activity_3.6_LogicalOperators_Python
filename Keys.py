'''
Keys
Pawelski
10/15/2023
Introduction to Computer Science

Instructions:
Run the program and try entering different roles.
What two roles get a key? What role does not get a key?
What happens when you try a role like "parent"? Why does
this happen? 

Modify the program so that a person with the "coach"
role gets a key.
'''

role = input("What is your role?")
if role == "teacher" or role == "administrator":
    print("You get a key!")
elif role == "student":
    print("You don't get a key.")
else:
    print("Invalid role.")

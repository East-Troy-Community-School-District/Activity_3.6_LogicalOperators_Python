'''
Keys
Pawelski
2/3/2025

Instructions:
1.  Run the program and try entering different roles.
    What two roles get a key?
    What role does not get a key?
    What happens when you try a role like "parent"?
2.  Modify the program so that a person with the "coach"
    role gets a key.
'''

role = input("What is your role?")
if role == "teacher" or role == "administrator":    # Add your code for step 2 here!
    print("You get a key!")
elif role == "student":
    print("You don't get a key.")
else:
    print("Invalid role.")

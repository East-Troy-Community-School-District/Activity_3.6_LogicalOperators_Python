'''
Staff Directory
Pawelski
10/15/2023
Introduction to Computer Science

Instructions:
Run the program and try entering different names.
What can you enter to access Mr. Pawelski's entry
in the staff directory? What about Mr. Mass? Based
on the last two programs, when should you use and?
When should you use or? 

Modify the program so that Mr. Hoff is part of the
staff directory. YOu should be able to enter his
entry by using the values "Hoff", "Michael Hoff",
and "Mr. Hoff".

Finally, let's look at one of the biggest mistakes
students make when working with the logical operators
for the first time. Modify the code on line  so it looks
like this...

if staff == "Pawelski" or "Nolan Pawelski" or "Mr. P":

Run the program and try entering "Mass". The program does
not give you the right entry! Why?
'''

staff = input("Enter the name of the staff member you want to look up >> ")
if staff == "Pawelski" or staff == "Nolan Pawelski" or staff == "Mr. P":
    print("Room: 603")
    print("Extension: x5250")
elif staff == "Mass" or staff == "Michael Mass" or staff == "Mr. Mass":
    print("Room: 316")
    print("Extension: x5232")
else:
    print("No entry. Not a staff member or invalid.")
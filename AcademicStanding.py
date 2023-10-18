'''
Academic Standing
Pawelski
10/15/2023
Introduction to Computer Science

Instructions:
Let’s look at an example involving multiple
logical operators in a single Boolean expression.
Run the program and try entering different
combinations of grades and absences. What must
be true in order to be in good academic standing?

In the last few programs, we saw what happens when
you have multiple logical operators and mix logical
operators within a single Boolean expression. You
may have noticed in this program, we had to use
parenthesis around the or operators. Just like the
math operators, Python executes the logical operators
in a specific order: not, and, or. This means we need
to use parentheses to force Python to evaluate all
the ors before the ands. 
'''

grade = input("What is your current grade? (A, B, C, D, or F) >> ")
absences = int(input("How many times have you been absent? >> "))
if (grade == "A" or grade == "B" or grade == "C" or grade == "D") and absences <= 2:
    print("You are in good standing!")
else:
    print("You are in bad standing!")

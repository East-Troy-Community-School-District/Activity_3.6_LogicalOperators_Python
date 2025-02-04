'''
Academic Standing
Pawelski
2/3/2025

Instructions:
1.  Let’s look at an example involving multiple
    logical operators in a single Boolean expression.
    Run the program and try entering different
    combinations of grades and absences. What must
    be true in order to be in good academic standing?
2.  Modify line  so that it looks like this (delete the
    parentheses around the or statements)...
    
    if grade == "A" or grade == "B" or grade == "C" or grade == "D" and absences <= 2:
    
    When you enter that you got a grade of D and had 55 absences (i.e., you were
    gone for the entire trimester), the program still reports that
    you are in good academic standing (it shouldn't). Why? I would
    suggest putting in a breakpoint on line  and stepping through the program
    to see how the code executes. Based on this, in what order are the
    and, or, and not operators executed? What do the parentheses do?
'''

grade = input("What is your current grade? (A, B, C, D, or F) >> ")
absences = int(input("How many times have you been absent? >> "))
if (grade == "A" or grade == "B" or grade == "C" or grade == "D") and absences <= 2:
    print("You are in good standing!")
else:
    print("You are in bad standing!")

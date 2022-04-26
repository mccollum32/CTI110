#Debug
#P3HW1-Debugging
#Apr 26 2022
#McCollum, Joseph


def main(): #this is used to define the 'main' function
# This program takes a number grade and outputs a letter grade.
# system uses 10-point grading scale
    """Grading Scale
    A 100 - 90
    B 80 - 70
    C 70 -65
    D 65 - 60
    """
    score = float(input('Enter your grade: '))

#Conditional IF/Elif/Else Statement
    if score >= 90:
        print("Grade is: A")

    elif score >= 80:
        print("Grade is: B")

    elif score >= 70:
        print("Grade is: C")

    elif score >= 60:
        print("Grade is: D")

    else:
        print("Failing score")
    
main() #use this to call the 'main' function start the program
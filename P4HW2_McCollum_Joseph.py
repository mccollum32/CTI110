## A brief description of the project - This program is to calculate number of pizzas you need to order for a group of students
## May 6 2022
## CTI-110 P4HW2 - Pizza Order
## McCollum, Joseph

import math

choice1 = 1.5
choice2 = 2
choice3 = 3
quit_pro = 'x'

#def main is the function
def main():
    
    #food variable controls the loop
    food = 0
    
    while food != quit_pro:
        
        #user controlled inputs contain floats/ intergers
        food = float(input('Enter number of people per pizza (1.5 , 2 , or 3): '))
        students = int( input('How many students would you like to order pizza for? '))
        pizza =  float(input('Enter the number of pizza\'s: ')) 
        pizza = math.ceil(students/pizza)

        #IF/Elif/Else statements contain the calculations for each choice
        if food == choice1:
            
            print()
            print('----Pizza Order ----')
            print('Nuber of students entered: ' , students) 
            print('Pizza choices: ' , food)
            print(f"Number of Pizzas needed:  {pizza / 6:.2f}")
            print('-------------------------')
            print('Would you like to end the program? (y or Y for yes): ')
            choice = input()
            if choice == 'y' or choice == 'Y':
                break
            else:
                main()
            
        elif food == choice2:
            
            print()
            print('----Pizza Order ----')
            print('Nuber of students entered: ' , students) 
            print('Pizza choices: ' , food)
            print(f"Number of Pizzas needed:  {pizza / 6:.2f}")
            print('-------------------------')
            print('Would you like to end the program? (y or Y for yes): ')
            choice = input()
            if choice == 'y' or choice == 'Y':
                break
            else:
                main()
            
        elif food == choice3:
            
            print()
            print('----Pizza Order ----')
            print('Nuber of students entered: ' , students) 
            print('Pizza choices: ' , food)
            print(f"Number of Pizzas needed:  {pizza / 6:.2f}")
            print('-------------------------')
            print('Would you like to end the program? (y or Y for yes): ')
            choice = input()
            if choice == 'y' or choice == 'Y':
                break
            else:
                main()
            
        else:
            print('Invalid entry!')
            print('Enter one of the following --> (1.5 , 2 or 3)')
            print('Enter number of people per pizza again! ')
            



    
if __name__ == "__main__":
    main() #the main function that calls for the program to start
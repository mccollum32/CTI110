## A brief description of the project - This program is to calculate number of pizzas you need to order for a group of students
## April 27 2022
## CTI-110 P3HW2 - Pizza Order
## McCollum, Joseph

choice1 = 1.5
choice2 = 2
choice3 = 3
quit_pro = 'y'

#def main is the function
def main():
    
    #food variable controls the loop
    food = 0
    
    while food != quit_pro:
        
        #user controlled inputs contain floats/ intergers
        food = float(input('Enter number of people per pizza (1.5 , 2 , or 3): '))
        students = int( input('How many students would you like to order pizza for? '))
        pizza =  float(input('Enter the number of pizza\'s: ')) 

        #IF/Elif/Else statements contain the calculations for each choice
        if food == choice1:
            
            print('Right amount')
            print('----Pizza Order ----')
            print('Nuber of students entered: ' , students) 
            print('Number of Pizza choices: ' , food)
            print(f"Number of Pizzas needed:  {pizza / 6:.2f}")
            print('-------------------------')
            
        elif food == choice2:
            
            print('Right amount')
            print('----Pizza Order ----')
            print('Nuber of students entered: ' , students) 
            print('Number of Pizza choices: ' , food)
            print(f"Number of Pizzas needed:  {pizza / 6:.2f}")
            print('-------------------------')
            
        elif food == choice3:
            
            print('Right amount')
            print('----Pizza Order ----')
            print('Nuber of students entered: ' , students) 
            print('Number of Pizza choices: ' , food)
            print(f"Number of Pizzas needed:  {pizza / 6:.2f}")
            print('-------------------------')
            
        elif food == quit_pro:
            print('Ending the program..')
            
        else:
            print('Invalid entry!')
            print('Enter one of the following --> (1.5 , 2 or 3)')
            print('Run the program again')
            



    
if __name__ == "__main__":
    main() #the main function that calls for the program to start
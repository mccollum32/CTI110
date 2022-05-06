# CTI-110
# P4HW1 - Score Avg
# McCollum, Joseph
# Date: 5/5/2022
#P4HW1_McCollum_Joseph.py

num_scores=int(input('How many scores do you want to enter? '))
num = 1
score_list=[]

#While loop/If statement
while num <= num_scores:
    print('Enter score #{}: '.format(num), end= '')
    score = float(input())
    
    if (score < 0) or (score > 100):
        print('INVALID Score entered!!!!')
        print('Should be between 0 and 100')

    else:
        score_list.append(score)
        num += 1 


print('**********Results**********')
#Lowest Score using the min function
print('Lowest Score: ', min(score_list))
lowest_scored = min(score_list)

#Remove the lowest scored using the remove function
score_list.remove(lowest_scored)

#Updated list after the lowest score removed
print('Modified List: ',score_list)
average_scores = sum(score_list) / len(score_list)
print(f'Score Averaged: {average_scores:.2f}')
print('********************************')
print()
def feet_to_steps(user_feet):
    total_steps=int(user_feet/2.5)
    return (total_steps)
    
if __name__ == '__main__':
    user_feet=float(input())
    total_steps=feet_to_steps(user_feet)
    print(total_steps)
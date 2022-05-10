def laps_to_miles(laps):
    return laps * .25
    
if __name__ == '__main__': 
    laps = float(input())
    num_miles = laps_to_miles(laps)
    print(f'{num_miles:.2f}')
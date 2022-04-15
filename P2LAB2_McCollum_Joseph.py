current_price = int(input()) #current_price
current_price_print = str(current_price) #dollar sign output
last_months_price = int(input())
change = int(current_price - last_months_price)
change_print = str(change)
monthly_morg = float((current_price * 0.051) / 12) #mortgage calculating value
formatted_morg = str("{:.2f}" .format(monthly_morg)) #mortgage output
print(f"This house is ${current_price_print}. The change is ${change_print} since last month." ) #f string formatting 
print("The estimated monthly mortgage is $",formatted_morg, "." , sep="") #Sep spacing between
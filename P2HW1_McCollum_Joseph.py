   # Total Purchases request 5 prices for purchased items. Subtotal/Sales Tax + Overall Total.
    # Apr 14 2022
    # CTI-110 P2HW1 - Total Purchases
    # McCollum, Joseph
    #P2HW1_McCollum_Joseph

#Item prices listed as floats / User enters prices of each item
i_price1 = float (input('Enter first price $'))
i_price2 = float (input('Enter Second price $'))
i_price3 = float (input('Enter Third price $'))
i_price4 = float (input('Enter Fourth price $'))
i_price5 = float (input('Enter Fifth price $'))

#Subtotal of all prices / sales tax
sub_total = i_price1 + i_price2 + i_price3 + i_price4 + i_price5
sales_tax = sub_total / 7
total = sub_total + sales_tax 

#Results of all prices 
print('======RESULTS======')
print(f'Subtotal: ${sub_total:.2f}') #Subtotal of all prices
print(f'Sales tax: ${sales_tax:.2f}') #Sales tax/ Floating point number
print(f'Total Prices: ${total:.2f}') #Total / Floating point number
print('====================')
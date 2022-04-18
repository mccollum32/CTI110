#Variable names/ Inputs
red = int(input()) 
green = int(input())
blue = int(input())
gray = 50

#condtional IF statements using 'And'
if (red <= green) and ( red <= blue):
    gray = red 
if (green <= red) and ( green <= blue):
    gray = green
if (blue <= green) and ( blue <= red):
    gray = blue

red = red - gray
green = green - gray
blue = blue - gray

print(red, green , blue)

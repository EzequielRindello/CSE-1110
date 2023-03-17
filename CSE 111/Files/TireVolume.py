#Import the datetime and math library.
import math
from datetime import datetime
current_date=datetime.now()
#Print the information.
print(f"Today is: {current_date:%Y-%m-%d}")

# Print description.
print("This program will calculate and display the volume of space inside a tire\n")

# Gets the input and covert it to an int.
width= float(input("Enter the width of the tire in mm :"))
aspectRatio= float(input("Enter the aspect ratio of the tire:"))
diameter= float(input("Enter the diameter of the wheel in inches :"))

#Calculations.
num1=(width* aspectRatio)+(2540 *diameter)
num2= math.pi* width**2 *aspectRatio
num3= num2 *num1
total=num3/10000000000
total=round(total, 1)

#Print the results.
print("")
print(f"The approximate volume is {total} liters")

#Open and save file. 
with open("volumen.txt", "r+") as tire_volume:
    print(f"current date: {current_date}", file=tire_volume)
    print(f"width of the tire:{width}", file=tire_volume)
    print(f"aspect ratio of the tire:{aspectRatio}", file=tire_volume)
    print(f"diameter of the wheel:{diameter}", file=tire_volume)
    print(f"volume of the tire:{total}", file=tire_volume)

    #Aditional code for grade.
    print("Do you want to buy tires with the dimensions entered?\n")
    answer=input("Please enter Y/N")
    if answer=="Y":
        for line in tire_volume:
            print(line)
    else :
        print("Goodbye")
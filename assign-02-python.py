#!/usr/bin/env python3
# Created by: Alex M
# Created on: Oct. 11, 2023
# This program calculates and displays the area and perimeter of a
# heptagon 

# importing math module to use mathematical functions and constants 
import math

#Asking user side 
side_length = float(input("Enter the length of the side (cm): "))

# this function takes an argument side_length and calculates the area, result returns to the function
def area_of_heptagon(side_length):

    # calculate the area and perimeter
    area = (7/4) * side_length**2 * (1 / math.tan(math.pi/7))
    return area

def perimeter_of_heptagon(side_length):
    perimeter = 7 * side_length
    return perimeter

#These lines take the result of the argument "side_length" and store them in the variable 
heptagon_area = area_of_heptagon(side_length)
heptagon_perimeter = perimeter_of_heptagon(side_length)

# display's the area and perimeter of the heptagon 
print(f"The area of the heptagon is: {heptagon_area:.2f}")
print(f"The perimeter of the heptagon is: {heptagon_perimeter:.2f}")


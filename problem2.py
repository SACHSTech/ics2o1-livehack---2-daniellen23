""""
Name: triangle_checker.py

Purpose: This program will check if the user inputted side lengths will make a triangle or not

Author: Nguyen.D 

Created: 2021-02-23
"""
#welcome message
print("Welcome To The Triangle Checker.")

#user input
first_side = int(input("Enter the length of the first side: "))
second_side = int(input("Enter the length of the second side: "))
third_side = int(input("Enter the length of the third side: "))

#triangle or not
if first_side + second_side > third_side and second_side + third_side > first_side and first_side + third_side > second_side:
  print("The figure is a triangle.")

else:
  print("The figure is not a triangle.")

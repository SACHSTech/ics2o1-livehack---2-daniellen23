""""
Name: alien_classification.py

Purpose: This program will detect and classify life forms from Mars, depending on the amount of antennae and eyes.

Author: Nguyen.D 

Created: 2021-02-23
"""
#Martian Class Criteria 
# AudreyMartian  | at least 3 antenna and at most 4 eyes  |
# MaxMartian  | at most 6 antenna and at least 2 eyes  |
# BrooklynMartian  | at most 2 antenna and at most 3 eyes  |
# MattDamonMartian  | No antenna and 2 eyes  |

#user input
antenna = int(input("Enter Number of Antennae Detected by Perseverance: "))
eyes = int(input("Enter Number of Eyes Detected by Perseverance: "))

# Declare criteria
AudreyMartian = antenna >= 3 and eyes <= 4
MaxMartian = antenna <= 6 and eyes >= 2 and not (antenna == 0 and eyes == 2)
BrooklynMartian = antenna <= 2 and eyes <= 3 and not (antenna == 0 and eyes == 2)
MattDamonMartian = antenna == 0 and eyes == 2

# if statements 
if AudreyMartian:
  print ("Lifeform Detected: AudreyMartian")
if MaxMartian: 
  print("Lifeform Detected: MaxMartian")
if BrooklynMartian:
  print("Lifeform Detected: BrooklynMartian")
if MattDamonMartian:
  print("Lifeform Detected: MattDamonMartian")

if not AudreyMartian and not MaxMartian and not BrooklynMartian and not MattDamonMartian:
  print("No life form Detected")


""""
===========================
### alternate option ###
===========================
# if statements
if antenna >= 3 and eyes <= 4:
  print("Lifeform Detected: AudreyMartian")
if antenna <= 6 and eyes >= 2 and not (antenna == 0 and eyes == 2):
  print("Lifeform Detected: MaxMartian")
if antenna <= 2 and eyes <= 3 and not (antenna == 0 and eyes == 2) :
  print("Lifeform Detected: BrooklynMartian")
if antenna == 0 and eyes == 2:
  print("Lifeform Detected: MattDamonMartian")

if not (antenna >= 3 and eyes <= 4) and not (antenna <= 6 and eyes >= 2) and not (antenna <= 2 and eyes <= 3) and not (antenna == 0 and eyes == 2):
  print("No life form Detected")
"""
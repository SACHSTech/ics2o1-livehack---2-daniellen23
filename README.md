# ICS2O1 LiveHack 2

## Instructions
For each of the described problems:
* Complete a flowchart for each described problem (see Google Classroom post)
* Write a python solution to the problem in the appropriate file
* Use proper variable naming
* Use appropriate commenting and include a program header
* Make input and output user friendly.


### Running your code
You can enter the following in the terminal to run your code:  
`python3 problem1.py`  
`python3 problem2.py`  


## Problem 1
NASA's Perseverance Rover has just landed on Mars and is ready to start discovering the planet. One of it's tasks is to detect life forms and classify them for research.   The rover is equipped with special sensors that can detect how many antenna and how many eyes a deteted life form has.  It will classify detected life forms based on the following critera:

| Martian Class  | Criteria  |
|---|---|
| AudreyMartian  | at least 3 antenna and at most 4 eyes  |
| MaxMartian  | at most 6 antenna and at least 2 eyes  |
| BrooklynMartian  | at most 2 antenna and at most 3 eyes  |
| MattDamonMartian  | No antenna and 2 eyes  |


#### Input Specification
The user will be prompted to enter two numbers. First, the user will be prompted to enter the number of antenna detected by Perseverance. Second, the user will be prompted to enter the number of eyes detected by Perseverance.





#### Output specification
The output will be the list of aliens who match the criteria outlined above. If no aliens match the critera, output "No life form detected".

#### Sample Run 1  
```
How many antennas? 4 
How many eyes? 5 
Life form detected: MaxMartian
```

#### Sample Run 2
```
How many antennas? 2 
How many eyes? 3 
Life form detected: MaxMartian
Life form detected: BrooklynMartian
```

#### Sample Run 3
```
How many antennas? 0 
How many eyes? 2 
Life form detected: MattDamonMartian
```

#### Sample Run 4 
```
How many antennas? 8 
How many eyes? 6 
No life form detected
```

## Problem 2
Three numbers represent the sides of a triangle when the sum of any two sides is greater than the third side. For example, 3, 4, and 5 are the sides of a triangle because the sum of any pair of sides is bigger than the third side. But 12, 3, and 8 are not sides of a triangle because 3 + 8 = 11 is not greater than 12. 

Write a program to have the user enter three lengths of sides and determine whether the figure is a triangle or not. Do not assume that the side lengths are entered in any particular order.

#### Sample Run 1
```
Welcome to the Triangle Checker
Enter the length of the first side: 3
Enter the length of the second side: 4
Enter the length of the third side: 5
The figure is a triangle.
```

#### Sample Run 2  
```
Welcome to the Triangle Checker
Enter the length of the first side: 12
Enter the length of the second side: 3
Enter the length of the third side: 8
The figure is NOT a triangle
```








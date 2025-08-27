'''
Task 1: Perform Basic Mathematical Operations

Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.

Expected Output:
The output should include the result of each operation performed
'''


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print(
    "\nAddition: ", a+b,
    "\nSubtraction: ", a-b,
    "\nMultiplication: ", a*b,
    "\nDivision: ", a/b
)
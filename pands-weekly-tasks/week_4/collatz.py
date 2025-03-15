"""1. Write a program, called collatz.py, 
2. that asks the user to input any positive integer 
3. and outputs the successive values of the following calculation.
    3.1 At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
4.Have the program end if the current value is one.

5. Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

Example of it running:

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1"""
value = int(input("Please enter a positive integer: "))# Asks user to enter a positive number
print(value, end=' ')
while value != 1:
    if value % 2 == 0:# Checks if it's even by using module operator to see if there is no remainder
        value = value // 2# Divide value by 2 and store it in a new variable
    else: value = (value * 3) + 1

    print (value, end=' ')

print()




















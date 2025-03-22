'''Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.'''

def sqrt(message = 'Please enter a positive decimal number: '):# Defining function
    num = False
    while (not num):
        try: # Part of try except to catch value error
            num = float(input(message))
            if num <= 0:
                print("Please enter a positive number")
                num = False


           # Check if the number is a float and not an integer
            if num == int(num):
                print('Please enter a valid decimal number')
                num = False

        except ValueError: # Exception statement
            print('That is not a valid number. Please try again.')
        sq_root = num ** 0.5 #Calculate the square root of that number
    return sq_root# return that value 


print(f'The square root is approx. {sqrt()}')

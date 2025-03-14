'''Weekly Task 03

Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890

Extra:

Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)'''

# Read in 10 character number
# Replace first 6 numbers with Xs
# Print out number with Xs
# Modify program to deal with account number is of any length
mask_l = "X"
acc_num = list(input("Please enter 10 character account number: "))


for i in range(min(6, len(acc_num))):
    acc_num[i] = mask_l
asked_acc_num = ''.join(acc_num)
print(asked_acc_num)























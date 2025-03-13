first_ammount = int(input("Please enter first amount in cents :"))
print("The first amount in cents is :", first_ammount)

second_amount= int(input("Please enter second amount in cents :"))
print("The second amount in cents is :", second_amount)

total_amount = first_ammount + second_amount

print("The sum of these is " f'€{total_amount/100:.2f}')

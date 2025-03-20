import random #Importing the random class

days_of_wk = ('Mon', 'Tue', 'Wens', 'Thurs', 'Fri', 'Sat', 'Sun')# Creates tuple with days of the week

for day in days_of_wk:#Loops through tuple
    rand_day = random.randint(0, len(days_of_wk))#Randomly chooses the index of each element in the tuple and stores the index of each day in a rand_day variable
    if rand_day > 5:# If the element is less than 5
        print(f'Today is {day}. Yes, unfortunately today is a weekday.')#Print out the day and explain this is a weekday

else:#Otherwise
    print(f'Today is {day}. It is the weekend, yay!')#Print out the day and explain this is a weekend

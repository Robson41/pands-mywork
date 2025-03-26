'''Weekly Task 8

Write a program called plottask.py that displays:

    a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

Some marks will be given for making the plot look nice (legend etc).'''

import numpy as np #Import numpy
import matplotlib.pyplot as plt #Import MATPLOTLIB

numbers = np.random.normal(loc=5, scale=2, size=1000) #creating normal distribution with a size,meand and standard deviation
plt.hist(numbers, label= 'Normal Distribution')#plot the Normal distribtion to a histogram and label it

x= np.array(range(0,11))#Creating a range of numbers between 0 to 10 inclusive
y = x**3 # x cubed is equal to y
plt.plot(x,y,  label = 'h(x)=x3')#Plotting x and y on the chart and labelling it


plt.legend()#Associating labels with the plotted data
plt.savefig('histogram_function_plot.png')#Saving the histogram / plot as a png file
plt.show()#Showing the generated histogram / plot diagram



'''Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.'''

import sys

FILENAME = 'moby-dick.txt'
if len(sys.argv) != 2:
    print('You need to add the filename as an argument')

FILENAME = sys.argv[1]

print(f' The filename provided is {FILENAME}')

with open(FILENAME, 'rt') as f:
    for data in f:
        freq = data.count('e')
        print(freq)



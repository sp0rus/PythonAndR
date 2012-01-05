#January 5, 2012 Notes

###################################################################

#Try/Except Blocks

try:
    for line in file("doesNotExist"):
        line = line.strip()
        #.
        #.
        #.
except IOError:
    print "The file failed to open!"

###################################################################

# Some other error types

int("cat") # ValueError
1/0 # ZeroDivisionError
range(5)[10] # IndexError

###################################################################

import urllib

#urlopen returns a file handle, read pulls the whole file to be read
yahoo = urllib.urlopen(http://m.yahoo.com").read()
print yahoo #prints the webpage out
sleep(2) # be nice to the server

###################################################################

#Linear Transformation
#   -Scaling approach
#      - used for scaling datasets
#      - Example: stock market investing, comparing two stocks at different prices
#           - scaling so that all values exist between 0 and 1 and retain their shape

#vector x

# Step 1
#   f(x)= (xi-low(x))/(high(x)-low(x))
# Step 2
#   x = xi - x0

###################################################################

# Numpy
#   - linear algebra library in Python

#Python's sequence data structure is a "list"
#Numpy has its own ndarray "array" data structure

#Array's are created with the following:
#   - based on existing Python lists
#   - a generator function
#   - reading straight from a data file

import numpy as np

a = [0.0, 1.0, 2.0, 3.0, 4.0] # a python list
npa = np.array(a) # converting the list to a numpy array
npa = np.arange(0.0, 5.0, 1.0, dtype = float) # make an array given a range and a type
npa = np.linspace(1.0,4.0,5) # make an array given a starting space, ending space, and number of elements

npa = np.zeros(5) # generate a vextor of zeros
npa[0] = 0.0
npa[1] = 1.0
npa[2] = 2.0
npa[3] = 3.0
npa[4] = 4.0

# ********

#Given a text file:

#numbers.txt
0.0
1.0
2.0
3.0
4.0

### End text file

npa = nploadtxt("numbers.txt") #loads the text file and cleans the data to some extent

vector = np.loadtxt("data.dat", usecols=[2],skiprows=1,delimiter=',')

###################################################################

# EXAMPLES

#Generate a sine curve
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0,4*np.pi,np.pi*1000)
y = np.sin(x)

plt.plot(x,y)
plt.show()

raw_input()

plt.plot(x,y*2) #increase amplitude
plt.show()

###################################################################

# Linear Regression
#   - two variables
#   - identify the relationship between the two (if at all)

# What we need
#   n -> number of records
#   sum(x) -> sum of x values
#   sum(y) -> sum of y values
#   sum(x*x) -> sum of squares of x
#   sum(x*y) -> sum of squares of x and y

#   m = (n * (sum(x*y))-(sum(x)*sum(y)))/(n * (sum(x*x)) - (sum(x)^2)
#   y = mx+b
#   b = (sum(y)-m*sum(x))/n

###################################################################

# R value

#   r = sum(xy)/(sqrt(sum(y)^2*sum(y)^2)

# this number ranges from -1 to +1

#A positively correlated data set has a large R value (>0.8)
#A negatively correlated data set has a small R value (<-0.8)



#1/usr/bin/env python

import math
import matplotlib.pyplot as plt

SQRT_2PI = math.sqrt(2.0 * math.pi)

def gaussian(x):
    return math.exp(-0.5*x*x)/SQRT_2PI

def kernel(x,y,h,binpoints):
    bins = [0] * len(binpoints)
    i = 0
    for b in binpoints:
        bins[i] = (float(y)/float(h))*gaussian((b-x)/float(h))
        i += 1
    return bins

filename = 'goals.dat'

years = [] #x-axis
scores = [] #y-axis

for line in file(filename):
    line = line.strip()
    [score, year] = line.split(",")
    if score != 'NA':
        scores.append(float(score))
        years.append(float(year))

binpoints = [0] * (10*len(scores))
low = min(years)
high = max(years)
delta = (high - low) / (len(binpoints) - 1)

b=low
i = 0
while i < len(binpoints):
    binpoints[i] = b
    b += delta
    i += 1

x = 1888 #year that england scored 5 points
y = 5
h = 2

bins = kernel(x,y,h,binpoints)

plt.plot(years, scores,'g+')
plt.plot(binpoints,bins,'b-')
plt.xlabel("Year")
plt.ylabel("Score")
plt.title("England's Score")
plt.show()

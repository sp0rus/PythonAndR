#!/usr/bin/env python

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

n = len(years)
nbins = n * 1
low = min(years)
high = max(years)

binpoints = [0] * nbins
masterbin = [0] * nbins

delta = (high - low) / (nbins - 1)

b = low
i = 0
while b <= high:
    binpoints[i] = b
    b += delta
    i += 1

for i in range(n):
    # I like using 10 the best, the line is smoothed the most and seems to
    # show trends best, 1 is not smoothed much, 3 still seems too messy
    bins = kernel(years[i],scores[i], 10, binpoints)
    for j in range(nbins):
        masterbin[j] += bins[j] # I had "=+" here and could not get the KDE to plot, took forever to find the problem

plt.plot(binpoints,masterbin,'b-')
plt.plot(years, scores,'g-')
plt.xlabel("Year")
plt.ylabel("Score")
plt.title("England's Score")
plt.show()

#!/usr/bin/env python

import matplotlib.pyplot as plt

filename = "presidential_days_in_office.txt"

daysInOffice = []

#loop through the file and assign the presidents term lengths to the list
for line in file(filename):
    line = line.strip()
    parts = line.split("\t")
    daysInOffice.append( int(parts[2]) )

#sort the presidents by length of term    
daysInOffice = sorted(daysInOffice)

#plot the list and show the plot    
plt.plot(daysInOffice)
plt.show()

#input function, allows us to show the next graph
raw_input()

#generate a plot of the cumulative density function
cdf = [0] * len(daysInOffice)
cdf[0] = daysInOffice[0]

i = 1
while i < len(daysInOffice):
    cdf[i] = daysInOffice[i] + cdf[i-1]
    i += 1

plt.plot(cdf, 'r+')
plt.show()

#show both graphs in one
#plt.plot(daysInOffice)
#plt.plot(cdf, 'r')
#plt.show()

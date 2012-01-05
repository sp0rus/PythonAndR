#!/usr/bin/env python

import matplotlib.pyplot as plt

#assign the file to a variable
filename = "Tax_Year_2007_County_Income_Data.csv"

averagegrossincome = []
returns = []
exemptions = []

#assign some variables for use later
i = 0 #counter to skip the first line
counties = 0 #number of counties (not including those with county code 0)

#loop through the file
for line in file(filename):
    #skip the first line
    if i != 0:
        #clean the data and make each line into a list to parse
        curline = line.strip()
        curline = curline.replace("$","")
        curlinelist = curline.split(",")
        
        #append the county's average gross income to the list
        if curlinelist[1] != 0:
            counties = counties + 1
            agi = int(curlinelist[6])
            pop = int(curlinelist[4])
            averagegrossincome.append(agi/pop)
            returns.append(pop)
            exemptions.append(int(curlinelist[5]))
    i = i + 1

#plot the average gross income of the counties
plt.plot(averagegrossincome)
plt.show()

raw_input()

#plot the average gross income of the counties, sorted
sortavegi = sorted(averagegrossincome)
plt.plot(sortavegi)
plt.show()

#compute and plot the CDF
cdf = [0] * len(sortavegi)
cdf[0] = sortavegi[0]

j = 1
while j < len(sortavegi):
    cdf[j] = sortavegi[j] + cdf[j-1]
    j += 1

raw_input()
    
plt.plot(cdf)
plt.show()

raw_input()

# plot the number of returns filed and number of exemptions
plt.plot(returns, exemptions, "r.")
plt.show()

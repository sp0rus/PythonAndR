#!/usr/bin/env python

#assign the file to a variable
filename = "Tax_Year_2007_County_Income_Data.csv"

#assign some variables for use later
i = 0 #counter to skip the first line
hagi = 0 # highest average gross income
lagi = 1000000000000000 # lowest average gross income
allagi = 0 # average gross income of all counties
counties = 0 #number of counties (not including those with county code 0)

#loop through the file
for line in file(filename):
    #skip the first line
    if i != 0:
        #clean the data and make each line into a list to parse
        curline = line.strip()
        curline = curline.replace("$","")
        curlinelist = curline.split(",")
        
        #loop through the current list
        if curlinelist[1] != 0:
            counties = counties + 1
            agi = int(curlinelist[6])
            pop = int(curlinelist[4])
            curavegi = agi/pop
            #compute the highest average gross income
            if curavegi > hagi:
                hagi = curavegi
                hagic = curlinelist[3]
            #compute the lowest average gross income
            if curavegi < lagi:
                lagi = curavegi
                lagic = curlinelist[3]
            #compute the sum of the average gross incomes of all counties to find national average
            allagi = allagi + curavegi
    i = i + 1

#report highest average gross income by county
print "The county with the highest aveage gross income is %s" % (hagic)
#report lowest average gross income by county
print "The county with the lowest average gross income is %s" % (lagic)
#average of all counties by average gross income
print "The average gross income of all counties is $%s" % ((allagi/counties)*1000)

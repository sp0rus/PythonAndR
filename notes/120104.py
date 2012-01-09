filename = "mynewsstory.txt"
story = file(filename).read()
story = story.replace ('.','')
story = story.replace(',','')
#.
#.
#.
story = story.lower()
bagofwords = story.split(' ')

words = {}

for w in bagofwords:
    if w in words:
        words[w] += 1
    else:
        words[w] = 1
mostSeenWordTally = max( words.values() )
mostSeenWord = ""

for w in words:
    if words[w] == mostSeenWordTally:
        mostSeenWord = w
        break
print mostSeenWord


###############################################################################

#JAVA CLASSES

class Bicycle {
    private int gear;
    public int speed;
    
    Bicycle(){
        gear = 1;
        speed = 0;
    }
    int getGear(){ return gear; }
    int getSpeed(){ return speed; }
    void setSpeed( int speed ){ this.speed = speed; }
    void setGear( int gear ) { this.gear = gear; }
    public String toString(){
        return "Gear: " + gear + " Speed: " + speed;
    }
}

#PYTHON CLASSES

class Bicycle:
    def __init__(self):
        self.__gear = 1 #to make something private, prefix with two underscores
        self.speed
    def getGear(self):
        return self.__gear
    def setGear(self, gear):
        self.__gear = gear
    def __str__(self):
        return "Gear: %s Speed %s" %(self.__gear, self.speed)


###############################################################################

#Histograms
#-> Tally of quantized values
#-> binning

import matplotlib.pyplot as plt

plt.hist(grossIncome) # plt.hist(grossIncome, bins=5)
plt.show()

###############################################################################

#Summary Statistics

import math
import matplotlib.pyplot as plt

SQRT2PI = math.sqrt(2*math.pi)

def gaussian(x):
    return math.exp(-o.5*x*x)/SQRT2PI
    
low = -5.0
high = 5.0
nbins = 201
x = [0] * nbins
y = [0] * nbins
delta = (high - low)/(nbins-1)
i = 0
b = low
while b <= high:
    x[i] = b
    y[i] = [gaussian(b)]
    i += 1
    b += delta

plt.plot(x,y)
plt.show()

###############################################################################

#Kernel Density Estimators
#-> Requires a bandwidth parameter

import math
import matplotlib.pyplot as plt

SQRT2PI = math.sqrt(2*math.pi)

def gaussian(x):
    return math.exp(-0.5*x*x)/SQRT2PI

def kernel(x,y,h,binpoints):
    bins = [0] * len(binpoints)
    for i in range(len(binpoints)):
        bins[i] = y * gaussian(((binpoints[i]- x))/float(h))/float(h))
        
#you have x and y data

plt.plot(x,y)
n = len(x)
low = min(x)
high = max(x)
nbins = 10*n
binpoints = [0] * nbins
masterbin = [0] * nbins
delta = (high-low)/(nbins-1)
b = low
i = 0
while b <= high:
    binpoints[i] = b
    b += delta
    i += 1
for i in range(n):
    bins = kernel(x[i],y[i],h,binpoints)
    for j in range(nbins):
        masterbin[j] += bins[j]
plt.plot(binpoints,masterbin)
plt.show()

###############################################################################

#Regular Expressions
#    - A regular expression is a mini-language for describing text
#        - any sort of text that has to hold to a format
#    - a regular expression is a sequence of atoms
#        - an atom at the very smallest is a single character
#        - atoms can be grouped together with parentheses
#        - by default, a regex matches a string if it is true anywhere inside 
#          the string
#        - atoms can be modified
        
#3 Most Common Regex Atom Modifiers

#    -> ? - this atom is optional
#    -> \? - a literal "?"
#    -> * - this is both optional and can be used infinitely
#    -> \* - a literal "*"
#    -> + - this is not optional, may be used infinitely
#    -> \+ - a literal "+"
    
#    color --
#           |--colou?r
#    colour--

#Character classes
#[abc123]

#-> . - match anything
#-> \. - math a period

#    gray--
#         |--gr[ea]y #character class to allow either spelling of the word
#    grey--

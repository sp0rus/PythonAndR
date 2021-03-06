#Python Interpreter
#iPython - another python interpreter, makes accessing libraries like numpy and scipy easier

#Basic Math
#- Compute the square root without the math library
#    sqrt(25) is the same as 25**0.5


#3 Methods for File Reading
#- read() -> reads an entire file as 1 string
#- readline() -> reads a single line as a string
#- readlines() -> reads all the lines, returns a list of strings

for  line in file(filename):
    print line, # comma after print statement means don't add a newline character


#File Writing

fh = file("writeme.txt","w")
fh.write("Hello.\n")
fh.close()

fh = file("writeme.txt","a") # a command prevents file from being overwritten completely, appends to the end
fh.write("Hi again.")
fh.close()

#methods/functions

def name(a,b,c):
    return a + b + c

#quadratic equation    
def quad(a,b,c)
    if a == 0:
        return None
    s = b * b - 4 * a * c
    if s < 0:
        return None
    if s == 0:
        return -b/float(2*a)
    sr = math.sqrt(s)
    return [(-b+sr)/float(2*a),
        (-b-sr)/float(2*a)]
        
#Immutable vs. Mutable datatypes
#- mutable: it can change
#- immutable: it cannot be changed (just replaced)


#- Python always passes values by reference

#Notes
#January 11, 2012

# Basic Probability

p(T) = 1.0 # probability that something is true
p(F) = 0.0 # probability that something is false
p(F) <= p(A) <= p(T) # the probability of A is not completely true or false,
                     #    we end up somewhere between 0.0 and 1.0
p(A && B) = p(A) * p(B) # probability of A and B is their probabilities
                     #    multiplied together
p(A || B) = p(A) + p(B) # probability of A or B is the sum of their
                     #    probabilities

# Bayes' Law

# probability of A, given that we know B is true, is the probability of B, 
#   given that we know a is true, times the probability of A, 
#   divided by the probability of B

p(A|B) = (p(B|A) * p(A))/p(B)

# EXAMPLE

# you are a pharmacutical company that made a new drug
n = 10000 # units of the drug sold
# 1% are sick after using the drug
sickpeople = 100
healthypeople = 9900
# we know how many are predicted to be sick, but not who, individually, is sick
# we develop a test that is 99% accurate in reporting healthy or sick
#   there are two possible errors in the test
#    - false negative
#        - inaccurately identifies healthy person as sick
#        - happens 1% of the time
#    - false positive
#        - inaccurately identifies sick person as healthy
#        - happens 1% of the time
# what is the probability that you are actually the status the test reports?
sickreportedsick = 99
sickreportedhealthy = 1
healthyreportedsick = 99
healthyreportedhealthy = 9801

totalreportedsick = 198
probabilitytestreportedcorrectly = sickreportedsick/totalreportedsick

# back to Bayes' law

# What is the probability that you are sick given that the test returned true?
p(test | sick=T) = 0.99
p(sick) = 0.01
p(test=T) = 0.0192

p(sick | test=T) = (0.99 * 0.01)/0.0192 = 0.5


###############################################################################

# K-means clustering
#   - a technique for finding out what groups are similar to other groups

# 1.   start with random points
# 2.a. evaluate closest centroid for each item
# 2.b. for each cluster, compute the mean. This is the new centroid for
#       this cluster
# 2.c. go back to 2.a. and loop until centroids do not change

# Prim Algorithm
#   - an easier algorithm to start with


###############################################################################

# TWITTER

http://search.twitter.com/search.json

# REST API

http://search.twitter.com/search.json?q=bieber&lang=en

###################

# twitsearch.py

import urllib
import json

term = "bieber"
url = 'http://search.twitter.com/search.json?q='+term+'&lang=en'
document = urllib.urlopen(url).read()

tweets = json.loads(document)

for tweet in tweets['results']:
    print '>>>', tweet['text']

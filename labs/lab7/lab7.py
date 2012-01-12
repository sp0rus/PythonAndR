#!/usr/bin/env python

import sys
import urllib
import json
import matplotlib.pyplot as plt
import time

def getTweets(term):
    document = urllib.urlopen("http://search.twitter.com/search.json?q=" + term + "&lang=en&rpp=100").read()
    tweets = json.loads(document)
    tweet_list = []
    for tweet in tweets['results']:
        tweet_list.append(tweet['text'])
    return tweet_list

def main():
    if (len(sys.argv) > 1):
        term = sys.argv[1]
    else:
        term = "bieber" #raw_input("Please provide a term to search for: ")
    tweets1 = getTweets(term)
    time.sleep(2)
    tweets2 = getTweets(term)
    time.sleep(2)
    tweets3 = getTweets(term)
    time.sleep(2)
    tweets4 = getTweets(term)
    time.sleep(2)
    tweets5 = getTweets(term)
    time.sleep(2)
    tweets6 = getTweets(term)
    
    all_tweets = tweets1 + tweets2 + tweets3 + tweets4 + tweets5 + tweets6
    
    tweet_length = [len(tweet) for tweet in all_tweets]
    
    bins = [0] * 141
    for tl in tweet_length:
        try:
            bins[tl] += 1
        except:
            print tl

    plt.plot(bins)
    plt.show()
    
    return 0

if __name__=='__main__':
    sys.exit(main())

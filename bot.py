"""
a bot that tweets from the collected works of Jean Baudrillard, a sociologist,
critic, and philosopher of modern media, communications, and technology. I
understand that by creating this bot, I engage in the very simulacrum that 
Baudrillard warned us about. But it is in this act that I engage a critical 
duality: to seduce others through the work of a dead philosopher on a medium
he would condemn and be disgusted by. A symbolic exchange that I believe the
medium could never return to Baudrillard himself. So let it be known by this
simulacrum: Baudrillard warned us.

author: Jean Baudrillard
editor: elias g
version: 1981

SIMULATE, THIS.
"""

# the books supported so far
from output.PerfectCrime import PERFECT_CRIME
from output.Seduction import SEDUCTION
from baudrillardSecret import (CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN,
                               ACCESS_SECRET)

import arrow
from nltk import WhitespaceTokenizer
import random
import tweepy as ty


def setTwitterAuth():
    """
    obtains authorization from twitter API
    """
    # sets the auth tokens for twitter using tweepy
    auth = ty.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = ty.API(auth)
    return api


def getQuote():
    randInt = random.randint(0, 1)
    if randInt == 0:
        quote = SEDUCTION[random.randint(0, len(SEDUCTION) - 1)]
        cite = "Seduction"
    elif randInt == 1:
        quote = PERFECT_CRIME[random.randint(0, len(PERFECT_CRIME) - 1)]
        cite = "The Perfect Crime"
    return quote, cite


def tweet(api, quote, cite):
    print("in tweet")
    citeTweet = "{} - {}"
    ellipsisTweet = "{}..."
    maxSize = 140 - len(cite) - 3
    ellipsisSize = 140 - 3
    if len(quote) > maxSize:
        print("in the first if check")
        sentence = WhitespaceTokenizer().tokenize(quote)
        print(sentence)
        sentenceSize = len(sentence)
        i = 0
        done = False
        tweets = []

        while not done:
            print("in main while")
            newTweet = ""

            while ((len(newTweet + " " + sentence[i]) < ellipsisSize)
                   and not done):
                print("in inner while")
                if i != sentenceSize - 7:
                    newTweet += " " + sentence[i]
                    i += 1
                else:
                    done = True
            if not done:
                tweets.append(ellipsisTweet.format(newTweet))
            else:
                tweets.append(ellipsisTweet.format(newTweet))
                newTweet = ""
                while i != sentenceSize:
                    newTweet += " " + sentence[i]
                    i += 1
                tweets.append(citeTweet.format(newTweet, cite))
        while tweets:
            tweet = tweets.pop()
            print(tweet)
    else:
        print(citeTweet.format(quote, cite))


if __name__ == "__main__":
    api = setTwitterAuth()
    quote, cite = getQuote()
    tweet(api, quote, cite)

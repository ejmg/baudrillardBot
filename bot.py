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
    # want to cite each quote, the three is for a space, dash, & another space
    maxLength = 140 - len(cite) - 3
    # size for a tweet that has an ellipsis
    ellipsisLength = 140 - 3
    if len(quote) >= maxLength:
        tweet = quote[-maxLength::]
        api.update_status("{} - {}".formate(tweet, cite))
        quote = quote[:len(quote) - maxLength:]

        while quote >= ellipsisLength:
            tweet = quote[-ellipsisLength::]
            api.update_status("{}...".format(tweet))
            quote = quote[:len(quote) - ellipsisLength:]

    else:
        api.update_status("{} - {}".format(quote, cite))


if __name__ == "__main__":
    api = setTwitterAuth()
    quote, cite = getQuote()
    tweet(api, quote, cite)

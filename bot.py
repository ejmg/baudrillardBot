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
from output import (Seduction, PerfectCrime)
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


if __name__ == "__main__":
    api = setTwitterAuth()
    

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
from txtoutput.PerfectCrime import PERFECT_CRIME
from txtoutput.Seduction import SEDUCTION
from baudrillardSecret import (CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN,
                               ACCESS_SECRET)
from nltk import WhitespaceTokenizer
from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap
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
    """
    gets a quote from the dictionaries provided. So far only Seduction and
    The Perfect Crime are included.
    """
    randInt = random.randint(0, 1)
    if randInt == 0:
        quote = SEDUCTION[random.randint(0, len(SEDUCTION) - 1)]
        cite = "Seduction"
    elif randInt == 1:
        quote = PERFECT_CRIME[random.randint(0, len(PERFECT_CRIME) - 1)]
        cite = "The Perfect Crime"
    return quote, cite


def tweetTxt(api, quote, cite):
    """
    generates a text only tweet of a baudrillard quote, or a series of tweets
    if over the limit.

    CURRENTLY NOT USED BECAUSE OF THE UNFORTUNATE WEIRD FORMATTING CAUSED
    BY THE WORD LIMIT AND AN INABILITY TO CREATE A SATISFACTORY SOLUTION
    WITH MY SKILLS.

    that said, the function works just fine.
    """
    citeTweet = "{} - {}"
    ellipsisTweet = "{}..."
    maxSize = 140 - len(cite) - 3
    ellipsisSize = 140 - 3
    if len(quote) > maxSize:
        sentence = WhitespaceTokenizer().tokenize(quote)
        print(sentence)
        sentenceSize = len(sentence)
        i = 0
        done = False
        tweets = []

        while not done:
            newTweet = ""

            while ((len(newTweet + " " + sentence[i]) < ellipsisSize)
                   and not done):
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
            api.update_status(tweet)
    else:
        api.update_status(citeTweet.format(quote, cite))


def tweetImage(api, quote, cite):
    """
    tweets the quote passed and an accompanying image with said quote. If
    the quote is shorter than maxSize, it is tweeted in full with citation.
    Otherwise, what fits is shown with a trailing ellipsis
    """
    shortTweet = "{} - {}"
    longTweet = "{}..."
    maxSize = 140 - len(cite) - 3
    longSize = 140 - 3
    createImage(quote)
    if len(quote) > maxSize:
        words = WhitespaceTokenizer().tokenize(quote)
        tweet = ""
        done = False
        i = 0
        while not done:
            if (len(tweet) + 1 + len(words[i])) < longSize:
                tweet += words[i] + " "
                i += 1
            else:
                tweet = tweet[:-1:]
                done = True
        api.update_with_media("../baudrillardBot/draw/output.png",
                              status=longTweet.format(tweet))

    else:
        api.update_with_media("../baudrillardBot/draw/output.png",
                              status=shortTweet.format(quote, cite))


def createImage(quote):
    """
    creates an image containing the quote passed to it on one of 4 template
    backgrounds

    SHOUT OUT TO GABRIELLE ORTMAN FOR THIS IDEA (it is much prettier/graceful
    than the pure text solution i was implementing)
    """
    randInt = random.randint(0, 3)
    img = Image.open("../baudrillardBot/images/{}.png".format(str(randInt)))
    x, y = img.size
    draw = ImageDraw.Draw(img)
    fontPath = os.path.abspath("/usr/share/fonts/truetype/liberation/"
                               "LiberationMono-Italic.ttf")
    font = ImageFont.truetype(fontPath, 16)
    lines = textwrap.wrap(quote, width=45)
    y_text = y
    for line in lines:
        draw.text((x / 7, y_text / 5), line, (0, 0, 0), font=font)
        y_text += 100
    img.save("../baudrillardBot/draw/output.png")


if __name__ == "__main__":
    api = setTwitterAuth()
    quote, cite = getQuote()
    # tweetTxt(api, quote, cite)
    tweetImage(api, quote, cite)

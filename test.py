from txtoutput.PerfectCrime import PERFECT_CRIME
from txtoutput.Seduction import SEDUCTION
from baudrillardSecret import (CONSUMER_TOKEN, CONSUMER_SECRET, ACCESS_TOKEN,
                               ACCESS_SECRET)
from nltk import WhitespaceTokenizer
import random
from PIL import Image, ImageDraw, ImageFont
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
    randInt = random.randint(0, 1)
    if randInt == 0:
        quote = SEDUCTION[random.randint(0, len(SEDUCTION) - 1)]
        print(quote)
        cite = "Seduction"
    elif randInt == 1:
        quote = PERFECT_CRIME[random.randint(0, len(PERFECT_CRIME) - 1)]
        print(quote)
        cite = "The Perfect Crime"
    return quote, cite


def tweetTxt(quote, cite):
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


def tweetImage(api, quote, cite):
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
    randInt = random.randint(0, 3)
    img = Image.open("../baudrillardBot/images/{}.png".format(str(randInt)))
    x, y = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../../../../../usr/share/fonts/truetype/"
                              "liberation/LiberationMono-Italic.ttf", 16)
    lines = textwrap.wrap(quote, width=45)
    y_text = y
    for line in lines:
        draw.text((x / 7, y_text / 5), line, (0, 0, 0), font=font)
        y_text += 100
    img.save("../baudrillardBot/draw/output.png")



if __name__ == "__main__":
    api = setTwitterAuth()
    quote, cite = getQuote()
    # tweetTxt(quote, cite)
    tweetImage(api, quote, cite)

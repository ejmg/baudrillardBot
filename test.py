from txtoutput.PerfectCrime import PERFECT_CRIME
from txtoutput.Seduction import SEDUCTION
from nltk import WhitespaceTokenizer
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap

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


def tweet(quote, cite):
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
    quote, cite = getQuote()
    img = Image.open("../baudrillardBot/image/scratchPaper.png")
    x, y = img.size
    print(str(x))
    print(str(y))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("../../../../../usr/share/fonts/truetype/"
                              "freefont/FreeMonoBold.ttf", 16)
    lines = textwrap.wrap(quote, width=40)
    y_text = y
    for line in lines:
        fx, fy = font.getsize(line)
        draw.text(((fx - x) / 5, y_text/4), line, (0, 0, 0), font=font)
        y_text += y
    img.save("../baudrillardBot/draw/sample.png")

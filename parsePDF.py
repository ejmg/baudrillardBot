"""
this file attempts to extract text from pdf files and saves it as a text file.
given the nature of these pdfs, the various methods will probably all be
hard coded to the specific pdf, so expect nothing pretty.

This script is also just as much about teaching myself how to get text from
pdfs, so that should explain why I'm doing this so ~meticulously~

author: elias g
version: 11.30.16
"""
import PyPDF2 as PDF

def extractSeduction():
    

def extractPerfectCrime():
    start = 5
    end = 79
    file = open("../baudrillardBot/rawtxt/Perfect-Crime.txt", "w")

    pdf = open("../baudrillardBot/pdfs/The-Perfect-Crime.pdf", "rb")
    reader = PDF.PdfFileReader(pdf)

    for page in range(start, end):
        text = reader.getPage(page).extractText()
        text = text.replace("\n", "")
        file.write(text)
    file.close()

if __name__ == "__main__":
    extractPerfectCrime()

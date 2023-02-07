import textwrap
from PIL import Image, ImageFont, ImageDraw
import os
import csv
import pandas
import re
import textwrap

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# define quote text and author name columns on csv file
colnames = ['quote', 'author']

# Change quotes.csv with your csv file name
data = pandas.read_csv('quotes.csv', names=colnames)

quotes = data.quote.tolist()
authors = data.author.tolist()

    
for num in range(len(quotes)):
    quote_text1 = quotes[num]
    quote_author1 = authors[num]
    
    # Create a new image with a transparent background
    bg_image = Image.new('RGBA', (7632, 6480))
    quote_image = ImageDraw.Draw(bg_image)

    # Load the fonts for the quote and author text
    quote_font = ImageFont.truetype('Quote.ttf', 700)
    author_font = ImageFont.truetype('Quote.ttf', 400)
    qmarks_font = ImageFont.truetype('Oswald.ttf', 1500)

    # Wrap the quote text and author text to a maximum width
    quote_text = textwrap.wrap(quote_text1, width=26)
    quote_author = textwrap.wrap(quote_author1, width=18)

    # Draw the openning quotation mark
    quote_image.text((150, 50), "“", (241, 208, 10), font=qmarks_font)

    # Draw each line of the quote text
    offset = 1200
    for ix in quote_text:
        quote_image.text((250, 150+offset), ix,
                         (234, 234, 234), font=quote_font)
        offset += 600

    # Draw the closing quotation marks
    quote_image.text((6700, offset-200), "”", (241, 208, 10), font=qmarks_font)

    # Draw each line of the author text
    offset += 700
    for ix in quote_author:
        quote_image.text((6300-(170*len(ix)), 150+offset), ix,
                         (234, 234, 234), font=author_font)
        offset += 350

    # Save the quote image to the results folder with a unique filename
    bg_image.save("results/"+str(num+1)+".png")
    print("|| results/"+str(num+1)+".png")

print("||---------------- FINISH!!")

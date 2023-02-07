from textwrap import wrap
from tkinter import W
from bs4 import BeautifulSoup
from itertools import zip_longest
import requests,csv,os,re


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Initialize two lists to store quotes and authors
quotes=[]
authors=[]

# Loop through 1 to 2 pages of quotes on the website
for number_page in range(1,2): 

    result = requests.get(f"https://www.azquotes.com/top_quotes.html?p={number_page}")
    src=result.content
    soup= BeautifulSoup(src,"lxml")
    
    # Get Quotes text
    quote = soup.find_all("a",{"class":"title"})
    # Get Authors
    author= soup.find_all("div",{"class":"author"})
    
    
    for i in range(len(quote)):
        # If the quote length is <= 150 char, it will be ignored to prevent 
        # problems while designing the image
        if(len(quote[i].text)<=150):    
            # Remove unwanted characters from text
            qq=re.sub(r'[’“”]', '', quote[i].text)
            aa=re.sub(r'[’“”]', '', author[i].text.strip())
            quotes.append(qq)
            authors.append(aa)
    
        
# Export data to csv file
file_list=[quotes,authors]
exported= zip_longest(*file_list)
myfile=open("quotes.csv","w",newline='')
wr = csv.writer(myfile)
wr.writerows(exported)


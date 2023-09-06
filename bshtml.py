# Python web scraping
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


# function to fetch out Book name and Author name
def bookNamesfromAma(fnstr):
    booklistname=[]     #Book names list
    authername=[]       #Author names list
    for i in range(20):
        if i%2==0:
            booklistname.append(fnstr[i].text)
        else:
            authername.append(fnstr[i].text)
    return booklistname, authername

# Function to fetch out Number of stars 
def starsofbook(s):
    strsli=list()       #list of stars
    for i in range(10):
        strofstars=all_stars[i].text
        strsli.append(strofstars[:4])
    return strsli

# Function to fetch out price of books
def priceofBooks(s):
    priceofbooks=list() #list of price of various books
    for i in range(10):
        priceofbooks.append(s[i].text)
    return priceofbooks

# Function to fetch out link of books
def booklinks(s):
    defPath='https://www.amazon.in/'
    linkslist=list()
    for i in range(0,40,4):
        linkslist.append(defPath+s[i]['href'])
    return linkslist

# Book image
def bookimages(s):
    imageslist=list()
    for i in range(10):
        imageslist.append(s[i]['src'])
    return imageslist

url="https://www.amazon.in/gp/bestsellers/books/" #url of site
r=requests.get(url)     #fetching out web page using requests module
print(r.status_code)    #Checking out status of the site    200
page_con=r.text         #Extracting text 
soup=BeautifulSoup(page_con,'html.parser') #using beautiful soup 
print(soup.title.text)  #fetching out title of the url page

#Fetching book name and author name
book_names=soup.find_all('div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y') 
res1,res2=bookNamesfromAma(book_names) 

#Fetching number of stars
all_stars=soup.find_all('span', class_='a-icon-alt')
res3= starsofbook(all_stars) 

#Fetching price of books
all_price=soup.find_all('span',class_='a-size-base')
res4=priceofBooks(all_price)

# Fetching links of books on amazon
all_links=soup.find_all('a',class_='a-link-normal')
res5=booklinks(all_links)

# Fetching image of books src link
all_images=soup.find_all('img', class_='a-dynamic-image p13n-sc-dynamic-image p13n-product-image')
res6=bookimages(all_images)

# Creating dictionary 
dict = {'Book Name': res1, 'Author Name': res2,'Number of stars':res3,'Price':res4,'Links': res5, 'Image':res6}

# Creating dataframe of dictionary using pandas module
df = pd.DataFrame(dict)
print(df)

# Creating csv file
df.to_json('TopBestSellersonAmazon.json')
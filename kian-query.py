""" 
from pyquery import PyQuery as pq
name = input("What do you want to search?")
url="https://www.amazon.com/s?k={name}&ref=nb_sb_noss"
response = pq(url=url.format(name=name))
print(response)"""

import requests, re
from bs4 import BeautifulSoup

query = input("What product do you want to search for?")
#URL = 'https://www.etsy.com/search/?query=' + query
URL = 'https://www.amazon.com/s?k=' + query + '&ref=nb_sb_noss_2'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
open("html.txt", "w").write(str(soup))
#print(soup)
"""
for line in s.split('\n'):
    if 'elephant' in line:
        print(line)
"""
with open('html.txt', 'r') as f:
    for line in f.readlines():
        if 'Amazon' in line:
            print(line)
"""
x = 0
while True:
 try: 
    from googlesearch import search 
 except ImportError:  
    print("No module named 'google' found") 
 query = input("Google: ")
 x = 1
 y = 2
 for j in search(query, tld="co.in", num=10, stop=1, pause=2):
   req = requests.get(j)
   soup = BeautifulSoup(req.text, "lxml")
   title = soup.title.string
   if title == "403 Forbidden":
     title = "Blocked Title"
   if title == "Sorry! Something went wrong!":
     title = "Error: Title Not Found"
   print("")
   print(title)
   print(j) 
   print("")
   x += 1
 print("")
 print("|--------------------------------------------------------------------------------------------|")
 print("")
 search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0) """
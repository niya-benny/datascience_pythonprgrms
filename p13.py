#web scraping in action

from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re


r=urllib.request.urlopen('https://www.wikipedia.org/').read()
soup=BeautifulSoup(r,'html.parser')

#scrap a webpage

print(soup.prettify()[:100])

print("\n")

for link in soup.find_all('a'):
    print(link.get('href'))

print("\n")

print(type(link))

print(soup.get_text())

print("\n")

print(soup.prettify()[0:1000])

for link in soup.find_all('a',attrs={'href':re.compile('http')}): #It filters these <a> tags to only include those whose href attribute matches the regular expression re.compile('http').
    print(link)

print("\n")

file=open('parsed_data.txt', 'w')
for link in soup.find_all('a',attrs={'href':re.compile('http')}):
    soup_link=str(link)  #Converts each <a> tag to a string
    print(soup_link)
    file.write(soup_link) #Writes that string into the file parsed_data.txt.


file.flush()
file.close()

#asynchronous web scraping (without waiting for the response for each request), reduces the CPU idle time

#aiohttp, asyncio libraries

import csv
import aiohttp    #for making asynchronous http requests.
import asyncio      #for asynchronous programming in python
import nest_asyncio
nest_asyncio.apply()

async def scrape_and_save_links(text):
    soup=BeautifulSoup(text,'html.parser')
    file=open('csv_file','a',newline='')
    writer=csv.writer(file,delimiter=',')

    for link in soup.find_all('a',attrs={'href':re.compile('^http')}):
        link=link.get('href')
        writer.writerow([link])
    file.close()

async def fetch(session,url):
    try:
        async with session.get(url) as response:
            text=await response.text()
            task=asyncio.create_task(scrape_and_save_links(text))
            await task
    except Exception as e:
        print(str(e))

 #await lets your program pause at that line only for that coroutine, while other parts continue.

async def scrap(urls):
    tasks=[]
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session,url))
        await asyncio.gather(*tasks)   #runs all tasks concurrently


urls=['https://www.python.org/','https://www.linkedin.com/']
asyncio.run(scrap(urls=urls))









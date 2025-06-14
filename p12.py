
#Web scraping
import requests

#get method
response=requests.get("https://www.python.org")
print(response)

#Headers (all the meta data)
print(response.headers)

#content types
print(response.headers['Content-Type'])

#Body/Content
print(response.content)


#compare sequences
import difflib
flines='Helo. How r u? I am Fine'
glines='How r u , niya? I am doing well'

d=difflib.Differ()
diff=d.compare(flines,glines)

for line in diff:
    print(line)


#BeautifulSoup
import sys
from bs4 import BeautifulSoup
#Objects in BeautifulSoup

#BeautifulSoup Objects

our_html_document = '''
<html><head><title>IoT Articles</title></head>
<body>
<p class='title'><b>2018 Trends: Best New IoT Device Ideas for Data Scientists and Engineers</b></p>

<p class='description'>It’s almost 2018 and IoT is on the cusp of an explosive expansion. In this article, I offer you a listing of new IoT device ideas that you can use...
<br>
<br>
It's almost 2018 and IoT is on the cusp of an explosive expansion. In this article, I offer you a listing of new IoT device ideas that you can use to get practice in designing your first IoT applications.
<h1>Looking Back at My Coolest IoT Find in 2017</h1>
Before going into detail about best new IoT device ideas, here’s the backstory. <span style="text-decoration: underline;"><strong><a href="http://bit.ly/LPlNDJj">Last month Ericsson Digital invited me</a></strong></span> to tour the Ericsson Studio in Kista, Sweden. Up until that visit, <a href="http://www.data-mania.com/blog/m2m-vs-iot/">IoT</a> had been largely theoretical to me. Of course, I know the usual mumbo-jumbo about wearables and IoT-connected fitness trackers. That stuff is all well and good, but it’s somewhat old hat – plus I am not sure we are really benefiting so much from those, so I’m not that impressed.

It wasn’t until I got to the Ericsson Studio that I became extremely impressed by how far IoT has really come. Relying on the promise of the 5g network expansion, IoT-powered smart devices are on the cusp of an explosive growth in adoption. It was Ericsson’s Smart Car that sent me reeling:<a href="bit.ly/LPlNDJj"><img class="aligncenter size-full wp-image-3802" src="http://www.data-mania.com/blog/wp-content/uploads/2017/12/new-IoT-device-ideas.jpg" alt="Get your new iot device ideas here" width="1024" height="683" /></a>

This car is connected to Ericsson’s Connected Vehicle Cloud, an IoT platform that manages services for the Smart Cars to which it’s connected. The Volvo pictured above acts as a drop-off location for groceries that have been ordered by its owner.

To understand how it works, imagine you’re pulling your normal 9-to-5 and you know you need to grab some groceries on your way home. Well, since you’re smart you’ve used Ericsson IoT platform to connect your car to the local grocery delivery service (<a href="http://mat.se/">Mat.se</a>), so all you need to do is open the Mat.se app and make your usual order. Mat.se automatically handles the payment, grocery selection, delivery, and delivery scheduling. Since your car is IoT-enabled, Mat.se issues its trusted delivery agent a 1-time token to use for opening your car in order to place your groceries in your car for you at 4:40 pm (just before you get off from work).

To watch some of the amazing IoT device demos I witnessed at Ericsson Studio, make sure to go <span style="text-decoration: underline;"><strong><a href="http://bit.ly/LPlNDJj">watch the videos on this page</a></strong></span>.
<h1>Future Trends for IoT in 2018</h1>
New IoT device ideas won’t do you much good unless you at least know the basic technology trends that are set to impact IoT over the next year(s). These include:
<ol>
 	<li><strong>Big Data</strong> &amp; Data Engineering: Sensors that are embedded within IoT devices spin off machine-generated data like it’s going out of style. For IoT to function, the platform must be solidly engineered to handle big data. Be assured, that requires some serious data engineering.</li>
 	<li><strong>Machine Learning</strong> Data Science: While a lot of IoT devices are still operated according to rules-based decision criteria, the age of artificial intelligence is upon us. IoT will increasingly depend on machine learning algorithms to control device operations so that devices are able to autonomously respond to a complex set of overlapping stimuli.</li>
 	<li><strong>Blockchain</strong>-Enabled Security: Above all else, IoT networks must be secure. Blockchain technology is primed to meet the security demands that come along with building and expanding the IoT.</li>
</ol>
<h1>Best New IoT Device Ideas</h1>
This listing of new IoT device ideas has been sub-divided according to the main technology upon which the IoT devices are built. Below I’m providing a list of new IoT device ideas, but for detailed instructions on how to build these IoT applications, I recommend the <a href="https://click.linksynergy.com/deeplink?id=*JDLXjeE*wk&amp;mid=39197&amp;murl=https%3A%2F%2Fwww.udemy.com%2Ftopic%2Finternet-of-things%2F%3Fsort%3Dhighest-rated">IoT courses on Udemy</a> (ß Please note: if you purchase a Udemy course through this link, I may receive a small commission), or courses that are available at <a href="http://www.skyfilabs.com/iot-online-courses">SkyFi</a> and <a href="https://www.coursera.org/specializations/iot">Coursera</a>.
<h2>Raspberry Pi IoT Ideas</h2>
Using Raspberry Pi as open-source hardware, you can build IoT applications that offer any one of the following benefits:
<ol>
 	<li>Enable built-in sensing to build a weather station that measures ambient temperature and humidity</li>
 	<li>Build a system that detects discrepancies in electrical readings to identify electricity theft</li>
 	<li>Use IoT to build a Servo that is controlled by motion detection readings</li>
 	<li>Build a smart control switch that operates devices based on external stimuli. Use this for home automation.</li>
 	<li>Build a music playing application that enables music for each room in your house</li>
 	<li>Implement biometrics on IoT-connected devices</li>
</ol>
<h2>Arduino IoT Ideas</h2>
There are a number of new IoT device ideas that deploy Arduino as a microcontroller. These include:
<ol>
 	<li>Integrate Arduino with Android to build a remote-control RGB LED device.</li>
 	<li>Connect PIR sensors across the IoT to implement a smart building.</li>
 	<li>Build a temperature and sunlight sensor system to remotely monitor and control the conditions of your garden.</li>
 	<li>Deploy Arduino and IoT to automate your neighborhood streetlights.</li>
 	<li>Build a smart irrigation system based on IoT-connected temperature and moisture sensors built-in to your agricultural plants.</li>
</ol>
[caption id="attachment_3807" align="aligncenter" width="300"]<a href="bit.ly/LPlNDJj"><img class="wp-image-3807 size-medium" src="http://www.data-mania.com/blog/wp-content/uploads/2017/12/IMG_3058-300x295.jpg" alt="" width="300" height="295" /></a> An IoT Chatbot Tree at the Ericsson Studio[/caption]
<h2>Wireless (GSM) IoT Ideas</h2>
Several new IoT device ideas are developed around the GSM wireless network. Those are:
<ol>
 	<li>Monitor soil moisture to automate agricultural irrigation cycles.</li>
 	<li>Automate and control the conditions of a greenhouse.</li>
 	<li>Enable bio-metrics to build a smart security system for your home or office building</li>
 	<li>Build an autonomously operating fitness application that automatically makes recommendations based on motion detection and heart rate sensors that are embedded on wearable fitness trackers.</li>
 	<li>Build a healthcare monitoring system that tracks, informs, and automatically alerts healthcare providers based on sensor readings that describe a patients vital statistics (like temperature, pulse, blood pressure, etc).</li>
</ol>
<h2>IoT Automation Ideas</h2>
Almost all new IoT device ideas offer automation benefits, but to outline a few more ideas:
<ol>
 	<li>Build an IoT device that automatically locates and reports the closest nearby parking spot.</li>
 	<li>Build a motion detection system that automatically issues emails or sms messages to alert home owners of a likely home invasion.</li>
 	<li>Use temperature sensors connected across the IoT to automatically alert you if your home windows or doors have been left open.</li>
 	<li>Use bio-metric sensors to build a smart system that automate security for your home or office building</li>
</ol>
To learn more about IoT and what’s happening on the leading edge, be sure to pop over to Ericsson’s Studio Tour recap and <span style="text-decoration: underline;"><strong><a href="http://bit.ly/LPlNDJj">watch these videos</a></strong></span>.

<em>(I captured some of this content on behalf of DevMode Strategies during an invite-only tour of the Ericsson Studio in Kista. Rest assure, the text and opinions are my own</em>)
<p class='description'>...</p>
'''


our_soup_object=BeautifulSoup(our_html_document,'html.parser')
print(our_soup_object)
print("\n")
print(our_soup_object.prettify()[0:300])


#tag object
#tag names
print("\n")
soup_object=BeautifulSoup('<h1 attribute_1 = "Heading level 1">Future Trends for IOT in 2018</h1>', 'html.parser')
tag=soup_object.h1
print(tag)
print(type(tag))
print(tag.name)

tag.name="heading 1"
print(tag)

#tag attributes
soup_object=BeautifulSoup('<h1 attribute_1 = "Heading level 1">Future Trends for IOT in 2018</h1>', 'html.parser')
tag = soup_object.h1
print(tag)

print(tag['attribute_1'])
print(tag.attrs) #print all attributes

tag['aatribute_2']="heading level 111"
print(tag.attrs)
print(tag)

del tag['aatribute_2']
print(tag.attrs)


#navigating a parse tree using tags

our_soup_object=BeautifulSoup(our_html_document,'html.parser')
print(our_soup_object.head)

print(our_soup_object.title)

print(our_soup_object.body.b)

print(our_soup_object.li)

print(our_soup_object.a)

#navigable string object

import sys
soup_object=BeautifulSoup('<h1 attr_1="Heading level 1">Future trends for iot in 2018</h1>', 'html.parser')
tag=soup_object.h1
print(type(tag))

print(tag.name)
print(tag.string)

print(type(tag.string))
our_navigatable_string=tag.string
print(our_navigatable_string)

our_navigatable_string.replace_with('NaN')
print(tag.string)

our_soup_object=BeautifulSoup(our_html_document,'html.parser')
for string in our_soup_object.stripped_strings:
    print(repr(string)) #print representation of the strings\


#access parent tag objects within a parse tree

first_link=our_soup_object.a #a->anchor tag
print(first_link)

print(first_link.parent)

print(first_link.string)


#data parsing

from bs4 import BeautifulSoup
import urllib
import urllib.request
import re #regular expression library
with urllib.request.urlopen('https://raw.githubusercontent.com/BigDataGal/Data-Mania-Demos/master/IoT-2018.html') as response:
     html=response.read()
#'with' ensures the connection is properly closed after reading.
soup=BeautifulSoup(html, 'html.parser')
print(type(soup))

print(soup.prettify()[0:100]) #'prettify()' returns a nicely formatted (indented) version of the HTML.

text_only=soup.get_text() # 'get_text()' strips all HTML tags and returns only the visible text content on the page.
print(text_only)

#searching and retrieving

print(soup.find_all('li'))

print(soup.find_all(id='link 7'))

print(soup.find_all('ol'))

print(soup.find_all(['ol','b']))

t=re.compile('t')
for tag in soup.find_all(t):  #finds all tags whose name contain the letter 't'
    print(tag.name)

print("\n")

for tag in soup.find_all(True): #  to print every tag name in the document
    print(tag.name)

print("\n")

for link in soup.find_all('a'): #all links in href
    print(link.get('href'))

print("\n")

print(soup.find_all(string=re.compile('data'))) #all strings that contain 'data'
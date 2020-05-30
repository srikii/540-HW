"""python script to read a URL and count the number of unique URL on the website.
    author: srikanth."""

import socket
import urllib.request
import urllib
import re   

def searchlink():
    i=set()
    url= input("enter URL: ")
    #url=https://www.tutorialspoint.com/python3/python_reg_expressions.htm
    fhand = urllib.request.urlopen(url).read().lower()   
    x = re.findall(b'"(http|https?://.*?)"', fhand)
    #x= re.findall(b'"(http[s]?://.*?)"',fhand)
    for link in x:
        i.add(link.decode())
    print(i)
    print("\n no of unique links=", len(i)) 

searchlink()
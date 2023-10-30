# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 20:12:29 2023

@author: karam
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
processDepth = int(input('Enter Count - '))
position = int(input('Enter position - '))
position = position - 1

# Development prescripts
# Sample Data
# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# processDepth = 7
# position = 17
# Actual Data
# url = "http://py4e-data.dr-chuck.net/known_by_Verity.html"

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

nextLink = tags[position].get('href', None) #initiate links
rePattern = "r'by_(.*)\.html$'"
thirdNameList = re.findall(r'by_(.*)\.html$', url)

nextTags = tags

for process in range(processDepth):

    nextLink = nextTags[position].get('href', None) #initiate links
    nextHTML = urllib.request.urlopen(nextLink, context=ctx).read()
    nextSoup = BeautifulSoup(nextHTML, 'html.parser')
    nextTags = nextSoup('a')
    nextThirdName = re.findall(r'by_(.*)\.html$', nextLink)
    thirdNameList = thirdNameList + nextThirdName
    
print(thirdNameList)
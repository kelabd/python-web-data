# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 18:45:14 2023

@author: karam
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

# Sample Data
# url = "http://py4e-data.dr-chuck.net/comments_42.html"
# Actual Data
# url = "http://py4e-data.dr-chuck.net/comments_1923294.html"

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
commentSum = 0
for tag in tags:

    commentCount = re.findall(">(.*)<", tag.decode())
    commentSum = commentSum + int(commentCount[0])

print(commentSum)
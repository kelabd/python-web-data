# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 01:38:14 2023

@author: karam
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Sample Data
# address = "http://py4e-data.dr-chuck.net/comments_42.xml"

# Actual Data
# address = "http://py4e-data.dr-chuck.net/comments_1923296.xml"

address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
result = tree.findall('.//count')
nResults = len(result)
print('Count:', nResults)

commentSum = 0
for comment in range(nResults):
    commentSum = commentSum+ int(result[comment].text)
print('Sum:', commentSum)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:14:15 2023

@author: karam
"""
import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Sample Data
# address = "http://py4e-data.dr-chuck.net/comments_42.json"

# Actual Data
# address = "http://py4e-data.dr-chuck.net/comments_1923297.json"

address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count:', len(info))

commentCount = 0
for item in info['comments']:
    if 'note' in item: continue
    # print('name', item['name'])
    # print('count', item['count'])
    commentCount = commentCount + item['count']
print('Sum -', commentCount)
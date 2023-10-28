# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:59:15 2023

@author: karam
"""

import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# sample cmd
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# actual cmd
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

extraction_keywords = ['Last-Modified', 'ETag', 'Content-Length', 'Cache-Control', 'Content-Type']

# Create a results dictionary with empty lists as values for each keyword
results_dict = {keyword: [] for keyword in extraction_keywords}

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    input_string = data.decode()
    
    # extract the keywords
    for extraction_keyword in extraction_keywords:
    
        pattern = r'{}: (.*)'.format(extraction_keyword)

        # Use re.findall() to extract the value
        result = re.findall(pattern, input_string)
        
        if result:
            results_dict[extraction_keyword].extend(result)
    
mysock.close()    
    
for keyword, result in results_dict.items():
    print(keyword, result)


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:27:46 2023

@author: karam
"""

import re

# Specify the file path
file_path = 'regex_sum_42.txt'

# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
    
print(file_contents)


result_list = re.findall('[0-9]+', file_contents)
int_list = [int(x) for x in result_list]

result_sum = sum(int_list)
print(result_sum)

#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import sys

inputfile = sys.argv

with open(inputfile[1]) as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for tag in soup.find_all('div', {"class": ["data-column", "column-accountId", "ng-star-inserted"]}):
    if (len(tag) > 0):
        email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", tag.text)
        for item in email:
            print(item)
        

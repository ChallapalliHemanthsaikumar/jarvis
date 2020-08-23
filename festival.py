 

import requests
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import re
import base64
import texteditor

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "https://www.officeholidays.com/countries/india/2020"
response = request(target_url)
result = texteditor.open(filename="write.txt",text=str(response.content))

parsed_html =  BeautifulSoup(response.content, 'html.parser').encode("utf-8")
print(parsed_html)
# table = re.match(r'<table.*?</table>', parsed_html,flags=0)
# try: 
#     for table in tables_list:
#         print(table)
# except:
#     pass     
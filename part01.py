# %%

from bs4 import BeautifulSoup
import requests
import csv
 
# %%
URL = 'https://en.wikipedia.org/wiki/Main_Page'
response = requests.get(URL)

response.status_code
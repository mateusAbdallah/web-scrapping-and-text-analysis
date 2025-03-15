# %%

from bs4 import BeautifulSoup
import requests
import csv
 
# %%

URL = 'https://en.wikipedia.org'
response = requests.get(URL)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

# %%

# paragraphs = soup.find_all('p')
# links = [for a in paragraphs]

# %%

links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/wiki/')]
unique_a = set(links)
list_unique_a = list(unique_a)

# %%

with open("wiki_paragraphs.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'first_paragraph'])


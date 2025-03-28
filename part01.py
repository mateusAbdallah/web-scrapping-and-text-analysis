# %%
from bs4 import BeautifulSoup
import requests
import csv
import time
 
# %%
BASE_URL = 'https://en.wikipedia.org'
response = requests.get(BASE_URL)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

# %%
links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/wiki/')]
unique_a = set(links)
list_unique_a = list(unique_a)

# %%
with open("data/wiki_paragraphs.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'first_paragraph'])

    for link in list_unique_a[:100]:
        page_url = BASE_URL + link
        page_response = requests.get(page_url)

        if page_response.status_code == 200:
            page_soup = BeautifulSoup(page_response.content, 'html.parser')
            
            first_paragraph_tag = page_soup.find('p')
            clean_paragraph = first_paragraph_tag.text.strip()
            page_title = page_soup.title.string

            writer.writerow([page_title, clean_paragraph])
        
        else:
            print(f'Failed to get {page_url}')

        time.sleep(2)
# Web Scraping and Text Analysis

This repository provides a Python-based solution for scraping data from websites and performing text analysis using BeautifulSoup and NLTK (Natural Language Toolkit).

With some Python's scripts it automates the process of extracting textual content from Wikipedia's pages. And then processes the text for analysis such as tokenization and sentiment analysis.

To get the pages it used request's python modules and then all a's tag. After that, it access these tags and get the page's title and the first paragraph.

Next step is all about text analysis. It takes the first paragraph of all selected pages and does the tokenize, remove stopwords, remove punctuation and finally does the sentiment analysis.

According to the words in the paragraph, it classifies in positive (greater then 0.05), negative (less than -0.05), and neutral (between -0.05 and 0.05).

# Features

- Web Scraping: Use BeautifulSoup to scrape text data from HTML page.
- Text processing and analysis: tokenization, stopword removal and sentiment analysis using NLTK.

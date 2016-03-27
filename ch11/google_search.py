#! python3.5
# This small program takes a string passed on the command line or the contents of the
# clipboard and opens a web browser with the top Google Search results in separate
# tabs.

from sys import argv
from bs4 import BeautifulSoup
import pyperclip
import requests
import webbrowser

BASE_URL = 'http://google.com{}'
SEARCH_URL = 'http://google.com/search?q={}'

if len(argv) > 1:
    search_string = ' '.join(argv[1:])
else:
    search_string = pyperclip.paste()

search_results = requests.get(SEARCH_URL.format(search_string))
search_results.raise_for_status()

soup = BeautifulSoup(search_results.content, 'html.parser')
result_links = soup.select('.r a')

num_links_to_open = min(5, len(result_links))

for i in range(num_links_to_open):
    webbrowser.open(BASE_URL.format(result_links[i].get('href')))

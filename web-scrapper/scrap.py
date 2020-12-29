# @author: Lucky Amadi

import requests
from bs4 import BeautifulSoup

raw_data = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(raw_data.text, 'html.parser')
story_links = soup.select('.storylink')
votes = soup.select('.score')

for vote in votes:
	print(vote)
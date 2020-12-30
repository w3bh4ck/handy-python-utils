# @author: Lucky Amadi
from pprint import pprint

import requests
from bs4 import BeautifulSoup

raw_data = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(raw_data.text, 'html.parser')
story_links = soup.select('.storylink')
sub_text = soup.select('.subtext')


def sort_stories_by_votes(news_list):
	return sorted(news_list, key=lambda k: k['votes'], reverse=True)


def create_custom_news(links, votes):
	hacker_news = []
	for index, item in enumerate(links):
		news_title = links[index].getText()
		href = links[index].get('href', None)
		vote = sub_text[index].select('.score')
		if len(vote) > 0:
			points = int(vote[0].getText().replace(' points', ''))

		if points > 99:
			hacker_news.append({'title': news_title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hacker_news)


pprint(create_custom_news(story_links, sub_text))

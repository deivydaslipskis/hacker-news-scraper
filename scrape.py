import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

selected_links = soup.select('.storylink')
selected_links2 = soup2.select('.storylink')
selected_subtexts = soup.select('.subtext')
selected_subtexts2 = soup2.select('.subtext')

all_links = selected_links + selected_links2
all_subtexts = selected_subtexts + selected_subtexts2


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(all_links, all_subtexts))

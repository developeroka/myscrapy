from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime


class Scipy:

    def set_url(self, url):

        self.get_html(url)

    def get_html(self, quote_page):

        page = urlopen(quote_page)
        self.parse_page_to_beautifulsoup(page)

    def parse_page_to_beautifulsoup(self, page):

        return BeautifulSoup(page, 'html.parser')


if __name__ == '__main__':
    quote_page = 'https://evand.com/events?sort=trending'
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    with open('evand.csv', 'a') as csv_file:
        link_count = 0
        for link in soup.findAll('div', attrs={'class': 'event-card-main'}):
            event_link = 'https://evand.com' + link.a['href']
            event_name = link.a.findChildren()[4].text
            event_place = link.a.findChildren()[7].text
            event_datetime = link.a.findChildren()[3].findChildren()[8].text
            event_price = link.a.findChildren()[3].findChildren()[11].text
            # writer = csv.writer(csv_file)
            # writer.writerow([event_name, event_price, event_place, event_date, event_time, event_link])

from urllib.request import urlopen
from bs4 import BeautifulSoup


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
    for link in soup.findAll('div', attrs={'class': 'event-card-main'}):
        print('https://evand.com' + link.a['href'])

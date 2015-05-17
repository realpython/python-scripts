import requests
from lxml import html
from collections import defaultdict


def get_stocks(url):
    # Make Request
    page = requests.get(url)
    # Parse/Scrape
    tree = html.fromstring(page.text)
    xpath = '//*[@id="mw-content-text"]/table[1]'
    rows = tree.xpath(xpath)[0].findall("tr")
    rows = [(row.getchildren()[0], row.getchildren()[3]) for row in rows[1:]]
    rows = [(row[0].getchildren()[0].text, row[1].text) for row in rows]
    industries = defaultdict(list)
    for row in rows:
        industries[row[1]].append(row[0])
    return industries


def output_data(data_dict):
    for industry in data_dict:
        print('\n'+industry)
        print('-'*len(industry))
        for ticker in data_dict[industry]:
            print(ticker)


if __name__ == '__main__':
    url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    scraped_data = get_stocks(url)
    output_data(scraped_data)

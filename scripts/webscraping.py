import requests
from bs4 import BeautifulSoup

def cars_brand_links():
    url = 'https://www.carsprite.com/en/car-prices'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll("a"):
        href = link.get('href')
        if "car-prices" not in href:
           pass
        else:
            data = href
            i = 9
            while i < 49:
                print(data[i])
                i += 1



cars_brand_links()

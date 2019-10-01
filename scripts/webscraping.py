import requests
from bs4 import BeautifulSoup

def cars_brand_links():
    url = 'https://www.carsprite.com/en/car-prices/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll("a"):
        href = "https://www.carsprite.com/en/" + link.get('href')
        if "car-prices/" not in href:
           pass
        else:
            data = href
            get_single_item_data(data)
def get_single_item_data(brand_url):
    source_code = requests.get(brand_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll("a"):
        href1 = link.get('href')
        if "/en/" not in href1:
           data1 = href1
           if "https" not in data1:
               data2 = data1
               if "/car-prices/" not in data2:
                   data_final = 'https://www.carsprite.com/en/car-prices/' + data2
                   print(data_final)

        else:
            pass


cars_brand_links()

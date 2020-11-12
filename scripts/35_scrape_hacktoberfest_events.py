import requests
import pandas
from bs4 import BeautifulSoup

# creating a soup object with html we got from the response
url = "https://hacktoberfest.digitalocean.com/events"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html)

# creating array of datas
all_names = []
all_locations = []
all_dates = []
all_time_zones = []
all_urls = []

# iterating on all the "tr" elements.
for tr_element in soup.findAll("tr", attrs={"class": "past"}):

    # for each tr element we find the proper value and add it to its proper array
    name_element = tr_element.find("td", attrs={"class": "event_name"})
    name = name_element.text.strip()
    all_names.append(name)

    location_element = tr_element.find("td", attrs={"class": "location"})
    location = location_element.text.strip()
    all_locations.append(location)

    date_element = tr_element.find("td", attrs={"data-label": "date"})
    date = date_element.text.strip()
    all_dates.append(date)

    time_zone_element = tr_element.find("td", attrs={"data-label": "zone"})
    time_zone = time_zone_element.text.strip()
    all_time_zones.append(time_zone)

    url_element = tr_element.find("a", attrs={"class": "emphasis"})
    url = url_element['href']
    all_urls.append(url)

# setting up our Comma Seperated Values
csv_name = "events.csv"
csv_structure = {
    "Name": all_names,
    "Location": all_locations,
    "Date": all_dates,
    "Time Zone": all_time_zones,
    "URL": all_urls,
}
# Creating a csv
dataFrame = pandas.DataFrame(csv_structure)
dataFrame.to_csv(csv_name, index=False, encoding='utf-8')



import requests
import re
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# regex
link_re = re.compile(r'href="(.*?)"')


def crawl(url):

    req = requests.get(url)

    # Check if successful
    if(req.status_code != 200):
        return []

    # Find links
    links = link_re.findall(req.text)

    print("\nFound {} links".format(len(links)))

    # Search links for emails
    for link in links:

        # Get an absolute URL for a link
        link = urljoin(url, link)

        print(link)

if __name__ == '__main__':
    crawl('http://www.realpython.com')

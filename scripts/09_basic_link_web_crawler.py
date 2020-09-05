import requests
import re
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# regex
link_re = re.compile(r'href="(.*?)"')


def crawl(url):
    """
        Crawls a page
        Arguments:
         - URL of the page to crawl
         Return:
         - List of all unique links found
    """

    found_link = []
    req = requests.get(url)

    # Check if successful
    if(req.status_code != 200):
        return []

    # Finding unique links
    links = set(link_re.findall(req.text))

    print("\nFound {} unique links".format(len(links)))

    # Search links for emails
    for link in links:

        # Get an absolute URL for a link
        link = urljoin(url, link)
        found_link.append(link)
        print(link)
    
    return found_link

if __name__ == '__main__':
    url = input("Enter a url to crawl: ")
    crawl(url)

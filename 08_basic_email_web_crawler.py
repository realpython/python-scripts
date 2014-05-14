import requests
import re
import urlparse

# regex
email_re = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')
link_re = re.compile(r'href="(.*?)"')

def crawl(url, maxlevel):

    result = set()

    while maxlevel > 0:

        # Get the webpage
        req = requests.get(url)

        # Check if successful
        if(req.status_code != 200):
            return []

        # Find and follow all the links
        links = link_re.findall(req.text)
        for link in links:
            # Get an absolute URL for a link
            link = urlparse.urljoin(url, link)

        # Find all emails on current page
        result.update(email_re.findall(req.text))

        print "Crawled level: {}".format(maxlevel)

        # new level
        maxlevel -= 1

        # recurse 
        crawl(link, maxlevel)

    return result

emails = crawl('http://www.website_goes_here_dot_com', 2)

print "\nScrapped e-mail addresses:"
for email in emails:
    print email
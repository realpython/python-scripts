import urllib2
import re

# get url
url =raw_input('Enter a URL (include `http://`): ')

# connect to the url
website = urllib2.urlopen(url)

# read html
html = website.read()

# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

# output links
for link in links:
	print link[0]
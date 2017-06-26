import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re
# import urllib
import urllib


images = []
file_names = []

# url = 'http://imgur.com/a/risg9'
url = 'http://imgur.com/a/risg9?grid'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

# for old URL
a_tags = soup.find_all('a', attrs={'class': 'zoom'})
a_tag = soup.find('a', attrs={'class': 'zoom'})

# for tag in a_tags:
    # images.append(tag.contents)

# for new URL
grid_holders = soup.find_all('span', attrs={'class':'post-grid-image pointer'})

print grid_holders

for span in grid_holders:
	print span
	images.append(span.contents)

# print images

# pattern = re.compile('//i.imgur.com//*.jpg')
pattern = re.compile(r'\/\/i\.imgur\.com\/\S+\.jpg')

# \/\/i\.imgur\.com\/\S+\.jpg
# http://pythex.org/

for image in images:
    match = re.search(pattern, str(image), flags=0)
    if match:
        file_names.append(str(image)[match.start():match.end()])


file_opener = urllib.URLopener()


for file_name in file_names:
	print file_name
	urllib.urlretrieve("http:" + str(file_name), 'images/' + str(file_name)[14:22] + ".jpg")
# pprint(images)


# print soup.prettify()

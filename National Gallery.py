import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# Open CSV
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link']) 

# Extract artist data 
artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

# Print and write artist data
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    print(names)
    print(links)
    f.writerow([names, links])








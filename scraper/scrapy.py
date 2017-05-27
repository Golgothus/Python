#! python3
# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus

import requests
import bs4

res = requests.get('https://www.nsa.gov')

try:
    res.raise_for_status()

except Exception as exc:
    print('There was a problem: %s' % (exc))

playFile = open('nsa.txt')

#for chunk in res.iter_content(100000):
#    playFile.write(chunk)

#playFile.close()

p1Soup = bs4.BeautifulSoup(playFile.read(), 'html.parser')

elems = p1Soup.select('p')

print(type(elems))
print(str(elems[0]))

for p in elems:
    print(p)

print(len(elems))

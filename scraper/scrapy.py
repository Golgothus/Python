#! python3
# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus

import requests
import bs4
import sys
import webbrowser

print('Researching...')
res = requests.get('https://www.google.gov' + ''.join(sys.argv[1:]))

try:
    res.raise_for_status()

except Exception as exc:
    print('There was a problem: %s' % (exc))

#Open a browser tab for each result.
soupTasty = bs4.BeautifulSoup(res.text, 'html.parser')
linkelems = soupTasty.select('.r a')
numOpen = min(7, len(linkelems))

for l in range(numOpen):
    webbrowser.open('http://nsa.gov' + linkelems[l].get('href'))

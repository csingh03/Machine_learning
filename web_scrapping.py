import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://login.thetimes.co.uk/?gotoUrl=https://www.thetimes.co.uk/")

br.select_form(nr=0)
br.form['username'] = 'username'
br.form['password'] = 'chandani'
br.submit()
url = 'https://www.thetimes.co.uk/edition/news/rail-upgrades-face-cash-crisis-after-treasury-demands-2bn-ndwhmtvlx'
soup = BeautifulSoup(br.open(url).read(), "html.parser")
txt = open('output_1.txt', 'w')
tags = soup('p')
for tag in tags:
    txt.write(tag.text.encode('utf-8') + '\n' + '\n')

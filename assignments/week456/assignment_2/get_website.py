#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://store.steampowered.com/app/1343370/Old_School_RuneScape/"
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

div = soup.find_all("div", class_="game_purchase_price")
print(div[0].text.strip())
#text.strip() is a function of print which can be used to clean up a result
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
import requests as uReq
import json, lxml, random

website = uReq.get("https://www.passiton.com/inspirational-quotes")
data = bSoup(website.content, "lxml")
dataQuotes = []
for ListQuotes in data.findAll("div", {"class":"portfolio-image"}):
	urlQuotes = "https://www.passiton.com{}".format(ListQuotes.a["href"])
	dataQuotes.append(urlQuotes)
randomQuotes = random.choice(dataQuotes)
website = uReq.get(randomQuotes)
data = bSoup(website.content, "lxml")
for getDataQuotes in data.findAll("div", {"class":"col-sm-8 col-sm-offset-2 text-center"}):
	image = getDataQuotes.a["href"]
	quotes = getDataQuotes.a.img["alt"]
result = {
	"quotes": quotes,
	"image": image
}
print(json.dumps(result, indent=4, sort_keys=False))
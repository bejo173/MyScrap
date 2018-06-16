# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
import requests as uReq
import json, lxml, re


website = uReq.get("http://pururin.io/browse/newest?page=1")
data = bSoup(website.content, "lxml")
dataDoujin = []
for listDoujin in data.findAll("div", {"class":"gallery-listing"}):
	for delPage in listDoujin.findAll("ul", {"class":"pagination"}):
		delPage.decompose()
	for getDoujin in listDoujin.findAll("a"):
		title = getDoujin.img["alt"].replace("Read ","")
		url = getDoujin["href"]
		dataDoujin.append({"title": title, "url": url})
result ={
	"result": dataDoujin
}
print(json.dumps(result, indent=4, sort_keys=False))

website = uReq.get("http://pururin.io/browse/search?q=fate&sType=normal&page=1")
data = bSoup(website.content, "lxml")
dataDoujin = []
for listDoujin in data.findAll("div", {"class":"gallery-listing"}):
	for delPage in listDoujin.findAll("ul", {"class":"pagination"}):
		delPage.decompose()
	for getDoujin in listDoujin.findAll("a"):
		title = getDoujin.img["alt"].replace("Read ","")
		url = getDoujin["href"]
		dataDoujin.append({"title": title, "url": url})
result ={
	"result": dataDoujin
}
print(json.dumps(result, indent=4, sort_keys=False))

website = uReq.get("http://pururin.io/gallery/32059/fatedeliheal-order")
data = bSoup(website.content, "lxml")
for readOnline in data.findAll("div", {"class":"text-center"}):
	url = readOnline.a["href"]
	website = uReq.get(url)
	data = bSoup(website.content, "lxml")
	dataImage = []
	for listChapter in data.findAll("script"):
		for res in listChapter.contents:
			if res.startswith("\n\t\tvar"):
				js = re.search(r'chapters\s*=\s*(\{.+\})\s*;', res).group(1)
				data = json.loads(js)
				images = []
				for i in data:
					url = data.get(i, {}).get("image", False)
					url and images.append(url)
				for listImage in images:
					print(listImage)
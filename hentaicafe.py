# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
import requests as uReq
import json, lxml

website = uReq.get("https://hentai.cafe/page/1/")
data = bSoup(website.content, "lxml")
dataDoujin = []
for listAllDoujin in data.findAll("article"):
	for getAllDoujin in listAllDoujin.findAll("div", {"class":"entry-wrap"}):
		for getDoujin in getAllDoujin.findAll("h2", {"class":"entry-title"}):
			title = getDoujin.a.text
			url = getDoujin.a["href"]
			dataDoujin.append({"title": title, "url": url})
result = {
	"result": dataDoujin
}
print(json.dumps(result, indent=4, sort_keys=False))

website = uReq.get("https://hentai.cafe/page/1/?s=harem")
data = bSoup(website.content, "lxml")
dataDoujin = []
for listAllDoujin in data.findAll("article"):
	for getAllDoujin in listAllDoujin.findAll("div", {"class":"entry-wrap"}):
		for getDoujin in getAllDoujin.findAll("h2", {"class":"entry-title"}):
			title = getDoujin.a.text
			url = getDoujin.a["href"]
			dataDoujin.append({"title": title, "url": url})
result = {
	"result": dataDoujin
}
print(json.dumps(result, indent=4, sort_keys=False))

website = uReq.get("https://hentai.cafe/himeno-komomo-academic-advancement-committee-zero/")
data = bSoup(website.content, "lxml")
for readOnline in data.findAll("a", {"class":"x-btn x-btn-flat x-btn-rounded x-btn-large"}):
	url = readOnline["href"]
	website = uReq.get(url)
	data = bSoup(website.content, "lxml")
	dataUrl = []
	for listUrlImage in data.findAll("ul", {"class":"dropdown"}):
		for getUrlImage in listUrlImage.findAll("li"):
			url = getUrlImage.a["href"]
			dataUrl.append(url)
	for getUrl in dataUrl:
		website = uReq.get(getUrl)
		data = bSoup(website.content, "lxml")
		for getImage in data.findAll("div", {"class":"inner"}):
			image = getImage.a.img["src"]
			print(image)
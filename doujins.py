# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from re import match
import requests as uReq
import html5lib, json, lxml, re

website = uReq.get("https://doujins.com/searches?words=milf&page=1")
data = bSoup(website.content, "lxml")
dataDoujins = []
for ListAllDoujins in data.findAll("div", {"class":"col-xs-6 col-sm-4 col-md-3 col-lg-2"}):
	for getTitle in ListAllDoujins.findAll("div", {"class":"title"}):
		title = getTitle.div.text
	for getUrl in ListAllDoujins.findAll("a"):
		url = "https://doujins.com{}".format(getUrl["href"])
		dataDoujins.append({"title": title, "url": url})
result = {
	"result": dataDoujins
}
print(json.dumps(result, indent=4, sort_keys=False))

website = uReq.get("https://doujins.com/hentai-magazine-chapters/nokoppa-the-mom-is-the-mating-season-36248")
data = bSoup(website.content, "lxml")
for listAllImage in data.findAll("div", {"class":"col-xs-12 text-center"}):
	for getAllImage in listAllImage.findAll("img", {"class":"doujin"}):
		allImage = getAllImage["data-file"]
		print(allImage)
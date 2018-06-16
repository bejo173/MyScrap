# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from re import match
import requests as uReq
import json, lxml, re

def skipLinkZippyshare(url):
	website = uReq.get(url)
	data = bSoup(website.content, "lxml")
	for listUrl in data.findAll("script", {"type":"text/javascript"})[5]:
		getLink = re.search("https://(\w+)\.zippyshare\.com/v/(\w+)/file.html", listUrl).group()
		return getLink
		
website = uReq.get("https://www.oploverz.in/page/1/")
data = bSoup(website.content, "lxml")
dataPost = []
for listPost in data.findAll("ul"):
	for listInfoPost in listPost.findAll("div", {"class":"dtl"}):
		title = listInfoPost.h2.a["title"]
		url = listInfoPost.h2.a["href"]
		dataPost.append({"title": title, "url": url})
result = {
	"result": dataPost
}
print(json.dumps(result, indent=4, sort_keys=False))

website = uReq.get("https://www.oploverz.in/megalo-box-episode-10-subtitle-indonesia/")
data = bSoup(website.content, "lxml")
index = [listAllLink for listAllLink in data.findAll("div", {"class":"soraurl list-download"})]
zippy480 = index[0]
zippy720V1 = index[1]
zippy720V2 = index[2]
zippy1080 = index[3]
for getLink480 in zippy480.findAll("a", text=[" Zippyshare", "Zippyshare"]):
	linkZippy480 = getLink480["href"]
for getLink720V1 in zippy720V1.findAll("a", text=[" Zippyshare", "Zippyshare"]):
	linkZippy720V1 = getLink720V1["href"]
for getLink720V2 in zippy720V2.findAll("a", text=[" Zippyshare", "Zippyshare"]):
	linkZippy720V2 = getLink720V2["href"]
for getLink1080 in zippy1080.findAll("a", text=[" Zippyshare", "Zippyshare"]):
	linkZippy1080 = getLink1080["href"]
convertLink480 = skipLinkZippyshare(linkZippy480)
convertLink720V1 = skipLinkZippyshare(linkZippy720V1)
convertLink720V2 = skipLinkZippyshare(linkZippy720V2)
convertLink1080 = skipLinkZippyshare(linkZippy1080)
result = {
	"result": {
		"480": {
			"Zippyshare": convertLink480
		},
		"720V1": {
			"Zippyshare": convertLink720V1
		},
		"720V2": {
			"Zippyshare": convertLink720V2
		},
		"1080": {
			"Zippyshare": convertLink1080
		}
	}
}
print(json.dumps(result, indent=4, sort_keys=False))
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from urllib.request import urlopen
import requests as uReq
import json, lxml, re, time, urllib

start = time.time()

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
website = "https://hitomi.la/index-all-1.html"
data = bSoup(urllib.request.urlopen(urllib.request.Request(website, headers = header)), "lxml")
dataDoujin = []
for listAllDoujin in data.findAll("div", {"class":"gallery-content"}):
	for getAllDoujin in listAllDoujin.findAll("h1"):
		title = getAllDoujin.a.text
		url = "https://hitomi.la{}".format(getAllDoujin.a["href"])
		id = getAllDoujin.a["href"].replace("/galleries/","").replace(".html","")
		dataDoujin.append({"title": title, "galleries_id": id, "url": url})
result = {
	"result": dataDoujin
}
print(json.dumps(result, indent=4, sort_keys=False))

galleries = "1238217"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
website = "https://ltn.hitomi.la/galleries/{}.js".format(galleries)
data = bSoup(urllib.request.urlopen(urllib.request.Request(website, headers = header)), "lxml")
for listJson in data.p:
	images = re.search(r'(\[.+\])', listJson)
	images = json.loads(images.group(1))
	allImage = "http://0a.hitomi.la/galleries/{}/".format(galleries)
	index = [allImage + getImage.get("name") for getImage in images]
	print(json.dumps(index, indent=4, sort_keys=False))
	
print("Execution time = {0:f}".format(time.time() - start))
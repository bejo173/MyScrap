# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
import requests as uReq
import json, lxml, re, time

start = time.time()

website = uReq.get("https://nhentai.net/search/?q=milf&page=2")
data = bSoup(website.content, "lxml")
dataDoujins = []
for listAllDoujins in data.findAll("div", {"class":"container index-container"}):
	for getUrl in listAllDoujins.findAll("div", {"class":"gallery"}):
		url = "https://nhentai.net{}".format(getUrl.a["href"])
	for getTitle in listAllDoujins.findAll("div", {"class":"caption"}):
		title = getTitle.text
		dataDoujins.append({"title": title, "url": url})
result = {
	"result": dataDoujins
}
print(json.dumps(result, indent=4, sort_keys=False))

url = "https://nhentai.net/g/235857/"
website = uReq.get("{}1/".format(url))
data = bSoup(website.content, "lxml")
for getJson in data.findAll("script")[2]:
	imgs = re.search(r"gallery\s*:\s*(\{.+\}),", getJson)
	imgs = json.loads(imgs.group(1))
	idx = imgs.get("media_id")
	images = []
	cdn = "https://i.nhentai.net/galleries/"
	ext = {"j": "jpg", "p": "png", "g": "gif"}
	for n, i in enumerate(imgs.get("images", {}).get("pages", [])):
		images.append("{}{}/{}.{}".format(cdn, idx, n + 1, ext.get(i.get("t"))))
	print(images)

print("Execution time = {0:f}".format(time.time() - start))
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
import requests as uReq
import json, lxml, re, time

start = time.time()

def getHtml(url, header):
	getUrl = uReq.get(url, headers = header)
	return bSoup(getUrl.content, "lxml")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
website = "https://www.google.co.in/search?q=naruto&source=lnms&tbm=isch"
data = getHtml(website, header)
dataGoogle = []
for listAllJson in data.findAll("div", {"class":"rg_meta"}):
	getAllJson = json.loads(listAllJson.text)
	dataGoogle.append({"title": getAllJson["pt"], "source": getAllJson["ru"], "image": getAllJson["ou"]})
result = {
	"result": dataGoogle
}
print(json.dumps(result, indent=4, sort_keys=False))

print("Execution time = {0:f}".format(time.time() - start))
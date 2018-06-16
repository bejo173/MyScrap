# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
from threading import Thread
import requests as uReq
import time, json, random, os, sys, urllib.parse, html5lib, lxml

start = time.time()
session = uReq.session()
result = {
    '480': [],
    '720': []
}

def skipLinkNekopoi(url, quality):
	with session as web:
		web.headers["user-agent"] = "Mozilla/5.0"
		url = web.get(url)
		data = bSoup(url.content, "lxml")
		for listUrl in data.findAll("div", {"class":"col-sm-6"}):
			result[quality].append(listUrl.a['href'])

'''
with session as web:
	web.headers["user-agent"] = "Mozilla/5.0"
	url = web.get("http://nekopoi.care/page/1/".format(urllib.parse.quote))
	data = bSoup(url.content, "lxml")
	dataresult = []
	for listpost in data.findAll("div", {"class":"eroinfo"}):
		for getpost in listpost.findAll("h2"):
			title = getpost.a.text
			url = "http://nekopoi.care{}".format(getpost.a["href"])
			dataresult.append({"title": title, "url": url})
	results = {
		"result": dataresult
	}
	print(json.dumps(results, indent=4, sort_keys=False))
'''

with session as web:
	web.headers["user-agent"] = "Mozilla/5.0"
	url = web.get("http://nekopoi.care/muttsuri-dosukebe-tsuyu-gibo-shimai-no-honshitsu-minuite-sex-sanmai-episode-1-subtitle-indonesia/".format(urllib.parse.quote))
	data = bSoup(url.content, "lxml")
	listdata480 = []
	listdata720 = []
	listlink = [link for link in data.findAll("div", {"class":"liner"})]
	link480 = listlink[1]
	link720 = listlink[0]
	for listurl480 in link480.findAll("p"):
		for urldownload480 in listurl480.findAll("a", text=["Solidfiles", "GoogleDrive", "ZippyShare"]):
			url = urldownload480["href"]
			listdata480.append(url)
	for listurl720 in link720.findAll("p"):
		for urldownload720 in listurl720.findAll("a", text=["Solidfiles", "GoogleDrive", "ZippyShare"]):
			url = urldownload720["href"]
			listdata720.append(url)
	threads = []
	for link480 in listdata480:
		td = Thread(target=skipLinkNekopoi, args=(link480, '480',))
		td.setDaemon(False)
		threads.append(td)
	for link720 in listdata720:
		td = Thread(target=skipLinkNekopoi, args=(link720, '720',))
		td.setDaemon(False)
		threads.append(td)
	for thread in threads:
		thread.start()
	for thr in threads:
		thr.join()

	result = {
		"result": {
			"480": {
				"GoogleDrive": result['480'][1],
				"Solidfiles": result['480'][0],
				"ZippyShare": result['480'][2]
			},
			"720": {
				"GoogleDrive": result['720'][1],
				"Solidfiles": result['720'][0],
				"ZippyShare": result['720'][2]
			}
		}
	}
	print(json.dumps(result,indent=4, sort_keys=False))
	
print("Execution time = {0:.5f}".format(time.time() - start))
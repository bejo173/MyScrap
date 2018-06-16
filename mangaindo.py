# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
import requests as uReq
import time, json, random, os, sys, urllib.parse, html5lib, lxml

start = time.time()

def Mangaindo(url):
	with uReq.session() as web:
		web.headers["user-agent"] = "Mozilla/5.0"
		url = web.get(url)
		data = bSoup(url.content, "html5lib")
		datapost = []
		for listPost in data.findAll("li", {"class":"rpwe-li rpwe-clearfix"}):
			for detailsPost in listPost.findAll("a"):
				title = detailsPost.text
				url = detailsPost["href"]
			for detailsDate in listPost.findAll("time", {"class":"rpwe-time published"}):
				release = detailsDate.text
				datapost.append({"title": title, "release": release, "url":url})
		result = {
			"code": 200,
			"result": datapost
		}
		print(json.dumps(result, indent=4, sort_keys=False))
		
def MangaindoPost(url):
	with uReq.session() as web:
		web.headers["user-agent"] = "Mozilla/5.0"
		url = web.get(url)
		data = bSoup(url.content, "html5lib")
		datapost = []
		for listImage in data.findAll("p"):
			for urlImage in listImage.findAll("img"):
				image = urlImage["src"]
				datapost.append(image)
		result = {
			"code": 200,
			"image": datapost
		}
		print(json.dumps(result, indent=4, sort_keys=False))
		
Mangaindo("https://mangaindo.web.id/")
MangaindoPost("https://mangaindo.web.id/ghosts-wife-chapter-36/")

print("Execution time = {0:.5f}".format(time.time() - start))
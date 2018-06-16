# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
import requests as uReq
import time, json, random, os, sys, urllib.parse, html5lib, lxml

start = time.time()

def JurnalOtaku(url):
	with uReq.session() as web:
		web.headers["user-agent"] = "Mozilla/5.0"
		url = web.get(url)
		data = bSoup(url.content, "html5lib")
		datapost = []
		for listPost in data.findAll("div", {"class":"cover size-a has-depth"}):
			for listTitle in listPost.findAll("img"):
				title = listTitle["alt"]
			for listUrl in listPost.findAll("a"):
				url = listUrl["href"]
				datapost.append({"title": title, "url": url})
		result = {
			"code": 200,
			"result": datapost
		}
		print(json.dumps(result, indent=4, sort_keys=False))

def JurnalOtakuPost(url):
	with uReq.session() as web:
		web.headers["user-agent"] = "Mozilla/5.0"
		url = web.get(url)
		data = bSoup(url.content, "html5lib")
		datapost = []
		for content in data.findAll("div", {"class":"section-wrapper section-article-content"}):
			for contentData in content.findAll("div", {"class":"meta-cover"}):
				for getData in contentData.findAll("img"):
					title = getData["alt"]
					thumb = getData["src"]
			for contentPost in content.findAll("div", {"class":"meta-content"}):
				for getData in contentPost.findAll("p"):
					text = getData.text
					datapost.append(text)
		berita = ""
		for detailsPost in datapost:
			berita += detailsPost
		result = {
			"code": 200,
			"result": {
				"title": title,
				"thumb": thumb,
				"berita": berita
			}
		}
		print(json.dumps(result, indent=4, sort_keys=False))
		
JurnalOtaku("http://jurnalotaku.com/all/page/1")
JurnalOtakuPost("http://jurnalotaku.com/2018/05/31/planet-with-ungkapkan-para-penyanyi-lagu-tema/")
	
print("Execution time = {0:.5f}".format(time.time() - start))
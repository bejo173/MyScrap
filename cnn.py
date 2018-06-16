# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from bs4.element import Tag
import requests as uReq
import time, json, random, os, sys, urllib.parse, html5lib, lxml

start = time.time()

with uReq.session() as web:
	web.headers["user-agent"] = "Mozilla/5.0"
	url = web.get("https://www.cnnindonesia.com/".format(urllib.parse.quote))
	data = bSoup(url.content, "html5lib")
	datapost = []
	for media in data.findAll("div", {"class":"box feed berita_terbaru_lst"}):
		for anu in media.findAll("div", {"class":"box box_grey akujkt mb15"}):
			anu.decompose()
		for anu1 in media.findAll("div", {"class":"box box_grey mb20 gtm_featuredbox_kanal_1"}):
			anu1.decompose()
		for anu2 in media.findAll("div", {"class":"box box_grey mb20 gtm_featuredbox_kanal_2"}):
			anu2.decompose()
		for anu3 in media.findAll("div", {"class":"box box_black mb20"}):
			anu3.decompose()
		for listArticle in media.findAll("article"):
			for articleData in listArticle.findAll("a"):
				url = articleData["href"]
				for listTitle in articleData.findAll("span", {"class":"box_text"}):
					title = listTitle.h2.text
				for listCategori in articleData.findAll("span", {"class":"kanal"}):
					categori = listCategori.text
				for listRelease in articleData.findAll("span", {"class":"date"}):
					release = listRelease.text
					datapost.append({"title": title, "categori": categori, "release": release, "url":url})
	result = {
		"code": 200,
		"result": datapost
	}
	print(json.dumps(result, indent=4, sort_keys=False))

with uReq.session() as web:
	web.headers["user-agent"] = "Mozilla/5.0"
	url = web.get("https://www.cnnindonesia.com/nasional/20180531152152-12-302544/jaksa-minta-yulianis-buka-cadar-saat-bersaksi-di-sidang-anas/".format(urllib.parse.quote))
	data = bSoup(url.content, "html5lib")
	for content in data.findAll("div", {"class":"content_detail"}):
		for dataTitle in content.findAll("h1", {"class":"title"}):
			title = dataTitle.text.replace("\n "," ")
		for dataDate in content.findAll("div", {"class":"date"}):
			release = dataDate.text.replace("\n "," ")
		for dataThumb in content.findAll("div", {"class":"media_artikel"}):
			for urlThumb in dataThumb.findAll("img"):
				thumb = urlThumb["src"]
		for dataText in content.findAll("span", {"id":"detikdetailtext"}):
			for delText1 in dataText.findAll("center"):
				delText1.decompose()
			for delText2 in dataText.findAll("table", {"class":"linksisip"}):
				delText2.decompose()
		text = dataText.text
	result = {
		"code": 200,
		"result": {
			"title": title,
			"release": release,
			"thumb": thumb,
			"berita": text
		}
	}
	print(json.dumps(result, indent=4, sort_keys=False))
		
print("Execution time = {0:.5f}".format(time.time() - start))
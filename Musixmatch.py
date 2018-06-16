# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
import requests as uReq
import time, json, random, urllib.parse, html5lib

def Musixmatch():
	with uReq.session() as web:
		web.headers["user-agent"] = "Mozilla/5.0"
		url = web.get("https://www.musixmatch.com/search/avici".format(urllib.parse.quote))
		data = bSoup(url.content, "html5lib")
		for trackList in data.findAll("ul", {"class":"tracks list"}):
			for urlList in trackList.findAll("a"):
				title = urlList.text
				url = urlList["href"]
				print(title, url)
		
def MusixmatchLyric():
	with uReq.session() as web:
		web.headers["user-agent"] = "Mozilla/5.0"
		url = web.get("https://www.musixmatch.com/lyrics/Avicii/The-Days".format(urllib.parse.quote))
		data = bSoup(url.content, "html5lib")
		for lyricContent in data.findAll("p", {"class":"mxm-lyrics__content "}):
			print(lyricContent)
		
Musixmatch()
MusixmatchLyric()
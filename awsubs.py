# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
import requests as uReq
import time, json, random, os, sys, urllib.parse, html5lib

with uReq.session() as web:
	web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	web = web.get("http://awsubs.co/kakuriyo-no-yadomeshi-episode-9-subtitle-indonesia/")
	data = bSoup(web.content, "html5lib")
	datalink = [link for link in data.findAll("div", {"class":"dl-item"})]
	link480 = datalink[0]
	link720 = datalink[1]
	link1080 = datalink[2]
	for datathumb in data.findAll("div", {"class":"separator"}):
		for urlthumb in datathumb.findAll("img"):
			thumb = urlthumb["src"]
			print(thumb)
	for zs480 in link480.findAll("a", text=["Zippyshare"]):
		Zippyshare480 = zs480["href"]
		with uReq.session() as web:
			web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
			web = web.get(Zippyshare480)
			data = bSoup(web.content, "html5lib")
			for safelink in data.findAll("div", {"id":"m"}):
				url = safelink.a["href"]
				with uReq.session() as web:
					web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
					web = web.get(url)
					data = bSoup(web.content, "html5lib")
					for redirect_url in data.findAll("div", {"class":"redirect_url"}):
						url = redirect_url.div.text
						with uReq.session() as web:
							web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
							web = web.get(url)
							data = bSoup(web.content, "html5lib")
							for kanan in data.findAll("div", {"class":"kanan"}):
								Zippy480 = kanan.a["href"]
	for gd480 in link480.findAll("a", text=["GoogleDrive"]):
		GoogleDrive480 = gd480["href"]
		with uReq.session() as web:
			web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
			web = web.get(GoogleDrive480)
			data = bSoup(web.content, "html5lib")
			for safelink in data.findAll("div", {"id":"m"}):
				url = safelink.a["href"]
				with uReq.session() as web:
					web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
					web = web.get(url)
					data = bSoup(web.content, "html5lib")
					for redirect_url in data.findAll("div", {"class":"redirect_url"}):
						url = redirect_url.div.text
						with uReq.session() as web:
							web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
							web = web.get(url)
							data = bSoup(web.content, "html5lib")
							for kanan in data.findAll("div", {"class":"kanan"}):
								GDrive480 = kanan.a["href"]
	for zs720 in link720.findAll("a", text=["Zippyshare"]):
		Zippyshare720 = zs720["href"]
		with uReq.session() as web:
			web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
			web = web.get(Zippyshare720)
			data = bSoup(web.content, "html5lib")
			for safelink in data.findAll("div", {"id":"m"}):
				url = safelink.a["href"]
				with uReq.session() as web:
					web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
					web = web.get(url)
					data = bSoup(web.content, "html5lib")
					for redirect_url in data.findAll("div", {"class":"redirect_url"}):
						url = redirect_url.div.text
						with uReq.session() as web:
							web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
							web = web.get(url)
							data = bSoup(web.content, "html5lib") 
							for kanan in data.findAll("div", {"class":"kanan"}):
								Zippy720 = kanan.a["href"]
	for gd720 in link720.findAll("a", text=["GoogleDrive"]):
		GoogleDrive720 = gd720["href"]
		with uReq.session() as web:
			web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
			web = web.get(GoogleDrive720)
			data = bSoup(web.content, "html5lib")
			for safelink in data.findAll("div", {"id":"m"}):
				url = safelink.a["href"]
				with uReq.session() as web:
					web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
					web = web.get(url)
					data = bSoup(web.content, "html5lib")
					for redirect_url in data.findAll("div", {"class":"redirect_url"}):
						url = redirect_url.div.text
						with uReq.session() as web:
							web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
							web = web.get(url)
							data = bSoup(web.content, "html5lib")
							for kanan in data.findAll("div", {"class":"kanan"}):
								GDrive720 = kanan.a["href"]
	for zs1080 in link1080.findAll("a", text=["Zippyshare"]):
		Zippyshare1080 = zs1080["href"]
		with uReq.session() as web:
			web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
			web = web.get(Zippyshare1080)
			data = bSoup(web.content, "html5lib")
			for safelink in data.findAll("div", {"id":"m"}):
				url = safelink.a["href"]
				with uReq.session() as web:
					web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
					web = web.get(url)
					data = bSoup(web.content, "html5lib")
					for redirect_url in data.findAll("div", {"class":"redirect_url"}):
						url = redirect_url.div.text
						with uReq.session() as web:
							web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
							web = web.get(url)
							data = bSoup(web.content, "html5lib") 
							for kanan in data.findAll("div", {"class":"kanan"}):
								Zippy1080 = kanan.a["href"]
	for gd1080 in link1080.findAll("a", text=["GoogleDrive"]):
		GoogleDrive1080 = gd1080["href"]
		with uReq.session() as web:
			web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
			web = web.get(GoogleDrive1080)
			data = bSoup(web.content, "html5lib")
			for safelink in data.findAll("div", {"id":"m"}):
				url = safelink.a["href"]
				with uReq.session() as web:
					web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
					web = web.get(url)
					data = bSoup(web.content, "html5lib")
					for redirect_url in data.findAll("div", {"class":"redirect_url"}):
						url = redirect_url.div.text
						with uReq.session() as web:
							web.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
							web = web.get(url)
							data = bSoup(web.content, "html5lib")
							for kanan in data.findAll("div", {"class":"kanan"}):
								GDrive1080 = kanan.a["href"]
	dataurl = {
		"code": 200,
		"result": {
			"480": {
				"GoogleDrive": GDrive480,
				"Zippyshare": Zippy480
			},
			"720": {
				"GoogleDrive": GDrive720,
				"Zippyshare": Zippy720
			},
			"1080": {
				"GoogleDrive": GDrive1080,
				"Zippyshare": Zippy1080
			}
		}
	}
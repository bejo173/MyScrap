# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bSoup
from re import match
import requests as uReq
import json, lxml, re

website = uReq.get("https://www.instagram.com/cristiano/")
data = bSoup(website.content, "lxml")
for getInfoInstagram in data.findAll("script", {"type":"text/javascript"})[3]:
	getJsonInstagram = re.search(r'window._sharedData\s*=\s*(\{.+\})\s*;', getInfoInstagram).group(1)
	data = json.loads(getJsonInstagram)
	for instagramProfile in data["entry_data"]["ProfilePage"]:
		username = instagramProfile["graphql"]["user"]["username"]
		name = instagramProfile["graphql"]["user"]["full_name"]
		picture = instagramProfile["graphql"]["user"]["profile_pic_url_hd"]
		biography = instagramProfile["graphql"]["user"]["biography"]
		followers = instagramProfile["graphql"]["user"]["edge_followed_by"]["count"]
		following = instagramProfile["graphql"]["user"]["edge_follow"]["count"]
		private = instagramProfile["graphql"]["user"]["is_private"]
		media = instagramProfile["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
		result = {
			"result": {
				"username": username,
				"full_name": name,
				"biography": biography,
				"followers": followers,
				"following": following,
				"media": media,
				"is_private": private,
				"profile_picture": picture
			}
		}
		print(json.dumps(result, indent=4, sort_keys=False))
	
	
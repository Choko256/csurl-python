# -*- coding:utf-8 -*-

import requests

API_URL = 'https://api.csurl.fr/api/'


class CSUrl:
	"""
	Generic object for using ChakSoft URL shortening service
	"""
	@staticmethod
	def shorten(cls, link):
		"""
		Shorten the link given in argument
		Returns an object with original link, short code and shortened link
		"""
		r = requests.post('{}'.format(API_URL),
			data={"origin": link},
			headers={"Content-Type": "application/json"}
		)
		return r.json()

	@staticmethod
	def get(cls, short):
		"""
		Get a full URL from the short code
		"""
		r = requests.get('{}{}'.format(API_URL, short))
		return r.json()

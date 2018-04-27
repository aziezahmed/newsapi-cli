"""The sources command."""

import requests, json

from .base import Base

from . import __api_key__ as API_KEY

class Sources(Base):

    def run(self):    	
    	url = "https://newsapi.org/v2/sources?apiKey=" + API_KEY
    	response = requests.get(url)
    	data = response.json()
    	sources = data["sources"]
    	for source in sources:
        	print(source["id"])
        


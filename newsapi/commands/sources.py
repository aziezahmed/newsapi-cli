"""The sources command."""

import requests, json

from .base import Base

class Sources(Base):

    def run(self):    	
    	url = "https://newsapi.org/v2/sources?apiKey=2ff80ad49a294ffc88827b9f0b47cb6c"
    	response = requests.get(url)
    	data = response.json()
    	sources = data["sources"]
    	for source in sources:
        	print(source["id"])
        


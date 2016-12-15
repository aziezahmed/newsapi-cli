"""The sources command."""

import requests, json

from .base import Base

class Sources(Base):

    def run(self):    	
    	url = "https://newsapi.org/v1/sources"
    	response = requests.get(url)
    	data = response.json()
    	sources = data["sources"]
    	for source in sources:
        	print(source["id"])
        


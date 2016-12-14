"""The sources command."""


import urllib, json

from .base import Base

class Sources(Base):

    def run(self):
    	url = "https://newsapi.org/v1/sources"
    	response = urllib.urlopen(url)
    	data = json.loads(response.read())
    	sources = data["sources"]
    	for source in sources:
        	print source["id"]
        


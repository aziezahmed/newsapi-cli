"""The headlines command."""


import urllib, json

from .base import Base

class Headlines(Base):

    def run(self):

        newsSource = self.options["<source>"]
        url = "https://newsapi.org/v1/articles?apiKey=2ff80ad49a294ffc88827b9f0b47cb6c&source=" + newsSource
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        articles = data["articles"]
        for article in articles:
            print article["title"].encode('utf8')
            if article["description"] is not None:
                print article["description"].encode('utf8')
                print article["url"]
                print " "


        


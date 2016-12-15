"""The headlines command."""

import requests, json

from .base import Base

class Headlines(Base):

    def run(self):
        newsSource = self.options["<source>"]
        url = "https://newsapi.org/v1/articles?apiKey=2ff80ad49a294ffc88827b9f0b47cb6c&source=" + newsSource
        response = requests.get(url)
        data = response.json()
        if data["status"] != "error":
            articles = data["articles"]
            for article in articles:
                print(json.dumps(article["title"]))
                if article["description"] is not None:
                    print(json.dumps(article["description"]))
                    print(article["url"])
                    print(" ")
        else:
            print("Invalid news source.")


        


"""The headlines command."""

import requests, json
from termcolor import colored
from unidecode import unidecode

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
                print(colored(unidecode(article["title"]),'green'))
                if article["description"] is not None:
                    print(unidecode(article["description"]))
                    print(colored(article["url"],'yellow'))
                    print(" ")
        else:
            print("Invalid news source.")


        


"""The search command."""

import requests, json
from termcolor import colored
from unidecode import unidecode
from . import __api_key__ as API_KEY
from .base import Base

class Search(Base):

    def run(self):
        keyword = self.options["<keyword>"]
        url = "https://newsapi.org/v2/top-headlines?apiKey=" + API_KEY + "&q=" + keyword
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


        


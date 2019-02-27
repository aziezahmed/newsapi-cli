"""The headlines command."""

import requests, json
from termcolor import colored
from unidecode import unidecode

from newsapi.user_settings import UserSettings

from .base import Base

class Headlines(Base):

    countries = ["ae", "ar", "at", "au", "be", "bg", "br", "ca", "ch", "cn", "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se", "sg", "si", "sk", "th", "tr", "tw", "ua", "us", "ve", "za"]
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

    def run(self):

        user_settings = UserSettings()
        api_key = user_settings.get_api_key()
        
        source = self.options["<source>"]

        if source in self.countries:
            url = "https://newsapi.org/v2/top-headlines?apiKey=" + api_key + "&country=" + source
        elif source in self.categories:
            url = "https://newsapi.org/v2/top-headlines?apiKey=" + api_key + "&category=" + source
        elif "/" in source:
            sourceSplit = source.split("/")
            if sourceSplit[0] in self.countries and sourceSplit[1] in self.categories:
                url = "https://newsapi.org/v2/top-headlines?apiKey=" + api_key + "&country=" + sourceSplit[0] + "&category=" + sourceSplit[1]
        else:
            url = "https://newsapi.org/v2/top-headlines?apiKey=" + api_key + "&sources=" + source
        

        if 'url' in vars():
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

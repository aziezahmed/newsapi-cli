"""The sources command."""

import requests, json

from .base import Base

from newsapi.user_settings import UserSettings

class Sources(Base):

    def run(self):

        user_settings = UserSettings()
        api_key = user_settings.get_api_key()
        
        url = "https://newsapi.org/v2/sources?apiKey=" + api_key
        response = requests.get(url)
        data = response.json()
        sources = data["sources"]
        for source in sources:
            print(source["id"])
        


"""
news

Usage:
  news sources
  news <source>
  news search <keyword>
  news api <api-key>
  news -h | --help
  news --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  news bbc-news
  news ars-technica
  news gb
  news business
  news gb/technology
  news search apple

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/aziezahmed/newsapi-cli/

"""

from docopt import docopt

from . import __version__ as VERSION

from newsapi.commands import Sources
from newsapi.commands import Headlines
from newsapi.commands import Search

from newsapi.user_settings import UserSettings

def main():

    """Main CLI entrypoint."""
    options = docopt(__doc__, version=VERSION)

    user_settings = UserSettings()
    api_key = user_settings.get_api_key()

    if api_key == "none" and not options["api"]:
        print("you need to set your api key first")
        print("if you don't have one you can get your's free from newsapi.org")
        print("example:");
        print("")
        print("news api 99213MY89API3842KEY0943320900")

    elif options["sources"]:
      sources = Sources(options)
      sources.run()
    elif options["api"]:
      user_settings.set_api_key(options["<api-key>"])
    elif options["search"]:
      search = Search(options)
      search.run()
    elif options["<source>"]:
      headlines = Headlines(options)
      headlines.run()

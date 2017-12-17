"""
news

Usage:
  news sources
  news <source>
  news search <keyword>
  news -h | --help
  news --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  news bbc-news
  news ars-technica
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


def main():
    """Main CLI entrypoint."""
    options = docopt(__doc__, version=VERSION)

    if options["sources"]:
      sources = Sources(options)
      sources.run()
    if options["search"]:
      search = Search(options)
      search.run()
    elif options["<source>"]:
      headlines = Headlines(options)
      headlines.run()

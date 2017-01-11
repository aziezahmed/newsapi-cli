"""
news

Usage:
  news sources
  news <source>
  news -h | --help
  news --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  news bbc-news
  news ars-technica

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/aziezahmed/newsapi-cli/

"""

from docopt import docopt

from . import __version__ as VERSION

from newsapi.commands import Sources
from newsapi.commands import Headlines

def main():
    """Main CLI entrypoint."""
    options = docopt(__doc__, version=VERSION)

    if options["sources"]:
      sources = Sources(options)
      sources.run()
    elif options["<source>"]:
      headlines = Headlines(options)
      headlines.run()

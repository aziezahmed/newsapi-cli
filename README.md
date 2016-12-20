# newsapi-cli

A command line application for displaying news headlines, written in Python.
Makes use of the [News API](https://newsapi.org) to get JSON metadata for news headlines.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* [Python 3](https://www.python.org) - Including PIP3

### Installing

Currently newsapi-cli is not on [PyPi](https://pypi.python.org/pypi) so it requires a manual install.

```
git clone https://github.com/aziezahmed/newsapi-cli.git
pip3 install -e ./newsapi-cli
```

## Using newsapi-cli

Display a list of all news sources
```
news sources
```

Get headlines from a specific source
```
news <source>
```

### Example

```
news bbc-news
```

## Built With

* [<docopt>](http://docopt.org) - To create the command line interface
* [News API](https://newsapi.org) - To get the news headlines


## Authors

* **Aziez Ahmed Chawdhary(https://github.com/aziezahmed)**


## License

This project is licensed under the MIT License


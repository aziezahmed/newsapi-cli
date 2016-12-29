newsapi-cli
===========

| A command line application for displaying news headlines, written in
  Python.
| Makes use of the `News API`_ to get JSON metadata for news headlines.

Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

Prerequisites
~~~~~~~~~~~~~

-  `Python 3`_ - Including PIP3

Installing
~~~~~~~~~~

Newsapi-cli is on `PyPi`_ so it can be installed with pip.

::

    pip install newsapi-cli

Using newsapi-cli
-----------------

Display a list of all news sources

::

    news sources

Get headlines from a specific source

::

    news <source>

Example
-------

::

    news bbc-news

Built With
----------

-  `skele-cli`_
-  `News API`_

Authors
-------

-  `Aziez Ahmed Chawdhary`_

License
-------

This project is licensed under the MIT License

.. _News API: https://newsapi.org
.. _Python 3: https://www.python.org
.. _PyPi: https://pypi.python.org/pypi
.. _skele-cli: https://github.com/rdegges/skele-cli
.. _Aziez Ahmed Chawdhary: https://github.com/aziezahmed

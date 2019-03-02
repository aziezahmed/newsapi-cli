newsapi-cli
===========

|PyPI version|

*A command line application for displaying news headlines, written in Python.*

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

-  `Python`_

Installing
~~~~~~~~~~

Newsapi-cli is on PyPI so it can be installed with pip.

.. code-block:: bash

    $ pip install newsapi-cli
    
To upgrade use the -U flag.

.. code-block:: bash

    $ pip install -U newsapi-cli

Alternatively get the source and install locally.

.. code-block:: bash

    $ pip install -e ./newsapi-cli/
    
Adding your API key
~~~~~~~~~~~~~~~~~~~

To begin you will need to add your API key. If you do not have an API key you can get one free from `News API`_.

.. code-block:: bash

  $ news api YOUR00API00KEY00GOES00HERE

Using newsapi-cli
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    Usage:
      news sources
      news <source>
      news search <keyword>
      news -h | --help
      news --version

Display a list of all news sources

.. code-block:: bash

  $ news sources

Get headlines from a specific source

.. code-block:: bash

  $ news <source>
  
Get headlines related to a keyword

.. code-block:: bash

  $ news search <keyword>

Example
~~~~~~~

Get news headlines from the bbc-news source.

.. code-block:: bash

  $ news bbc-news

Get top news headlines for Great Britain.

.. code-block:: bash

  $ news gb

Get top business news headlines for Great Britain.

.. code-block:: bash

  $ news gb/business

Get top headlines about apple.

.. code-block:: bash

  $ news search apple

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
.. _Python: https://www.python.org
.. _PyPi: https://pypi.python.org/pypi
.. _skele-cli: https://github.com/rdegges/skele-cli
.. _Aziez Ahmed Chawdhary: https://github.com/aziezahmed
.. |PyPI version| image:: https://img.shields.io/pypi/v/newsapi-cli.svg
   :target: https://pypi.python.org/pypi/newsapi-cli

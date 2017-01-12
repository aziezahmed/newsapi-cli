newsapi-cli
===========

*A command line application for displaying news headlines, written in Python.*

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

-  `Python`_

Installing
~~~~~~~~~~

Newsapi-cli is on `PyPi`_ so it can be installed with pip.

.. code-block:: bash

    $ pip install newsapi-cli

Using newsapi-cli
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    Usage:
      news sources
      news <source>
      news -h | --help
      news --version

Display a list of all news sources

.. code-block:: bash

  $ news sources

Get headlines from a specific source

.. code-block:: bash

  $ news <source>

Example
~~~~~~~

Get news headlines from the bbc-news source.

.. code-block:: bash

  $ news bbc-news

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

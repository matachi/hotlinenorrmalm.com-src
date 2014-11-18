===================
Hotlinenorrmalm.com
===================

| Author: Daniel Jonsson
| Code license: `MIT License <LICENSE>`_
| Content license: `CC BY 4.0 <http://creativecommons.org/licenses/by/4.0/>`_

Prerequisites
=============

Install virtualenv on Fedora:

.. code:: shell

  $ sudo yum install python-virtualenv

Setup
=====

Set up a virtualenv:

.. code:: shell

  $ virtualenv -p /usr/bin/python3 env
  $ source env/bin/activate

Install Pelican:

.. code:: shell

  $ pip install pelican

Download the theme:

.. code:: shell

  $ ./setup.py

Build
=====

.. code:: shell

  $ pelican

Development server
==================

.. code:: shell

  $ ./develop_server.sh

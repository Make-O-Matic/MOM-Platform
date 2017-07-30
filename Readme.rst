..
  Copyright (c) 2016-2017 Enproduktion GmbH & Laber's Lab e.U. (FN 394440i, Austria)

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.


Make-o-Matic Platform
=====================

This is the quickstart README for the Make-o-Matic Platform. For further
information, please consult the docs.

MoM Platform is written in Flask, utilising
`Pluggable Views <http://flask.pocoo.org/docs/0.11/views/>`_.


Dependencies
------------

MOM Platform depends on following docker images:

- `makeomaticio/jupyter-openjdk <https://hub.docker.com/r/makeomaticio/jupyter-openjdk/>`_

- `makeomaticio/jupyter-pyspark <https://hub.docker.com/r/makeomaticio/jupyter-pyspark/>`_

Most of the make tasks require ansible to run.


Run MoM Platform flask application locally
---------------------------------

.. code-block:: bash

    mkdir -p ~/.mom/platform/neo4j
    docker-compose up


Run MoM Platform flask application for development
-----------------------------------------

 .. code-block:: bash

    docker-compose -f docker-compose-dev.yml up

 .. code-block:: bash

    virtualenv -p python3.5 ~/VirtualEnvs/mom-platform
    source ~/VirtualEnvs/mom-platform/bin/activate
    pip install -r Requirements
    python mom-platform.py

Don't forget to adapt config.py


Makefile Commands
-----------------

.. code-block:: python

    make tu # runs all unittests specified in the Makefile
    make tuv # runs all unittests specified in the Makefile verbose

    make tf # runs all functional tests
    make tfv # runs all functional tests verbose

    make docs # generates docs
    make clean-docs # cleans the docs

    make provision # run mom.yml ansible on production server

    make update-nginx # update nginx conf on production server
    make update-platform # update flask application on production server
    make update-notebooks # update jupyter notebooks
    make update-jupyter # update jupyter stack
    make update-mongo # update mongo stack
    make update-neo4j # update neo4j stack


Update and install new jupyter packages
---------------------------------------

1. Adapt docker/mom-jupyter/Dockerfile
2. Run make update-jupyter


Edit mongodb rules
------------------

.. code-block:: bash

    ssh your-ip-here
    docker exec -ti ....
    mongo

    use test
    db.createUser(
      {
	user: "",
	pwd: "",
	roles: [
	   { role: "readWrite", db: "test" }
	]
      }
    )


Documentation
-------------

Code MUST be documented using `NumPy rst style <https://github
.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>`_.

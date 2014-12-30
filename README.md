ramlizer
========

A parser for the RAML (RESTful API Modeling Language) file format.

Installation
============

To install the package without using Git, install via easy_install or pip:

    $ easy_install ramlizer

    $ pip install ramlizer
    
Use sudo as required!

To install the Git distribution, use:

    $ git clone https://github.com/SandyChapman/ramlizer.git
    
Then, to use it locally:

    $ cd /path/to/ramlizer/
    $ python setup.py develop
    
Usage
=====

    import ramlizer
    r = ramlizer.RamlFile(open('my-raml-file.raml', 'r'))
    print(r)
    
Some usage for the RamlFile object:

    print(r.root)
    print(r.root.version)
    print(r.root.resources)
    
Outstanding Work
================

Tests and refinements on the API. This project is still quite young, so expect some API
changes over time. 
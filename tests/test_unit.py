import os
from os import path
import re
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from jinja2 import Environment, FileSystemLoader
from code_generator import CodeGenerator
from config import Config
from swagger import Swagger

try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

try:
    basestring
except NameError:
    basestring = str

class TestCodeGenerator(unittest.TestCase):
    def test_initialization(self):
        language = "python"
        cg = CodeGenerator(language)
        t = cg._env.get_template('examples_header.jinja')
        with open('./' + language + '/templates/examples_header.jinja', 'r') as myfile:
            t2=myfile.read().replace('\n', '')
        self.assertEqual(str(t.render()).replace('\n', ''), t2)
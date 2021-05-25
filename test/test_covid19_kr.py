import os,sys
os.path.abspath(os.pardir)
from Covid19.src.covid19_kr import CovidInfokr
import unittest

class TestCovid19Kr(unittest.TestCase):
    def setUp(self):
        self.app = CovidInfokr()

    def test_covid_kr_run(self):
        assert(self.app, -1)
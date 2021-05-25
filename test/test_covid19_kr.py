import os,sys
os.path.abspath(os.pardir)
import unittest
import pytest

class TestCovid19Kr(unittest.TestCase):
    def setUp(self):
        self.app = CovidInfokr()

    def test_covid_kr_run(self):
        pass

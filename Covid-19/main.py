import requests
from bs4 import BeautifulSoup as bs4
import argparse, sys
import covid19_kr, covid19_wd


"""
    field_val = [
        "OBJECTID",
        "PROVINCE_STATE",
        "COUNTRY_REGION",
        "CONFIRMED",
        "DEATHS",
        "RECOVERED"
        ]
"""
    

if __name__ == '__main__':
    covidkr = covid19_kr.CovidInfokr()
    Covidwd = covid19_wd.CovidInfowd()
    status = covidkr.covid_get_data_kr()
    
    
    # Covidwd.show() # terminal output
    Covidwd.jsontocsv()


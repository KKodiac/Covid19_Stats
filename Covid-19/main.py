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
    covidkr = covid19_kr.CovidInfokr() # Korean Stats for Covid-19
    Covidwd = covid19_wd.CovidInfowd() # World Stats for Covid-19
    status = covidkr.covid_get_data_kr() 
    Covidwd.jsontocsv()
    
    # Covidwd.show() # terminal output
    


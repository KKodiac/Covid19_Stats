import covid19_kr, covid19_wd, covid19_nwd, covid19_seoul


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
    # covidkr = covid19_kr.CovidInfokr() # Korean Stats for Covid-19
    covidseoul = covid19_seoul.CovidInfoSeoul() # Seoul Stats for Covid-19
    covidseoul.crawl_and_save_data()
    # status = covidkr.covid_get_data_kr() 
    # Covidwd = covid19_wd.CovidInfowd() # World Stats for Covid-19
    # Covidwd.jsontocsv()
    
    
    
    # N_Covidwd = covid19_nwd.CovidWorldInfo() # new World Stats that has more accurate
    # N_Covidwd.worldTimeseries()
    # N_Covidwd.inputData()             # standings on current state of the
    #                                          # epidemic
    

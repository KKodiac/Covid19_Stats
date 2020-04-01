from src.covid19_kr import CovidInfokr
from src.covid19_wd import CovidWorldInfo
from src.covid19_seoul import CovidInfoSeoul

if __name__ == '__main__':
    covidkr = CovidInfokr() # Korean Stats for Covid-19
    covidkr.covid_get_data_kr()
    
    n_covidwd = CovidWorldInfo() # new World Stats that has more accurate
    n_covidwd.worldTimeseries()
    n_covidwd.inputData()             # standings on current state of the epidemic
    
    seoul = CovidInfoSeoul()
    seoul.crawl_and_save_data()
    
    
    

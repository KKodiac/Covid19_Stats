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
    print("---한국 코로나 관련 현황을 보여줍니다---\n")
    print("Showing current status of Covid-19 in Korea\n")
    print("Data from Korea CDC\n")
    # print("질병관리본부 페이지를 크롤링 합니다.\n")
    # covid = covid19_kr.CovidInfokr(0)
    # status = covid.covid_get_data_kr()
    # print(f"확진자:{status[0]}, 완치:{status[1]}, 사망:{status[2]}\n")
    # print(f"Confirmed : {status[0]}, Recovered : {status[1]}, Deceased : {status[2]}\n")
    
    
    print("---세계 코로나 현황을 보여줍니다---\n") 
    print("---현황을 자세히 보려면 covid_dat.json 파일 참고하세요---\n")
    
    print("---Showing World Covid-19 Status---\n")
    print("---In order to view the status in json format, see covid_dat.json file.\n")
    
    print("")
    
    
    # args = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]
    
    # Covid = covid19_wd.CovidInfowd(args[0], args[1], args[2], args[3], args[4], args[5])
    
    # covidwd = covid19_wd.CovidInfowd(2, "Country_Region='South Korea'", "Country_Region" ,"Confirmed")
    covidwd_all = covid19_wd.CovidInfowd(2, "Confirmed > 0", "*", "Confirmed")
    # covidwd.return_wd_dat()
    covidwd_all.show()
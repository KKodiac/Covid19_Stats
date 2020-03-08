import requests
from bs4 import BeautifulSoup as bs4
from os import path
import json, csv
"""
    API provide by : https://ncov.zeroday0619.kr/
    sub url : {status}/{region}/{location}
    status : 한국 전체 현황을 보여줍니다. Shows status of covid-19 in Korea
    region : 국내 지역마다의 현황을 보여줍니다. Shows regional status of covid-19
    location : 각 지역의 현황을 보여줍니다. Shows specific status of covid-19 in a region
        - seoul         - chungbuk
        - busan         - chungnam
        - daegu         - jeonbuk
        - incheon       - jeonnam
        - gwangju       - gyeongbuk
        - daejeon       - gyeongnam
        - ulsan         - jeju
        - sejong        - gyeonggi
        - gangwon
"""
class CovidInfokr:
    def __init__(self):
        
        self.kr_url= "https://ncov.zeroday0619.kr/kr/"

    def return_kr_dat(self):
        try:
            country_stat = requests.get(path.join(self.kr_url,"status/"))
            regional_stat = requests.get(path.join(self.kr_url,"status/region/"))
        except ConnectionError:
            print("API Request 를 받지 못했습니다.\n")
            exit()
        except TimeoutError:
            print("연결이 원활하지 않습니다.\n")
            exit()
            
        return country_stat, regional_stat
        
        
    def covid_get_data_kr(self):
        ct, rg = self.return_kr_dat()
        ct_json = json.loads(ct.text)
        rg_json = json.loads(rg.text)
        print(rg_json['idr'][0]['SEOUL'].keys())
        region_kr = [
            'SEOUL',    # 0
            'BUSAN',    # 1
            'DAEGU',    # 2
            'INCHEON',  # 3
            'GWANGJU',  # 4
            'DAEJEON',  # 5
            'ULSAN',    # 6
            'SEJONG',    # 7
            'GYEONGGI',  # 8
            'GANGWON',  # 9
            'CHUNGBUK', # 10
            'CHUNGNAM', # 11
            'JEONBUK',  # 12 
            'JEONNAM',  # 13
            'GYEONGBUK', # 14
            'GYEONGNAM', # 15
            'JEJU',      # 16
        ]
        with open('covid_dat_kr.csv', "w+") as file:
            df = csv.writer(file)
            df.writerow(['General Korean Situation (Covid-19)'])
            stats = ['Confirmed', 'Recovered','Deceased', 'Investigated']
            df.writerow(stats)
            df.writerow(ct_json['info'].values())
            df.writerow('')
            
            for cnt, region in enumerate(region_kr):
                data = rg_json['idr'][cnt][region]
                data['Region'] = region
                print(data.keys(), data.values())
                df.writerow(data.keys())
                
                df.writerow(data.values())
                  
                
            
            
            file.close()
        
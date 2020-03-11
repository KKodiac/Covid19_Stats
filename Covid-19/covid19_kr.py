import requests
from bs4 import BeautifulSoup as bs4
from os import path
import json, csv
from time import time, ctime
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
            # country_stat = requests.get(path.join(self.kr_url,"status/"))
            regional_stat = requests.get(path.join(self.kr_url,"status/region/"))
            detail_stat = requests.get(path.join(self.kr_url, "status/inspection/detail"))
        except ConnectionError:
            print("API Request 를 받지 못했습니다.\n")
            exit()
        except TimeoutError:
            print("연결이 원활하지 않습니다.\n")
            exit()
            
        return regional_stat, detail_stat
        
        
    def covid_get_data_kr(self):
        rg, dt = self.return_kr_dat()
        dt_json = json.loads(dt.text)
        rg_json = json.loads(rg.text)
        
        region_kr = [
            'SEOUL',     # 0
            'BUSAN',     # 1
            'DAEGU',     # 2
            'INCHEON',   # 3
            'GWANGJU',   # 4
            'DAEJEON',   # 5
            'ULSAN',     # 6
            'SEJONG',    # 7
            'GYEONGGI',  # 8
            'GANGWON',   # 9
            'CHUNGBUK',  # 10
            'CHUNGNAM',  # 11
            'JEONBUK',   # 12 
            'JEONNAM',   # 13
            'GYEONGBUK', # 14
            'GYEONGNAM', # 15
            'JEJU',      # 16
        ]
        c_date = ctime(time())
        
        with open(f'Data/covid_dat_kr_total_{c_date}.csv', 'w+') as file:
            df = csv.writer(file)
            df.writerow(['General Korean Situation (Covid-19)'])
            keys = ['Iso', 'Quar','Deceased', 'Conf_Test', 'Neg', 'Num_Test', 'Under_Test', 'Total_Test']
            df.writerow(keys)
            
            line = []
            jdata = dt_json['InspectionDetail']
            
            for key in list(jdata.keys()):
                if(key=='ConfirmationPatient'):
                    for sval in list(jdata[key].values()):
                        line.append(sval)
                else:
                    line.append(jdata[key])
            
            
            
            # print(dt_json['InspectionDetail']['ConfirmationPatient'])
            df.writerow(line)
            
            file.close()
            
        with open(f'Data/covid_dat_kr_{c_date}.csv', "w+") as file:
            df = csv.writer(file)
            for cnt, region in enumerate(region_kr):
                
                data = rg_json['region'][cnt][region]
                data['Region'] = region
                
                if(cnt==0):df.writerow(data.keys())
                df.writerow(data.values())
            
            
            file.close()
        
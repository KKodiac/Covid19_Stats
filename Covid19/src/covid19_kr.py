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
        self.c_date = ctime(time())
        self.kr_url= "https://ncov.zeroday0619.dev/v1/kr"
        self.kcdc = "http://ncov.mohw.go.kr/bdBoardList_Real.do?"
        self.data_regional = f'./Covid19/Data/Korea/covid_dat_kr_region.csv'
        self.data_country_kr = f'./Covid19/Data/Korea/covid_dat_kr_total.csv'
        self.date = ctime(time())
        
        
    def return_kr_dat(self):
        try:
            regional_stat = requests.get(path.join(self.kr_url,"status/region/")).json()
            detail_stat = requests.get(self.kcdc)
        except (requests.exceptions.HTTPError,requests.exceptions.Timeout):
            exit()
        
        return regional_stat, detail_stat
    
    
    def read_csv_data(self):
        with open(self.data_regional) as rfile:
            fieldvalues = []
            reader = csv.reader(rfile)
            fieldnames = next(reader, None)
            fieldnames.append(self.date)
            for line in reader:
                fieldvalues.append(line)
                
        return fieldnames, fieldvalues
        
        
    def get_regional_data(self, rg):
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
        
        fieldnames, fieldvalues = self.read_csv_data()
        
        new_values = []
        for cnt, rg_data in enumerate(rg):
            temp = ''
            data = rg_data[region_kr[cnt]]
            
            for cnt, v in enumerate(list(data.values())):
                if(cnt==4):
                    temp+=str(v)
                else: 
                    temp+=(str(v)+'|')
            new_values.append(temp)
                
        with open(self.data_regional, 'w+') as file:
            df = csv.writer(file)
            df.writerow(fieldnames)
            for cnt,value in enumerate(fieldvalues):
                value.append(new_values[cnt])
                df.writerow(value)
            file.close()
            
            
    def get_country_data(self, dt):
        keys = [
            'patient',
            'recovered',
            'deceased',
            'total_confirmed',
            'test_negative',
            'test_accumulate',
            'test_under_exam',
            'test_total',
            'date'
            ]
            
        soup = bs4(dt.text, 'html.parser')
        temp = soup.find(class_='minisize').find_all('td')
        status = [data.text for data in temp]
        status.append(ctime(time()))
        
        if(path.isfile(self.data_country_kr)==False):
            with open(self.data_country_kr, 'w+') as file:
                df = csv.writer(file)
                df.writerow(keys)
                file.close()
                
        with open(self.data_country_kr, 'a+') as file:
            df = csv.writer(file)
            df.writerow(status)
            file.close()
            
            
    def run(self):
        
        rg, dt = self.return_kr_dat()
        self.get_regional_data(rg)
        self.get_country_data(dt)
        



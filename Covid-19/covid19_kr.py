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
        self.kr_url= "https://ncov.zeroday0619.kr/v1/kr/"
        self.kcdc = "http://ncov.mohw.go.kr/bdBoardList_Real.do?"
        self.data_regional = f'Data/Korea/covid_dat_kr_region.csv'
        self.data_country_kr = f'Data/Korea/covid_dat_kr_total.csv'
        
    def return_kr_dat(self):
        try:
            regional_stat = requests.get(path.join(self.kr_url,"status/region/"))
            detail_stat = requests.get(self.kcdc)
        except requests.exceptions.HTTPError:
            print("API Request 를 받지 못했습니다.\n Couldn't connect to Korean API.\n")
            exit()
        except requests.exceptions.Timeout:
            print("연결이 원활하지 않습니다.\n Connection Timed out.\n")
            exit()
            
        return regional_stat, detail_stat
    
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
        
        rg_json = json.loads(rg.text)
        for cnt, region in enumerate(region_kr):
            data = rg_json['region'][cnt][region]
            data['Region'] = region
            if(path.isfile(self.data_regional)==False):
                with open(self.data_regional, 'w+') as file:
                    df = csv.writer(file)
                    data['date'] = ''
                    keys = data.keys()
                    df.writerow(data.keys())
                    file.close()
            else:
                with open(self.data_regional, 'a') as file:
                    df = csv.writer(file)
                    values = data.values()
                    data['date'] = ctime(time())
                    
                    df.writerow(data.values())
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
            
    def covid_get_data_kr(self):
        
        rg, dt = self.return_kr_dat()
        self.get_regional_data(rg)
        self.get_country_data(dt)
        
    ## TODO: re-sort csv data into integrated format in CSSE
    
    def reorginize(self):
        with open(self.data_regional) as data:
            reader = csv.reader(data)
            data_list = [row for row in reader] # entire mod of data from region file
            header = data_list[0]
            del header[-1] # deletes 'date' element in header
            header.reverse() # reverse ['increase', 'patient', 'death', 'ratio', 'inspection', 'Region']
            rev_data_list = [ele[-2::-1] for ele in data_list[1:]]
            
                
                
            


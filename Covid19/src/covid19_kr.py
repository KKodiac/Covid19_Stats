import requests
from bs4 import BeautifulSoup as bs4
from os import path
import json, csv
from time import time, ctime

"""
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
        self.kcdc_main = "http://ncov.mohw.go.kr/"
        self.kcdc = "http://ncov.mohw.go.kr/bdBoardList_Real.do?"
        self.data_regional = f'./Covid19/Data/Korea/covid_dat_kr_region.csv'
        self.data_country_kr = f'./Covid19/Data/Korea/covid_dat_kr_total.csv'
        self.date = ctime(time())
        
        
    def return_kr_dat(self):
        try:
            regional_stat = requests.get(self.kcdc_main)
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
        
    def crawl_regional_data(self,rg):
        soup = bs4(rg.content, 'html.parser')
        
        rlist = []
        for i in range(18):
            data_html = soup.find(class_="rpsa_detail").find(id="map_city"+str(i+1)).find('ul')
            incr = data_html.find(class_="sub_num").text
            tincr = ''.join(e for e in incr if e.isalnum())
            rlist.append(tincr)
            for cnt,i in enumerate(data_html.find_all(class_="num")):
                
                tincr = ''.join(e for e in i.text if (e.isalnum() or (e=='.')))
                rlist.append(tincr)
            
        return rlist
        
    def get_regional_data(self, rg):
        fieldnames, fieldvalues = self.read_csv_data()
        # list inside list
        rlist = self.crawl_regional_data(rg) 
        # 서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 검역
        # every 5 element is a data for a region
        new_values = []
        tmp = ''
        for cnt, data in enumerate(rlist):
            if((cnt+1)%5==0):
                tmp += data
                new_values.append(tmp)
                tmp = ''
            else:
                tmp += (data + '|')
              
                
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
        



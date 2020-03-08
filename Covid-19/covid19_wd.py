"""
Because the original dataset is intended to create a geomap of spread of the Covid-19, render data will be occasionally viewed
For more information of the NCOV api, visit https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/layers
데이터 셋이 기존 코로나-19 의 바이러스 매핑을 위해 만들어 졌기 때문에 데이터 아웃풋이 GEOMETRIC 관련된 것이 자주 나옵니다.
API 에 대한 자세한 정보를 알고 싶으면, https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/layers 를 방문하세요

Query Note:

    LABEL: [0:Deaths, 1:Cases, 2:Cases_country]
    f: File Format ['html', 'json']
    where: [
        Fields:[
            OBJECTID,PROVINCE_STATE,COUNTRY_REGION,LAST_UPDATE,LAT,LONG,CONFIRMED,DEATHS,RECOVERED
            ]
        ]  " + <>= + [NUM]"
        
    outFields: Json 으로 반환 될 Field 값을 지정합니다. Assigns Fields value to be returned in Json format
                [DEFAULT=*,
                Fields:[
                    OBJECTID,PROVINCE_STATE,COUNTRY_REGION,LAST_UPDATE,LAT,LONG,CONFIRMED,DEATHS,RECOVERED
                    ] 
                ]
    orderByFields: "Fields-value%value"
    
"""

import csv, json, sys
from os import path
import json 
import requests

service_link = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/{}/"
query_syn = "query?f={}&where={}&outFields={}&orderByFields={}"

# 0 shows a list of Countries and Chinese provinces only, where cases of death has occured 
## returns all field values
# 1 shows a list of Countries and Chinese provinces with Confirmed cases
## returns all field values
# 2 shows a list of Countries only with Confirmed cases
## returns all field values

label_death = 0
label_casses = 1
label_country = 2

class CovidInfowd:
    def __init__(self, label=2, wfield="", ofield="*", orderfield="",fformat="json"):
        self.label = label
        self.wfield = wfield
        self.ofield= ofield
        self.orderfield = orderfield
        self.fformat = fformat
    
    def covid_get_data(self):
        slink = service_link.format(self.label)
        qlink = query_syn.format(self.fformat, self.wfield, self.ofield, self.orderfield)
        data_url = path.join(slink, qlink)
        # print(data_url)
        jtext = requests.get(data_url).text
        
        return jtext 
        
        
        
    def return_wd_dat(self):
        data = self.covid_get_data()
        dumped = json.loads(data)
        with open("covid_dat.json", "w+") as file:
            json.dump(dumped['features'], file, sort_keys=True, indent=4)
            
        return dumped 
        
    def show(self):
        json_dump = self.return_wd_dat()
        data = json_dump["features"]
        for row in data:
            print(row['attributes'])
        
        
    def jsontocsv(self):
        inputFile = open("covid_dat.json")
        outputFile = open("covid_dat.csv", 'w+')
        data = json.load(inputFile)
        inputFile.close()
        output = csv.writer(outputFile)
        # print(data['features'])
        output.writerow(data[0]['attributes'])
        print(data[0]['attributes'].values())
        # output.writerow(data[0].keys())
        for row in data:
            output.writerow(row['attributes'].values())
            
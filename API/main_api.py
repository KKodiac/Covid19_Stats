from fastapi import FastAPI
from os.path import join
import csv 

covid_api = FastAPI()

data_root = {
    "data_root": "../Covid-19/Data/",
    "data_root_kr": "Korea/",
    "kr_seoul_timeseries": "seoul_timeseries/",
    "data_root_wd": "World/",
    "wd_world_timeseries": "world_timeseries/",
}

file_path = {
    "kr_regional_dat": "covid_dat_kr_region.csv",
    "kr_all_dat": "covid_dat_kr_total.csv",
    "wd_new_dat": "new_covid_dat.csv",
    "wd_dat": "covid_dat.csv"
}



@covid_api.get("/")
async def root():
    return {"message": "HELLO WORLD"}
    
@covid_api.get("/Korea/")
async def korea_status():
    path = join(data_root["data_root"], data_root["data_root_kr"])
    return {"message" : f"{path}"}


@covid_api.get("/World/")
async def world_status():
    path = join(data_root["data_root"],data_root["data_root_wd"])
    return {"message" : f"{path}"}
# This one gets all table data text
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from urllib.parse import urlparse

# access to seoul corona data panel
url = "http://www.seoul.go.kr/coronaV/coronaStatus.do"

# create dummy dataframe
dummy_data1 = {}
df = pd.DataFrame(dummy_data1)

# get page content response from the web using requests and beautifulsoup
res = requests.get(url)
soup = BeautifulSoup(res.content, "lxml")

# use table html tag to find tables in the webpage:
tables = soup.find_all("table")
print(len(tables))

# crawl all table data from the webpage: this includes unwanted data
for i in range(0, len(tables)):
    # using panda's read_html to crawl tabledata
    df_crawl = pd.read_html(str(tables[i]), encoding="utf-8", header=0)[0]
    # save as csv file
    df_crawl.to_csv(
        "/Users/noopy/_forks/Covid19_Stats/Covid-19/Data/Korea/seoul_timeseries/"
        + str(i)
        + ".csv"
    )

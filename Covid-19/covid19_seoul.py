# This one gets all table data text
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv


class CovidInfoSeoul:

    """
    Seoul Covid Confirmed cases crawler
    데이터출처: 서울시청 홈페이지 http://www.seoul.go.kr/coronaV/coronaStatus.do
    data source: http://www.seoul.go.kr/coronaV/coronaStatus.do
    """

    def __init__(self):
        # access to seoul corona data panel
        self.scrape_url = "http://www.seoul.go.kr/coronaV/coronaStatus.do"

    def crawl_and_save_data(self):
        # create dummy dataframe
        dummy_data1 = {}
        df = pd.DataFrame(dummy_data1)

        # get page content response from the web using requests and beautifulsoup
        res = requests.get(self.scrape_url)
        soup = BeautifulSoup(res.content, "lxml")

        # use table html tag to find tables in the webpage:
        tables = soup.find_all("table")
        # print(len(tables))

        # crawl all table data from the webpage: this includes unwanted data
        for i in range(0, len(tables)):
            # using panda's read_html to crawl tabledata
            df_crawl = pd.read_html(str(tables[i]), encoding="utf-8", header=0)[0]
            # save as csv files
            df_crawl.to_csv("./Data/Korea/seoul_timeseries/" + str(i) + ".csv")

        # validate all collected csv data from seoul, save and merge confirmed cases as csv file
        df_confirmed = pd.DataFrame(dummy_data1)
        for i in range(0, len(tables)):
            # read all csv files in folder
            df_not_validated = pd.read_csv(
                "./Data/Korea/seoul_timeseries/" + str(i) + ".csv"
            )

            if len(df_not_validated.index) < 10:
                pass
            else:
                columns_list = df_not_validated.columns
                if "환자" in columns_list:
                    # print(df_not_validated.head())
                    df_confirmed = pd.concat([df_confirmed, df_not_validated])

        df_confirmed.to_csv("./Data/Korea/covid_dat_seoul.csv")
        print("Seoul's data crawled and merged")

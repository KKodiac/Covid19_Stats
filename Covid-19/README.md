# `COVID-19`
코로나-19 에 대한 확진/완치/사망 에 대한 국내, 해외 정보를 수집합니다. <br />
Data scrapes Covid-19 Confirmed/Cured/Deceases Cases.

## Contents - Daily Stat Records(Starting from 2020-03-09)

* Time recording is based on UTC (+0900 for KST)
* 자료 파일의 시간은 UTC 기준입니다.(UTC+0900가 한국기준시 입니다.)
* [Korea - Covid-19 Daily Statistics](./Data/Korea)
* [World - Covid-19 Daily Statistics](./Data/World)

### Covid19 Korea Data / 코로나 한국 자료 

* [zeroday0619/COVID-19API](https://github.com/zeroday0619/COVID-19API/) 에서 제공하신 국내 동향 조회 API를 활용합니다.
  [Documentaion on above API](https://ncov.zeroday0619.kr/redoc/)
* [KCDC - 대한민국 질병관리 본부](http://ncov.mohw.go.kr/bdBoardList_Real.do?) API에서 크롤링 한 국내 자료 입니다.
 By following the link above, you can view the entire situation in Korea. There are also links provided by Korean Local Governments on the lower side of the page.
  There are up-to-date situation reports about each individual local government. 
 위에 링크를 활용하면 각 시도에서 제공하는 지역별 코로나 현황을 볼 수 있습니다. 대한민국 짱 
* [서울시청 홈페이지](http://www.seoul.go.kr/coronaV/coronaStatus.do)에서 서울시의 확진자 데이터를 csv 파일 형태로 스크레이프 합니다
#### Data / 데이터

* [covid_dat_kr_region](./Data/Korea/covid_dat_kr_region.csv) 
  * Returns regional status of Covid-19 in South Korea.
  * 코로나 바이러스의 지역적 한국 현황을 보여줍니다.
* [covid_dat_kr_total](./Data/Korea/covid_dat_kr_total.csv) 
  * Returns total status of Covid-19 in South Korea.
  * 코로나 바이러스의 전체적인 한국 현황을 보여줍니다.
* [covid_dat_seoul](./Data/Korea/covid_dat_seoul.csv) 
  * Returns Seoul's confirmed cases of Covid-19.
  * 서울 시의 확진자 현황을 보여줍니다

### Covid19 World Data

* [CSSEGISandData/CODIV-19](https://github.com/CSSEGISandData/COVID-19) 에서 사용 중인 ArcGIS API를 활용합니다. 
* [WorldOMeters](https://www.worldometers.info/coronavirus/#countries) 에서 데이터를 스크래이프 합니다.

#### Try it out
```
Field: 
    "OBJECTID",
    "PROVINCE_STATE",
    "COUNTRY_REGION",
    "CONFIRMED",
    "DEATHS",
    "RECOVERED"
```

* Example / 예시
```
python3 main.py
​```Look for results in /Data/ folder```
```

* Returns in JSON format in order from least to most Confirmed cases.

Documents about ArcGIS FeatureService Rest API can be found here:<br />
[ArcGIS-FeatureService](https://developers.arcgis.com/rest/services-reference/feature-service.htm)
[ArcGIS-FeatureService(Layer)](https://developers.arcgis.com/rest/services-reference/query-feature-service-layer-.htm)


### JSON data

 Data scraped from the API is returned in JSON format into `covid_dat.json` file.
 API 에서 크롤된 자료는 `covid_dat.json` 파일에 반환됩니다.
 이 후 `covid_dat.csv` 파일로 정리 됩니다.
## Built With/사용된 파이썬 모듈

* [Python3](https://www.python.org/doc)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
- [Requests](https://requests.readthedocs.io/en/master/)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

## Author


* **Sean Hong(홍성민)** 
* 현재 군인 현역으로 있는 학생이기 때문에 많이 부족합니다. 보완점을 가르쳐주시면 감사하겠습니다!
* Any lacking parts in my code are welcome to any suggestions and criticism.

## Contributors

- [Young-jin Ahn (안영진)](https://github.com/snoop2head)

## Acknowledgments


* World data scraped from - *github repo* - [Covid-19](https://github.com/CSSEGISandData/COVID-19) - [Service](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer)
* [WorldOMeters](https://www.worldometers.info/coronavirus/#countries).
* Korea data scraped from / 한국데이터 출처는 다음과 같습니다:
  * [질병관리본부(Korea CDC)](http://ncov.mohw.go.kr/index_main.jsp)
  * [zeroday0619/COVID-19API](https://github.com/zeroday0619/COVID-19API/)
  * [서울시청 홈페이지: Seoul City webpage](http://www.seoul.go.kr/coronaV/coronaStatus.do)

### Any problems please contact me at [seanhong2000@gmail.com](seanhong2000@gmail.com)

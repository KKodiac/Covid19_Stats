# Covid19-Scraper
코로나-19 에 대한 확진/완치/사망 에 대한 한국, 해외 정보를 수집합니다. <br />
Data scrapes Covid-19 Confirmed/Cured/Deceases Cases in Korea and rest of the World.<br />

## Contents 

* Time recording is based on UTC (+0900 for KST) 
* 자료 파일의 시간은 UTC 기준입니다.(UTC+0900가 한국기준시 입니다.)

### [Korea - Covid-19 Daily Statistics](./Covid-19/Data/Korea)

* [covid_dat_kr_region](./Covid-19/Data/Korea/covid_dat_kr_region.csv) 
  * Returns regional status of Covid-19 in South Korea.
  * 코로나 바이러스의 지역적 한국 현황을 보여줍니다.
    ```
      [Increased # of patients compared to day before] | [Total # of patients] | [Total # of Recovered] | [Total # of Deceased] | [Ratio of Incidence / 100k Population]
    ```
  * Or more simply just: 'increase'	'patient'	'recovered' 'deceased' '/100k pop'
* [covid_dat_kr_total](./Covid-19/Data/Korea/covid_dat_kr_total.csv) 
  * Returns total status of Covid-19 in South Korea.
  * 코로나 바이러스의 전체적인 한국 현황을 보여줍니다.
* [covid_dat_seoul](./Covid-19/Data/Korea/covid_dat_seoul.csv) 
  * Returns Seoul's confirmed cases of Covid-19.
  * 서울 시의 확진자 현황을 보여줍니다

### [World - Covid-19 Daily Statistics](./Covid-19/Data/World)

* [CSSEGISandData/CODIV-19](https://github.com/CSSEGISandData/COVID-19) 에서 사용 중인 ArcGIS API를 활용합니다. 
* [WorldOMeters](https://www.worldometers.info/coronavirus/#countries) 에서 데이터를 스크래이프 합니다.



## Getting Started

### Prerequisites
Create a virtual environment.<br />
파이썬 가상환경을 만드세요.<br />
```
python3 -m venv .covid
```
Install modules in `requirements.txt`.<br /><br />
`requirements.txt` 에 있는 파이썬 모듈을 다운 받으세요.<br />
```
python3 -m pip install -r requirements.txt
```
### For Visualization of Korean Regional dataset
* Add These two lines to main.py
```
...
...
from Web import web

if __name__ == '__main__':
 ...
 ... # And comment out These lines
 ...
  web.app.run(port=8080, debug=True)
```
## Built With/사용된 파이썬 모듈
* [Python3](https://www.python.org/doc)<br />
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) <br />
- [Requests](https://requests.readthedocs.io/en/master/)<br />
- [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

## Authors

* **Sean Hong(홍성민)** <br />
-현재 군인 현역으로 있는 학생이기 때문에 많이 부족합니다. 보완점을 가르쳐주시면 감사하겠습니다!<br />
-Any lacking parts in my code are welcome to any suggestions and criticism.<br />

## Contributors

- [Young-jin Ahn (안영진)](https://github.com/snoop2head)

## Acknowledgments

* World data scraped from - *github repo* - [Covid-19](https://github.com/CSSEGISandData/COVID-19) - [Service](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer)
* [WorldOMeters](https://www.worldometers.info/coronavirus/#countries)
* Korea data scraped from / 한국데이터 출처는 다음과 같습니다:
  * [질병관리본부(Korea CDC)](http://ncov.mohw.go.kr/index_main.jsp)
  * [zeroday0619/COVID-19API](https://github.com/zeroday0619/COVID-19API/)
  * [서울시청 홈페이지: Seoul City webpage](http://www.seoul.go.kr/coronaV/coronaStatus.do)

### Any problems please contact me at seanhong2000@gmail.com


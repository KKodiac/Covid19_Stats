# COVID-19 Stats and Visualizations
코로나-19 에 대한 확진/완치/사망 에 대한 국내, 해외 정보를 수집합니다. <br />
추가적으로 매일 데이터에 대한 시각적 자료 또한 간단하게 제공합니다. <br />
Data scrapes Covid-19 Confirmed/Cured/Deceases Cases. <br />
Additionally provides simple visualization of Today's data.


## Contents 
* [그냥 Heroku가 뭔지 알아보려고 만들어본 웹](https://covidstatsweb.herokuapp.com/map/korea)
  - 여기서 업데이트 자동화 구현해보기(웹에서 자동으로 끌어와서 깃헙 푸쉬까지)
* Time recording is based on UTC (+0900 for KST) 
* 자료 파일의 시간은 UTC 기준입니다.(UTC+0900가 한국기준시에용.)

### Korea - Covid-19 Daily Statistics

* [covid_dat_kr_region](https://github.com/KKodiac/Covid19_Stats/tree/master/map/src/data/Korea/covid_dat_kr_region.csv) 
  * Returns regional status of Covid-19 in South Korea.
   ```
      [Increased # of patients compared to day before] | 
      [Total # of patients] | [Total # of Quarantine] | [Total # of Recovered] | [Total # of Deceased] |
      [Ratio of Incidence / 100k Population]
    ```
   * Or more simply just: 'increase'	'patient'	'quarantine' 'recovered' 'deceased' '/100k pop'
  
  * 코로나 바이러스의 지역적 한국 현황을 보여줘요.
   ```
      [전날 대비 환자 증가 수] | 
      [전체 환자 수] | [전체 격리인원 수] | [전체 완치자 수] | [전체 사망자 수] |
      [10만 인구 당 증가율]
    ```
  * 간단하게: 증가, 환자, 격리, 완치, 사망, /10만인구 당 비율
  
* [covid_dat_kr_total](https://github.com/KKodiac/Covid19_Stats/tree/master/map/src/data/Korea/covid_dat_kr_total.csv) 
  * Returns total status of Covid-19 in South Korea.
  * 코로나 바이러스의 전체적인 한국 현황을 보.
  
* [covid_dat_seoul](https://github.com/KKodiac/Covid19_Stats/tree/master/map/src/data/Korea/covid_dat_seoul.csv) 
  * Returns Seoul's confirmed cases of Covid-19.
  * 서울 시의 확진자 현황을 보여줘요

### World - Covid-19 Daily Statistics

* [new_covid_dat.csv](https://github.com/KKodiac/Covid19_Stats/blob/master/map/src/data/World/new_covid_dat.csv)
  * Stats of Covid19 in Countries world around.
  * 세계 나라들의 코로나 현황을 보여줘요

## Built With / 사용된 도구
* [Python3](https://www.python.org/doc)<br />
  * [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) <br />
  * [Requests](https://requests.readthedocs.io/en/master/)<br />
  * [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)
* [Google Charts API](https://developers.google.com/chart)
* [Heroku](https://covidstatsweb.herokuapp.com/map/korea)

## Authors

* **Sean Hong(홍성민)** <br />
-학생이기 때문에 많이 부족합니다. 보완점을 가르쳐주시면 감사하겠습니다!<br />
-Any lacking parts in my code are welcome to any suggestions and criticism.<br />

## Contributors

- [Young-jin Ahn (안영진)](https://github.com/snoop2head)

## Acknowledgments

* [Google Charts API](https://developers.google.com/chart)
* World data scraped from
    - [WorldOMeters](https://www.worldometers.info/coronavirus/#countries)
* Korea data scraped from / 한국데이터 출처는 다음과 같습니다:
    - [질병관리본부(Korea CDC)](http://ncov.mohw.go.kr/index_main.jsp)
    - [서울시청 홈페이지: Seoul City webpage](http://www.seoul.go.kr/coronaV/coronaStatus.do)

### Any problems please contact me at seanhong2000@gmail.com


# Covid19-Scraper
코로나-19 에 대한 확진/완치/사망 에 대한 국내, 해외 정보를 수집합니다. 
Data scrapes Covid-19 Confirmed/Cured/Deceases Cases.

## Getting Started
### Prerequisites
Create a virtual environment.
파이썬 가상환경을 만드세요.
```
python3 -m venv .covid
```
Install modules in `requirements.txt`.
`requirements.txt` 에 있는 파이썬 모듈을 다운 받으세요.
```
python3 -m pip install -r requirements.txt
```

## Built With/사용된 파이썬 모듈
* [Python3](https://www.python.org/doc)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
- [Requests](https://requests.readthedocs.io/en/master/)

## Authors

* **Sean Hong(홍성민)** 

## Acknowledgments

* World data scraped from - *github repo* - [Covid-19](https://github.com/CSSEGISandData/COVID-19) - [Service](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer)
* Korea data scraped from [질병관리본부(Korea CDC)](http://ncov.mohw.go.kr/index_main.jsp)


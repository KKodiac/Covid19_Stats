import requests
from bs4 import BeautifulSoup as bs4

kr_covid_url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncvContSeq=&contSeq=&board_id=&gubun="


class CovidInfokr:
    def __init__(self, url_label, kr_url=kr_covid_url):
        self.url_label=url_label
        self.kr_url=kr_url

    def return_kr_dat(self):
        try:
            url = requests.get(self.kr_url)
        except ConnectionError:
            print("한국 질병관리본부에서 Request 를 받지 못했습니다.\n")
            exit()
        except TimeoutError:
            print("연결이 원활하지 않습니다.\n")
            exit()
            
        html = url.text
        soupify = bs4(html,'html.parser')
        
        return soupify
        
        
    def covid_get_data_kr(self):
        soup = self.return_kr_dat()
        
        data = soup.table('tr')
        
        parse = {"confirmed": data[0].find('td').text, "Cured": data[1].find('td').text, "Deceased": data[2].find('td').text}
        status = [parse["confirmed"], parse["Cured"], parse["Deceased"]]
        
        return status
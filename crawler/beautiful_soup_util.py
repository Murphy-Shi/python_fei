import requests

from common.log_util import *
from bs4 import BeautifulSoup


class BeautifulSoupUtil:
    def __init__(self, url: str):
        self.url = url
        self.html = ""

    def get_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content.decode("utf-8", "ignore").encode("gbk", "ignore")

    def ba4_paraser(self):
        all_value = []
        soup = BeautifulSoup(self.html, 'html.parser')
        print(soup)

    def stary(self):
        self.html = self.get_page()
        self.ba4_paraser()



if __name__ == '__main__':
    url = "http://www.icbc.com.cn/ICBC/%E7%BA%AA%E5%BF%B5%E5%B8%81%E4%B8%93%E5%8C%BA/default.htm"
    BeautifulSoupUtil(url).stary()
# soup = BeautifulSoup("<html>data</html>")

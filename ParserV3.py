import re
import requests
from bs4 import BeautifulSoup
url = "https://api.coinmarketcap.com/content/v3/news?coins=1&page=1&size=5"
data = {
    'coins': '1',
    'page': '1',
    'size': '5',
    }
Headers = {
    'referer': 'https://coinmarketcap.com/',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    }
def get_html(url):
    r = requests.get(url,headers = Headers,params = data)
    return r.json()
def get_title(json):
    a = []
    for i in json['data']:
        a.append(i['meta']['title'])
    return a
def get_subtitle(json):
    a = []
    for i in json['data']:
        a.append(i['meta']['subtitle'])
    return a
def print_news(a,b):
    for i in range(len(a)):
        print(a[i],'\n')
        print(b[i],'\n')
        print("-----------------------------------------------------")
    pass
print_news(get_title(get_html(url)),get_subtitle(get_html(url)))

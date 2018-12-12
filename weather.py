import requests
from bs4 import BeautifulSoup
import json
import re
import random

def weather(string):

  if '台' in string and '台東' not in string:
    string = '臺' + string[1]
  url = 'https://www.cwb.gov.tw/V7/'
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

  resp = requests.get(url, headers=headers)
  #use UTF-8
  resp.encoding = resp.apparent_encoding
  soup = BeautifulSoup(resp.text,"html.parser")
  # sel = soup.find_all(title=re.compile(' '))
  sel_city = soup.select("div#divTitle a")
  flag = 0
  for city in sel_city:
    if flag == 0:
      for untaged in city:
        if string in untaged:
          return_url = 'https://www.cwb.gov.tw' + city['href']
          flag = 1
  # print(return_url)
  return return_url

# weather('宜蘭')
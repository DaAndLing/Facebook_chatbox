import requests
from bs4 import BeautifulSoup
import json
import re
import random

def weather(string):
  city_list = {'台北':"Taipei_City.htm", '新北':"New_Taipei_City.htm",
               '桃園':"Taoyuan_City.htm", '台中':"Taichung_City.htm",
                '台南':"Tainan_City.htm", '高雄':"Kaohsiung_City.htm",
                "基隆":"Keelung_City.htm", '新竹':"Hsinchu_City.htm",
                '苗栗':"Miaoli_County.htm", '彰化':"Changhua_County.htm",
                '南投':"Nantou_County.htm", '雲林':"Yunlin_County.htm",
                '嘉義':"Chiayi_City.htm", '嘉義':"Chiayi_County.htm",
                '屏東':"Pingtung_County.htm", '宜蘭':"Yilan_County.htm",
                '花蓮':"Hualien_County.htm", '台東':"Taitung_County.htm",
                '澎湖':"Penghu_County.htm", '金門':"Kinmen_County.htm",
                '連江':"Lienchiang_County.htm"}

  return_url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/' + city_list[string]
  print(return_url)
  return return_url

# weather('屏東')
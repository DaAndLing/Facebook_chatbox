#藉由首頁取得所有文章的URL
import requests
from bs4 import BeautifulSoup
import json
import re
import random

def pic_url(category):
    print(category)
    p = requests.Session()

    url = 'https://www.dcard.tw/f/' + category
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text,"html.parser")
    # sel = soup.select("div.PostList_wrapper_2BLUMj a.PostEntry_root_V6g0rd")
    sel = soup.find_all(href=re.compile("/f/" + category))

    article_href = []
    for s in sel:
        # substring = "/f"
        if ("/f/" + category + "/p/") in str(s["href"]):
            article_href.append(s["href"])

    #article_href[2] is because there are 2 board-relative topics
    url = "https://www.dcard.tw"+ article_href[2]

    #broaden website by continuously refresh
    for k in range(0,10):
            post_data={
                "before":article_href[-1][9:18],
                "limit":"30",
                "popular":"true"
            }
            r = p.get("https://www.dcard.tw/_api/forums/" + category + "/posts",params=post_data, headers = { "Referer": "https://www.dcard.tw/", "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'})
            data2 = json.loads(r.text)
            for u in range(len(data2)):
                Temporary_url = "/f/" + category + "/p/"+ str(data2[u]["id"]) + "-" + str(data2[u]["title"].replace(" ","-"))
                article_href.append(Temporary_url)

    # requests.session().close()
    #find an article with pictures
    url = "https://www.dcard.tw"+article_href[random.randint(3,len(article_href) - 1)]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text,"html.parser")
    # sel_jpg = soup.select("div.Post_content_NKEl9d div div div img.GalleryImage_image_3lGzO5")
    sel = soup.find_all(class_=re.compile("GalleryImage_imag"))
    while len(sel) == 0:
        url = "https://www.dcard.tw"+ article_href[random.randint(3,len(article_href) - 1)]
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text,"html.parser")
        sel = soup.find_all(class_=re.compile("GalleryImage_imag"))
    
    requests.session().close()
    p.close()

    #only print one picture
    # print(sel[0]["src"])
    return sel[0]["src"]

# pic_url("pet")
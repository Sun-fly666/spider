import re
import requests
from bs4 import BeautifulSoup
import os

fold = "./bilibili_header_img"

if not os.path.exists(fold):
    os.makedirs(fold)


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

url = "https://www.bilibili.com/"

text = requests.get(url=url, headers = headers).text

print(text)
ex = r'<div class = "live-card".*?<img src="(.*?)@.*?>'

result = re.findall(ex, text, re.S)

print(result)
# for src in result:
#
#     if not src.startswith("https"):
#         img_link = "https:" + src
#
#     img_name = src.split('/')[-1]
#
#     print(img_link)
#     img_data = requests.get(url=img_link, headers=headers).content
#     img_path = fold + "/" + img_name
#     with open(img_path, "wb") as f:
#        f.write(img_data)





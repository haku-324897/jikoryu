import requests
from bs4 import BeautifulSoup
import time

urls=[
    "https://www.askul.co.jp/p/AW33947/",
    "https://www.askul.co.jp/p/542680/",
    "https://www.askul.co.jp/p/617360/",
    "https://www.askul.co.jp/p/1166666/",
]

for url in urls:
    
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    title = soup.title.string.removesuffix(" - アスクル")


    price_tag = soup.find("span",class_="a-price_value")
    price = price_tag.string
    if price_tag :
        price = price_tag.string
    else:
        price = "価格ない！！"

    kosuu = soup.find("h2",class_="a-heading_text")
    if kosuu:
        kosuu = kosuu.string.replace("販売単位：","")
    else:
        kosuu = "個数ない！！"


    jan="janコードない！！"
    for span in soup.find_all("span"):
        if span.string and "／JANコード：" in span.string:
            jan=span.string.replace("／JANコード：","")
            break #for文を抜ける!!

    print(title)
    print(price)
    print(kosuu)
    print(jan)
    print("")
    time.sleep(0.5)
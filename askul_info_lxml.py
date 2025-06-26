import requests
from lxml import html
import time

urls=[
    "https://www.askul.co.jp/p/AW33947/",
]

for url in urls:

    res = requests.get(url)
    tree = html.fromstring(res.content)

    title_list = tree.xpath("//title/text()")
    if title_list:
        title = title_list[0].removesuffix(" - アスクル")
    else:
        title = "タイトルない！！"

    price_list = tree.xpath('//span[@class="a-price_value"]/text()')
    if price_list:
        price = price_list[0]
    else:
        price = "価格ない！！"
 
    quantity_list = tree.xpath('//h2[@class="a-heading_text"]/text()')
    if quantity_list:
        quantity = quantity_list[0].replace("販売単位：","")
    else:
        quantity = "個数ない！！"

    jan_list = tree.xpath('//span[contains(text(), "／JANコード：")]/text()')
    if jan_list:
        jan = jan_list[0].replace("／JANコード：","")
    else:
        jan = "JANない！！"


print(title)
print(price)
print(quantity)
print(jan)

time.sleep(0.5)
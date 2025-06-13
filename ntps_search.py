import requests
from bs4 import BeautifulSoup
import time


session = requests.Session()

top_url = "https://www.ntps-shop.com/shop/wellstech/"
session.get(top_url)


product_url = "https://www.ntps-shop.com/product/6679541/"
res = session.get(product_url)

# 取得したページをスクレイピング
soup = BeautifulSoup(res.text, "html.parser")
title = soup.title.string.removesuffix(" | GIF-TECHs SHOP")
print(title)  
import requests
from lxml import html
import time


session = requests.Session()
top_url = "https://www.ntps-shop.com/shop/wellstech/"
session.get(top_url)

# 処理したいJANコードのリスト
jancodes = [
    "4901080563910",
    "4901681503513",
    "4901681502516",
    "4971850145202",
    "4549526602887",
    "4971850123194",
]

for jancode in jancodes:
    search_url = f"https://www.ntps-shop.com/search/res/{jancode}/"
    res = session.get(search_url)
    tree = html.fromstring(res.content)

    #変数の初期化
    product_id = ""
    
    # パターン1:商品ページが複数ある場合、一番上のリンクを取得
    product_link_list = tree.xpath('//td[@class="tano-center"]/a/@href')
    if product_link_list:
        product_id = product_link_list[0]

    else:
        # パターン2:商品ページが1つの場合、そのリンクを取得
        product_link_list = tree.xpath('//div[@class="tano-item-detail-right"]/a/@href')
        if product_link_list:
            product_id = product_link_list[0]
        else:
            # パターン3:商品ページがない場合、空文字列を返す
            product_id = ""
    
    #
    if product_id:
        #1: 商品ナンバー以外の情報を削除
        product_id_kai = product_id.split('?')[0]

        #2: 商品の完全なURLを作成
        base_url = "https://www.ntps-shop.com"
        product_url = base_url + product_id_kai
    
        #3: 商品ページから情報を取得
        gif_res = session.get(product_url)
        gif_tree = html.fromstring(gif_res.content)

        #3-1: 商品名を取得
        gif_name_list = gif_tree.xpath('//h1[@id="tano-h1"]/span/text()')
        if gif_name_list:
            gif_name = gif_name_list[0]
        else:
            gif_name = ""
        
        #3-2: 商品価格を取得
        gif_price_list = gif_tree.xpath('//span[@id="tano-sale-price"]/span/text()')
        if gif_price_list:
            gif_price = gif_price_list[0]
        else:
            gif_price = ""

        #3-3: 商品数量を取得
        gif_quantity_list = gif_tree.xpath('//dl[@class="tano-product-stock-left clearfix"]/dd/text()')
        if gif_quantity_list:
            gif_quantity = gif_quantity_list[0]
        else:
            gif_quantity = ""
        
        #3-4: 商品申し込み番号を取得
        gif_number_list = product_id_kai.split('/')[2]
        if gif_number_list:
            gif_number = gif_number_list
        else:
            gif_number = ""
        
        print(gif_name)
        print(gif_price)
        print(gif_quantity)
        print(gif_number)
        time.sleep(0.5)

    else:
        product_url = ""
        time.sleep(0.5)




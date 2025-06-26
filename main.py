import streamlit as st
import pandas as pd
import re
import time
import requests

st.title("アスクル&Gif_shop商品情報取得")
st.write("JANコードから商品情報をまとめて検索できるアプリです。")

askul_input =st.text_input("アスクルの商品番号を入力してください")

#検索ボタン
if st.button("検索"):
    if askul_input:
        #ダミーデータ
        date = {
            "サイト": ["アスクル", "Gif_shop"],
            "商品名": ["アスクル商品名", "Gif_shop商品名"],
            "価格": ["1000円", "950円"],
            "個数": ["1個", "1個"],
            "JANコード": ["1234567890123", "1234567890123"],
            "商品番号": ["AW12345", "GS54321"]
        }
        df=pd.DataFrame(date)
        st.dataframe(df)
    else:
        st.warning("何もかいてないよ！！")
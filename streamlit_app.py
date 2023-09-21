# Streamlitライブラリをインポート
import streamlit as st
import random
st.title('おみくじ')
if st.button("おみくじを引く"):
    results=["大吉","中吉","小吉","吉","凶","大凶"]
    result=random.choice(results)
    st.write(f"結果:{result}")

if st.button("今日のラッキーカラー"):
    result=["赤","青","黄色","緑","紫","黒","白"]
    result=random.choice(results)
    st.write(f"結果:{result}")
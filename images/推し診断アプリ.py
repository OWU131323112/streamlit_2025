import streamlit as st
import os

# 背景色を薄紫色に設定
page_bg_color = """
<style>
    body {
        background-color: #f3e5f5;
    }
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

st.title(" 推しキャラ紹介＆診断アプリ ")

# キャラ一覧（相対パスで指定）
characters = {
    "須王芦佳": {
        "image": "images/須王.PNG",
        "bio": "愛され無能のトラブルメーカー！"
    },
    "樋宮明星": {
        "image": "images/樋宮.PNG",
        "bio": "甘え上手な底なし沼"
    },
    "槻本大河": {
        "image": "images/槻本.PNG",
        "bio": "出自を疎む経理兼オカン"
    },
    "相沢篠信": {
        "image": "images/相沢.PNG",
        "bio": "愛嬌たっぷりの利口な狂犬"
    },
    "祠堂恭耶": {
        "image": "images/祠堂.PNG",
        "bio": "気品と自信溢れる美術講師"
    },
    "神家": {
        "image": "images/神家.PNG",
        "bio": "記憶喪失のバレリーノ"
    }
}

# キャラ選択
selected_char = st.selectbox("私の推しキャラ紹介：", list(characters.keys()))
char_info = characters[selected_char]

# 画像が存在するかチェック（デバッグ用）
if not os.path.exists(char_info["image"]):
    st.error(f"画像ファイルが見つかりません: {char_info['image']}")
else:
    st.image(char_info["image"], width=300)

st.write(f"**{selected_char}の紹介：**")
st.write(char_info["bio"])

st.markdown("---")

# 診断パート
st.header("あなたが好きそうなキャラを診断してみよう")

q1 = st.radio("好きなタイプは？", ["かわいい", "おもしろい", "クール"])

if st.button("診断する"):
    if q1 == "かわいい":
        st.success("あなたにおすすめのキャラは相沢篠信、神家です！")
    elif q1 == "おもしろい":
        st.success("あなたにおすすめのキャラは須王芦佳、樋宮明星です！")
    else:
        st.success("あなたにおすすめのキャラは槻本大河、祠堂恭耶です！")


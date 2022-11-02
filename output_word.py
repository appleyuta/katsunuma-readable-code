import sys

import json

#辞書データの読み込み
with open('./word_data.json', "r", encoding="utf-8") as f:
    dic_data = json.load(f)


# ユーザ情報を取得
userdata = dic_data['userdata']

# 単語情報を取得
word_info = dic_data['word_info']

# ユーザ情報の表示
print(f"ユーザー名: {userdata['username']}")


#引数の数によって挙動を変更する
if len(sys.argv) == 2:
    #引数で指定されたidの単語を出力
    word_data = word_info[int(sys.argv[1])]
    print(f"{word_data['id']}: {word_data['word']} {word_data['kana']}")

else:
    #辞書データに登録されているidと単語をすべて出力
    for word_data in word_info:
        print(f"{word_data['id']}: {word_data['word']} {word_data['kana']}")

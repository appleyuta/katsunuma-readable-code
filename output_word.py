import sys

import json

#辞書データの読み込み
with open('./word_data.json') as f:
    dic_data = json.load(f)

#引数の数によって挙動を変更する
if len(sys.argv) == 2:
    #引数で指定されたidの単語を出力
    word_data = dic_data[int(sys.argv[1])]
    print(str(word_data["id"])+": " + word_data["word"])

else:
    #辞書データに登録されているidと単語をすべて出力
    for word_data in dic_data:
        print(str(word_data["id"])+": " + word_data["word"])
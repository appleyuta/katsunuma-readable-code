使用言語：python

実行方法：
　（前提）pythonが実行可能な環境
　output_word.pyをpythonに読み込ませて実行する

　例) python3 output_word.py

引数：
　実行時に引数が与えられたか否かで挙動を変更する
　引数としてid情報が付与された場合は、そのidで指定された単語を出力
　引数が指定されたなかった場合は、すべての単語を出力する
　
　例) python3 output_word.py 1

辞書データファイル:
  ファイル名は"word_data.json"とする
  ファイル形式はjsonであり、キーをつけて情報を管理する
  ・  id...単語id
  ・word...単語
  ・kana...ふりがな

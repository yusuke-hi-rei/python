#------- 正規表現 --------#
import re

data = """
太郎 taro@yamada.com
花子 hanako@flower.jp
一郎 ichiro@baseball.com
幸戸 sachi@happy.org
"""
# r : Do not escape escape characters.
relist = re.findall(r"(.*?)([a-zA-Z]+@[a-zA-Z.]+)", data)

print(relist)

#------- 文字列置換 --------#

relist = re.sub(
    r'([a-zA-Z0-9.-_]+)@([a-zA-Z0-9.]+)(com|jp|org)',
    r'(***@\2jp)',
    data)

print(relist)


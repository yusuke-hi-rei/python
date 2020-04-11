import requests
import re

#------- request testing ------------
res = requests.get("http://httpbin.org/get")
print(res.text)

#------- request param testing ------------

params={"id":123, "name":"taro", "pass":"hoge"}
res = requests.get("http://httpbin.org/get", params)
print(res.text)

data = res.json()
args = data["args"]
for item in args:
    print(item + "=" + args[item])

#------- request post testing ------------

params={"id":123, "name":"taro", "pass":"hoge"}
res = requests.post("http://httpbin.org/post", params)
print(res.text)

data = res.json()
args = data["form"]
for item in args:
    print(item + "=*=" + args[item])

#------- request re testing ------------

params={"id":123, "name":"taro", "pass":"hoge"}
res = requests.get("http://httpbin.org", params)
#print(res.text)

data = re.findall(r'<a href="(.*?)".*?>(.*?)</a>', res.text)
for item in data:
    print(item)#[0])

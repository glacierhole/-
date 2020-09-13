import urllib.request
import re
import random
import time

uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
    ]
def UA():
    opener=urllib.request.build_opener()
    thisua=random.choice(uapools)
    ua=("User-Agent",thisua)
    opener.addheaders=[ua]
    urllib.request.install_opener(opener)
    print("当前使用UA："+str(thisua))
for i in range(0,35):
    UA()
    thisurl="https://www.qiushibaike.com/text/page/"+str(i+1)+ "/"
    data=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
    pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
    rst=re.compile(pat,re.S).findall(data)
    for j in range(0,len(rst)):
        print(rst[j])
        print("——————")
    

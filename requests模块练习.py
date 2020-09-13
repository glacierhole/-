import requests
import re

hd={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",}
px={"http":"http://47.96.106.177:8080"}

rst=requests.get("https://www.aliwx.com.cn/",headers=hd)
title=re.compile("<title>(.*?)</title>",re.S).findall(rst.text)

pr={"wd":"阿里文学",}
rst2=requests.get("http://www.baidu.com/s",params=pr)


postdata={"username":"饭面面",
     "password":"2000313rxr",
     }
rst3=requests.post("http://www.fast8.com/phome/index.php",data=postdata)



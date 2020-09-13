import urllib.request
import re
cid="6689895369036463828"
for i in range(0,10):
    print("第"+str(i+1)+"页评论数据")
    url="https://video.coral.qq.com/varticle/5572751505/comment/v2?callback=_varticle5572751505commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(cid)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132"
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat1='"content":"(.*?)"'
    comment=re.compile(pat1,re.S).findall(data)
    for item in comment:
        print(str(item))
        print("_______________________________________________")
    pat2='"last":"(.*?)"'
    cid=re.compile(pat2,re.S).findall(data)[0]



# -*- coding:utf-8 -*-
from  urllib.request import urlopen
import re
buff = urlopen('https://coding.imooc.com/').read().decode("utf-8")
lists = re.findall(r'//img.mukewang.com/.+\.jpg',buff)
i = 0
for list in lists:
    with open('D:\\IMOOC\\'+str(i)+'.jpg','wb') as file:
        req = urlopen('http:'+list)
        buf = req.read()
        file.write(buf)
        print('NO '+str(i)+' picture download successfully')
        i += 1
        
        
        
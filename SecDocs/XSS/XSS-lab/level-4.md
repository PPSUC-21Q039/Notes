# 知识点：
< >的删除
```php
$str2=str_replace(">","",$str);
$str3=str_replace("<","",$str2);
```
靠事件执行的标签绕过
# 思路：
"前有空格，不然无法执行<br />"onfocus=javascript:alert(1) "<br />![image.png](./images/20231017_2355267555.png)

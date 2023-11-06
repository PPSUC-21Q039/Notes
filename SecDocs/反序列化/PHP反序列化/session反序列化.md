# 文章
[带你走进PHP session反序列化漏洞 - 先知社区](https://xz.aliyun.com/t/6640)<br />[原理+实践掌握(PHP反序列化和Session反序列化) - 先知社区](https://xz.aliyun.com/t/7366)<br />[PHP :: Doc Bug #71101 :: serialize_handler must not be switched for existing sessions](https://bugs.php.net/bug.php?id=71101#:~:text=Session%20module%20can%20not%20predict%20that%20somebody%20in,try%20to%20load%20session%20data%20with%20wrong%20handler.)<br />[php序列化 - l3m0n - 博客园](https://www.cnblogs.com/iamstudy/articles/php_serialize_problem.html#2-php_session%E5%BA%8F%E5%88%97%E5%8C%96%E5%8F%8A%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E9%97%AE%E9%A2%98)
# 其他
Linux上，常见的php-session存放位置有：
:::tips
/var/lib/php5/sess_PHPSESSID <br />/var/lib/php7/sess_PHPSESSID <br />/var/lib/php/sess_PHPSESSID <br />/tmp/sess_PHPSESSID <br />/tmp/sessions/sess_PHPSESSED
:::
### 设置php session 处理器的方法
#### ini_set()
[PHP: ini_set - Manual](https://www.php.net/manual/zh/function.ini-set.php)<br />这是最为常见的方法，但第二个参数不支持数组，如果是传递数组的话需要用`session_start()`
```php
ini_set('serialize_handler', 'php_serialize');
```
#### session_start()
[PHP: session_start - Manual](https://www.php.net/manual/zh/function.session-start.php)<br />PHP 7 中 `session_start ()` 函数可以接收一个数组作为参数，可以覆盖 php.ini 中 session 的配置项。此数组中的键无需包含 session. 前缀。
```php
session_start(Array('serialize_handler' => 'php_serialize'))
```

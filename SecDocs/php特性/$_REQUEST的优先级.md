# 文章
[What is the $_REQUEST precedence?](https://stackoverflow.com/questions/43157933/what-is-the-request-precedence)
# 原理
`$_REQUEST`会接受`$_GET`, `$_POST`, `$_COOKIE`。<br />并且设置的顺序是由`php.ini`中的`variables_order`或`request_order`进行控制。<br />一般默认值为
```php
variables_order = "GPC"
```
即，先设置`$_GET`，再设置`$_POST`，再设置`$_COOKIE`<br />优先级则为`CPG`<br />例如，当`$_GET`和`$_POST`都传递了`flag`参数，则`flag`的参数值为`$_POST`中的值<br />可以以此绕过一些过滤

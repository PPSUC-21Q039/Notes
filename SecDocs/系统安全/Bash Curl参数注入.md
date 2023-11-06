## 文章

[bash curl参数注入题目](F:\LocalCTF\bash curl参数注入题目.pdf)

[bashinj writeup](F:\LocalCTF\bashinj writeup.pdf)

## 恶意服务器脚本

**恶意代理服务器**

```bash
import mitmproxy.http
from mitmproxy import ctx
from mitmproxy.http import HTTPFlow, Response


data = br'''
evil contents
'''


class Hook:
    def request(self, flow: HTTPFlow):
        flow.response = Response.make(200, data, {'Content-Type':'text/plain'})
        ctx.log.info("Process a request %r" % flow.request.url)


addons = [
    Hook()
]
```

启动

```bash
mitmdump -s test.py --set block_global=false -p 7777
```

**恶意DNS服务器**

```bash
import dns.message
import dns.query
from dnslib import DNSRecord
from dnslib.server import DNSServer, DNSHandler, BaseResolver

class MyDNSResolver(BaseResolver):
    def resolve(self, request, handler):
        # 解析请求的域名
        qname = request.q.qname
        # 创建一个 DNSRecord 对象
        reply = DNSRecord()
        # 设置响应的查询问题部分
        reply.add_question(qname, qtype=request.q.qtype)
        # 添加响应的回答部分
        reply.add_answer(*self.get_dns_answer(qname))
        # 将响应发送回客户端
        handler.send_reply(reply)

    def get_dns_answer(self, qname):
        # 在这里实现您的自定义逻辑，根据查询的域名返回相应的回答
        # 这里只是一个示例，始终返回一个 A 记录回答
        answer = ('httpbin.org', 'A', '172.20.240.1', 60)
        return answer

if __name__ == '__main__':
    resolver = MyDNSResolver()
    server = DNSServer(resolver, port=53, address='0.0.0.0')
    server.start()
```


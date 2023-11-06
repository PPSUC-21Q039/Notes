大多数 POST 请求使用由 HTML 表单生成的默认内容类型，例如 application/x-www-form-urlencoded。一些网站希望接收这种格式的请求，但会容忍其他内容类型，包括 XML<br />例如，如果一个正常的请求包含以下内容：
```xml
POST /action HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 7

foo=bar
```
然后您可能可以提交以下请求，结果相同：
```xml
POST /action HTTP/1.0
Content-Type: text/xml
Content-Length: 52

<?xml version="1.0" encoding="UTF-8"?><foo>bar</foo>
```
如果应用程序容忍消息正文中包含 XML 的请求，并将正文内容解析为 XML，那么您只需将请求重新格式化为使用 XML 格式，就可以到达隐藏的 XXE 攻击面。

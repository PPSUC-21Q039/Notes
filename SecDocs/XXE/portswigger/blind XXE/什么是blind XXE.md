当应用程序容易受到 XXE 注入但未在其响应中返回任何已定义外部实体的值时，就会出现盲 XXE 漏洞。这意味着无法直接检索服务器端文件，因此盲目 XXE 通常比常规 XXE 漏洞更难利用。<br />有两种广泛的方法可以发现和利用盲目的 XXE 漏洞：

- 您可以触发带外网络交互，有时会在交互数据中泄露敏感数据。
- 您可以通过错误消息包含敏感数据的方式触发 XML 解析错误。

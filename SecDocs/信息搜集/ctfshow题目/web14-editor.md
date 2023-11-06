# 知识点
有时候源码里面就能不经意间泄露重要(editor)的信息,默认配置害死人<br />0day:某编辑器最新版默认配置下，如果目录不存在，则会遍历服务器根目录
# 思路
访问editor<br />![image.png](./images/20231017_2356125915.png)<br />发现上传文件可以查看文件空间<br />![image.png](./images/20231017_2356136652.png)<br />从var/www/html/nothinghere/fl000g.txt 找到flag<br />![image.png](./images/20231017_2356144227.png)<br />浏览器访问地址获得flag<br />![image.png](./images/20231017_2356159205.png)

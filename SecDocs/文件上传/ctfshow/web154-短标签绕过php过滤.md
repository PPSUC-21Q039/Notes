# 知识点
### php短标签
# 思路
文件内容中php没过滤，通过短标签绕过<br />向文件中写入配置文件，开启短标签<br />![image.png](./images/20231018_0000022837.png)<br />传入1.txt被主文件包含<br />![image.png](./images/20231018_0000038425.png)<br />进行rce![image.png](./images/20231018_0000044887.png)

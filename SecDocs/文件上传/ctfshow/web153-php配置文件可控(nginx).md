# 知识点
### .user.ini / .htaccess
[https://www.php.net/manual/en/configuration.file.per-user.php](https://www.php.net/manual/en/configuration.file.per-user.php)
### php.ini相关的选项
[https://www.php.net/manual/en/ini.list.php](https://www.php.net/manual/en/ini.list.php)<br />[auto_append_file](https://www.php.net/manual/en/ini.core.php#ini.auto-append-file) 将指定文件包含在文件尾<br />[auto_prepend_file](https://www.php.net/manual/en/ini.core.php#ini.auto-prepend-file) 将指定文件包含在文件头

# 思路
### 方法一
写入配置文件<br />![image.png](./images/20231017_2359553304.png)<br />抓包上传配置文件<br />![image.png](./images/20231017_2359562587.png)<br />上传木马文件<br />![image.png](./images/20231017_2359579661.png)<br />访问/upload时，1.txt会包含在index.php的文件尾被解析，就可以进行命令执行了<br />![image.png](./images/20231017_2359586412.png)
### 方法二 通过控制配置文件 包含log日志
我们还可以通过配置文件包含log日志<br />![image.png](./images/20231018_0000001120.png)<br />进行rce<br />![image.png](./images/20231018_0000019985.png)

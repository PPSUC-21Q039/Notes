binlog 二进制日志文件
### 查询日志文件是否开启
```java
show global variables like 'log_bin%';
show global variables like 'log%';
```
![image.png](./images/20231018_0005067454.png)
### 查询当前数据库日志
```java
show binary logs;
show master logs;
```
### 查询数据苦当前状态
```java
status
```
![image.png](./images/20231018_0005078703.png)
### 解析日志文件
```java
mysqlbinlog.exe [日志文件]
```
![image.png](./images/20231018_0005081181.png)

除了flag外，还有一份密码表

![image-20231011084032399](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011084032399.png)

有可能是172.22.2.16的mssql密码


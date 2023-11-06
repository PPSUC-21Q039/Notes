# Windows 常用命令与信息搜集

## Windows 常用命令

```
$ query user               # 查看用户登陆情况
$ whoami                   # 当前用户权限
$ set                      # 环境变量
$ hostname                 # 主机名
$ systeminfo               # 查看当前系统版本与补丁信息
$ ver                      # 查看当前服务器操作系统版本
$ net user                 # 查看用户信息
$ net start                # 查看当前计算机开启服务名称
$ netstat -ano             # 查看端口情况
$ netstat -ano|find "3389" # 查看指定端口
$ tasklist                 # 查看所有进程占用的端口
$ taskkil /im xxx.exe /f   # 强制结束指定进程
$ taskkil -PID pid号       # 结束某个pid号的进程
$ tasklist /svc|find "TermService" # 查看服务pid号
$ wmic os get caption              # 查看系统名
$ wmic product get name,version    # 查看当前安装程序
$ wmic qfe get Description,HotFixID,InstalledOn # 查看补丁信息
$ wmic qfe get Description,HotFixID,InstalledOn | findstr /C:"KB4346084" /C:"KB4509094" # 定位特定补丁
```
```
# 添加管理员用户
$ net user username(用户名) password(密码) /add  # 添加普通用户
$ net localgroup adminstrators username /add   # 把普通用户添加到管理员用户组
# 如果远程桌面连接不上可以添加远程桌面组
$ net localgroup "Remote Desktop Users" username /add
```

开启3389端口：

```
REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 00000000 /f
```

## 当前主机信息搜集

### 常用信息搜集

- whoami # 查看当前用户
- net user # 查看所有用户
- query user # 查看当前在线用户
- ipconfig /all # 查看当前主机的主机名/IP/DNS等信息
- route print # 查看路由表信息
- netstat -ano # 查看端口开放情况
- arp -a # 查看arp解析情况
- tasklist /svc # 查看进程及对应服务名
- net localgroup administrators # 查看管理员组成员
- systeminfo # 查看系统信息含补丁信息
- net use # 查看ipc连接情况
- net view # 查看匿名共享情况
- netsh firewall show state # 查看防火墙状态
- cmdkey /l # 查看当前保存的登陆凭证

### 密码搜集

- netsh wlan show profiles # 查看连接过的wifi名称
- netsh wlan show profile name="wifi名称" key=clear # 查看wifi的密码
- dir /a %userprofile%\AppData\Local\Microsoft\Credentials* # 查看RDP连接凭证
- dir /a /s /b "网站目录\*config*" > 1.txt # 数据库配置文件
- laZagne.exe all -oN # 本地wifi/浏览器等密码
- dir %APPDATA%\Microsoft\Windows\Recent # 查看最近打开的文档

### 连通性

- ping www.baidu.com # ICMP连通性
- nslookup www.baidu.com # DNS连通性
- curl [https://www.baidu.com](https://www.baidu.com/) # http连通性
- nc ip port # TCP连通性

## 域信息搜集

### 常用信息搜集

- net config workstation #查看当前登录域
- net user /domain # 获得所有域用户列表
- net view /domain # 查看所有的域
- net view /domain:XXX # 查看该域内所有主机
- net group /domain # 查看所有域用户组列表
- net group "domain computers" /domain # 查看域内所有的主机名
- net group "domain admins" /domain # 查看所有域管理员
- net group "domain controllers" /domain # 查看所有域控制器
- net group "enterprise admins" /domain # 查看所有企业管理员
- nltest /domain_trusts # 获取域信任信息
- net time /domain # 查看当前登录域
- net accounts /domain # 查看域密码策略
- dsquery server # 寻找目录中的域控制器
- netdom query pdc # 查看域控制器主机名
- wmic useraccount get /all #获取域内用户的详细信息

### 环境信息搜集

- nbtscan.exe xx.xx.xx.xx/24 # 查看c段机器
- csvde.exe -f 1.csv -k # 批量导入/导出AD用户
- setspn.exe -T xx.xx.xx.xx -Q */* # 查看当前域内所有spn

### 密码搜集

- dir /s /a \域控IP\SYSVOL*.xml # 获取域里面所有机子的本地管理员账号密码
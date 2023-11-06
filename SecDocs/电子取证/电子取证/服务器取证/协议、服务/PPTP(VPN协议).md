### 参考资料
[[MS-PTPT]: Point-to-Point Tunneling Protocol (PPTP) Profile](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ptpt/32e8cf6d-2e0d-4843-8dc0-a4934e16e1f5)<br />[RFC 2637: Point-to-Point Tunneling Protocol (PPTP)](https://www.rfc-editor.org/rfc/rfc2637)
### PPTP协议流程分析
[PPTP协议握手流程分析 - Gordon0918 - 博客园](https://www.cnblogs.com/gordon0918/p/5280587.html)<br />PPTP默认端口 1723
### Linux PPTPD的配置
[PPTPD 服务搭建 - Khazix - 博客园](https://www.cnblogs.com/demonxian3/p/10606220.html)
#### /etc/pptpd.conf
```powershell
/etc/pptpd.conf 是 PPTP VPN 服务器的配置文件，它包含了 PPTP 服务的全局配置信息。以下是该配置文件的详解：

listen：指定 PPTP 服务监听的 IP 地址，默认为本机的所有 IP 地址。

localip：指定 PPTP 服务器分配给客户端的 IP 地址的起始值和结束值，通常设置为一个网段中未被使用的 IP 地址范围。例如：localip 192.168.0.100-200

remoteip：指定 PPTP 服务器分配给远程用户使用的 IP 地址，也可以设置为一个 IP 地址范围。例如：remoteip 192.168.0.201-250

refuse-pap：禁用 PAP 认证方式。

refuse-chap：禁用 CHAP 认证方式。

refuse-mschap：禁用 MSCHAP 认证方式。

require-mschap-v2：要求使用 MSCHAPv2 认证方式。

require-mppe：要求使用 MPPE 加密方式。

nologin：禁止使用 /etc/passwd 文件进行认证，只允许使用 PPTP 用户数据库进行认证。

name：指定 PPTP 服务的名称，可选。

debug：开启调试模式，输出更多的日志信息。
```
**具体例子**
```powershell
listen 10.0.0.1
localip 10.0.0.2-50
remoteip 10.0.0.51-100
require-mschap-v2
require-mppe
```

#### /etc/ppp/pptpd-options
```powershell
/etc/ppp/pptpd-options 是 PPTP VPN 服务器的 PPP 配置文件，用于指定 PPTP 客户端和服务器之间的连接选项。以下是该配置文件的详解：

name：指定 PPTP 连接的名称，可选。

refuse-pap：禁用 PAP 认证方式。

refuse-chap：禁用 CHAP 认证方式。

refuse-mschap：禁用 MSCHAP 认证方式。

require-mschap-v2：要求使用 MSCHAPv2 认证方式。

require-mppe：要求使用 MPPE 加密方式。

nobsdcomp：禁用 BSD 原始压缩协议。

nodeflate：禁用 Deflate 压缩协议。

noipx：禁用 IPX 协议。

novj：禁用 Van Jacobson TCP/IP 头压缩算法。

novjccomp：禁用 VJ TCP/IP 数据压缩算法。

nologfd：不将日志输出到标准错误流中。

ms-dns：指定 DNS 服务器的 IP 地址。

mtu：指定最大传输单元的大小，通常为 1400 或 1450。

mru：指定最大重组单元的大小，通常与 MTU 相同。
```
**具体例子**
```powershell
require-mschap-v2
require-mppe
ms-dns 8.8.8.8
mtu 1400
mru 1400
```

#### /etc/ppp/chap-secrets
```powershell
/etc/ppp/chap-secrets 是 PPTP VPN 服务器的 PPP 用户数据库文件，用于保存可以通过 PPTP 认证的用户列表。它的每一行都包含四个字段，分别是“用户名”、“PPP 服务名称”、“密码”和“允许访问的 IP 地址”。以下是该文件的详细说明：

用户名：指定需要认证的用户名。

PPP 服务名称：指定使用哪个 PPP 服务进行认证，通常为 “pptpd”。

密码：指定用户的密码，必须使用单引号或双引号括起来。

允许访问的 IP 地址：指定用户被允许连接时所分配的 IP 地址，也可以使用星号 “*”，表示任意 IP 地址。
```
**具体例子**
```powershell
# Secrets for authentication using CHAP
# client    server      secret              IP addresses
alice       pptpd       alicepassword       *
bob         pptpd       bobpassword         192.168.0.2
charlie     pptpd       charliepassword     10.0.0.2-10.0.0.5
```

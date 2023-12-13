# Linux 取证的五个主要领域

[网络安全与取证研究](javascript:void(0);) *2023-11-21 08:00* *Posted on 北京*

https://mp.weixin.qq.com/s/c7YiymK0ow02QwCYI8wGVg

---

**MicroPest**.个人开发的小工具](https://mp.weixin.qq.com/s/c7YiymK0ow02QwCYI8wGVg#)

关于Linux的安全检测，我以前的文章介绍了好几篇，有《[工具：Linux Malware Detect](http://mp.weixin.qq.com/s?__biz=MjM5NDcxMDQzNA==&mid=2247484771&idx=1&sn=03b8f838b7262a13bab9e6e0712f2fbb&chksm=a682d3ae91f55ab88b9d40067762082df48972a57098bd5f9f6ecc1231deb0982a2d7eb54bf2&scene=21#wechat_redirect)》《[工具：Linux安全检查GScan](http://mp.weixin.qq.com/s?__biz=MjM5NDcxMDQzNA==&mid=2247485175&idx=1&sn=e3137eaebfece590014a797ccedb5af8&chksm=a682d03a91f5592c8113ec76611331f03463c304e11927ceeec9a852fbc1ab728f5b1ea3264c&scene=21#wechat_redirect)》《[工具：Linux 应急检测脚本](http://mp.weixin.qq.com/s?__biz=MjM5NDcxMDQzNA==&mid=2247485246&idx=1&sn=9e3a6c0b3fa05c17c2bf09000a380293&chksm=a682d1f391f558e5e9ab0ffb5b49296439fcaaeeb9246e849de15cf474f1f051b42b3f68764c&scene=21#wechat_redirect)》《[Windows/Linux入侵手工排查](http://mp.weixin.qq.com/s?__biz=MjM5NDcxMDQzNA==&mid=2247485925&idx=1&sn=1c63cdd13c98610ec216832e06d5637c&chksm=a682df2891f5563ed4cc0a5c3a9a9a906ca057c3449cffedd521bcc99b38dd533a886932fa4e&scene=21#wechat_redirect)》《[记录任何 Linux 进程访问了哪些文件](http://mp.weixin.qq.com/s?__biz=MjM5NDcxMDQzNA==&mid=2247486897&idx=1&sn=c7cc4ddced65b7d23b65629a1349896d&chksm=a682db7c91f5526ab204057ba52a03ce4916cf5daca46b074dcba5ecfe6e093c7d5ce8b8d9fa&scene=21#wechat_redirect)》。

攻防*1000:1规则*：

防御者需要知道成千上万种入侵系统的方法。攻击者只需正确一次。

攻击者需要知道成千上万种掩盖踪迹的方法掩盖行踪。防御者需要发现错一次。

掌握下面的关注点，我们对入侵的检测就能做到游刃有余了；非常不错的Linux取证五个知识领域。



## 一、重点关注所说的 Linux 取证的五个主要领域：

**进程**– 可疑进程和网络活动。

**目录**– 包含恶意负载、数据或工具的可疑目录，允许横向移动到网络中。

**文件**– 恶意的、可能被篡改的或在 Linux 主机上不合适的文件。

**用户**– 检查可疑用户活动的区域。

**日志**– 日志文件篡改检测和公共区域，用于检查有人掩盖踪迹的迹象。



![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzSEiaVTyAHDfLs4ZQOZ4JYPINbJoUYdwDGQUkhfdRD2IKiaRRk3Z1JTKQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

## Processes

Large amounts of RAM:

```
top
```

Process tree:

```
ps -auxwf
```

Open network ports or raw sockets:

```
netstat -nalpn
etstat -plant
ss -a -e -i
lsof [many options]
```

Deleted binaries still running:

```
ls -alR /proc/*/exe 2> /dev/null |  grep deleted
```

Process command name/cmdline:

```
strings /proc/<PID>/comm
strings /proc/<PID>/cmdline
```

Real process path:

```
ls -al /proc/<PID>/exe
```

Process environment:

```
strings /proc/<PID>/environ
```

Process working directory:

```
ls -alR /proc/*/cwd
```

Process running from tmp, dev dirs:

```
ls -alR /proc/*/cwd 2> /dev/null | grep tmp
ls -alR /proc/*/cwd 2> /dev/null | grep dev
```

## Directories

Commonly targeted directories:

```
/tmp, /var/tmp, /dev/shm, /var/run,/var/spool, user home directories
```

List and delimit spaces, etc. in names:

```
ls -lap
```

List all hidden directories:

```
find / -type d -name ".*"
```

## Files

Immutable files and directories:

```
lsattr / -R 2> /dev/null | grep "\----i"
```

Find SUID/SGID files:

```
find / -type f \( -perm -04000 -o -perm -02000 \) -exec ls -lg {} \;
```

Files/dirs with no user/group name:

```
find / \( -nouser -o -nogroup \) -exec ls -lg  {} \;
```

List all file types in current dir:

```
file * -p
```

Find executables anywhere, /tmp, etc.:

```
find / -type f -exec file -p '{}' \; |  grep ELF
find /tmp -type f -exec file -p '{}' \; |  grep ELF
```

Find files modified/created within last day:

```
find / -mtime -1
```

Persistence areas:

```
/etc/rc.local, /etc/initd, /etc/rc*.d, /etc/modules, /etc/cron*, /var/spool/cron/*
```

Package commands to find changed files:

```
rpm -Va | grep ^..5.
debsums -c
```

## Users

Find all ssh authorized_keys files:

```
find / -name authorized_keys
```

History files for users:

```
find / -name .*history
```

History files linked to /dev/null:

```
ls -alR / 2> /dev/null | grep .*history |  grep null
```

Look for UID 0/GID 0:

```
grep ":0:" /etc/passwd
```

Check sudoers file:

```
cat /etc/sudoers and /etc/group
```

Check scheduled tasks:

```
crontab -l
atq
systemctl list-timers  --all
```

## Logs

Check for zero size logs:

```
ls -al /var/log/*
```

Dump audit logs:

```
utmpdump /var/log/wtmp
utmpdump /var/run/utmp
utmpdump /var/log/btmp
last
lastb
```

Find logs with binary in them:

```
grep [[:cntrl:]] /var/log/*.log
```

## 二、具体例子：

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzcgjjVoG2SrnZx2ZHJhxgQksueiaKwf18AxxUDAZ0LySAKiaXqRGzY9qQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzsCvEb8JCdL9phrcJwiafAA7icsBkYZuibxiaco0QZzJMQgkiat2l1xY78Vg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzFfcpCFue38SHiaCEC7Klf6Ex9AJtsq8y59VO4QLpBsMn8G5Ebe12dCw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDz234AMCULMjyWvTKSkPhXkUsc8XHzAapkibOhyfzCuOJTdAu6kzMPSDQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzF3lfVLRPyvPkicktvNDcJe6bKrqHAp6K7cenWIwYa9NuYm9sK56yZmQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzXUoHcnzPUXczC82QbwlW037Kgr3a4AD6AMa7ypiaDNicib8IYS5RTu2Hg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzB8mRJUstAeUw2iaxiau9Yhq8bCYuA1vibgibdUxsSo5VUFNocMbaxkekyA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDz7djVuNdpg89m6yFJUZVEGyvAzU3SagQZEN2bG4pGVem4j6hd55ztyg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzaXUkVLOTqBovVZVZD2DQr5NIWqrf6sbGINtYJSaMM5FnNclJ3H8kPw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDz1Xjl1j9QSTrvxmjYsIss32XdoLJEEo3P0OF1sjlofOhamxsQwIlDCA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzM7OkiavP2xfoDbLv9niau8aYpfQibBLg4ic4vtAETia7copwJXmgdABuFicg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzQ40tsicTpq4tWsVWkFLldoJ39ym3TKgOqSNO4b8Bd4Bra0fkc3c3dMw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzXTvL1NKib0PiaciaicQvnLIKqhsCzj1N7YemYGYSwC0sj9rUIIa7y14B1w/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzXQn5CHjk6MSBCdGFeh89PibhE6CIn6TuNlQs9bRRibicRibTkcB4Z3ZmjQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzddg8z09UFF25JicOnb0FWGia2m1FZBcyLTC1wugYAZReFjLGPkneZm9Q/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDz1DiccvK1YbOfVNWQDCR0OkHvpdbztWJ3oLutxchFXpgsEq7hVpia5ciaw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDz7wdBv6LicK5YgL2zVVbHV7L9CWHCmnm1WOHqXrRVVWd0Wic96oma79gQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzyXdqa5HToNWTufsicBxr8Xictzcu5aEsBC1yAGjuict13bWhErnaVCTZw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzZTNUco5CcZbMBpD0ECfA3NxKvArtMmZa4LWJI52gV7OWKpULsBw2nA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDznBApiakId7IrSj5QdKbGVicgC1lRExkZuQhsxv66GHLrzmkiap52kickcg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzkhZJ7oFJfdoC2UvUxRzf1XHric9CdXZd4jjAvybbpxNB3z11YickALQg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzL00uZUQicHS6awfel53VF0D6yFFjibB7ujonwrSWsvSicLdvLR71FLTqQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzw7KK0GQA2fHTTiaP7aCMCXrcibibdo3XFBRqwxXdU2mDMvDTu8ZbSYh2g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzqdD9RYeQw2P8rm1NODUKgoTHfBBj2g8ibiadicfhajUHlicToAJIyRXAYA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpLnHEqB93m9J6ZwwRltxcDzwadTxic8yu5clzcm0oZeXZlE3BA4Ytyck3Zo750qz7noibKBTAK2gK4g/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)
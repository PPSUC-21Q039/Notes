## 安装宝塔

## 管理宝塔
宝塔工具箱(包含下列绝大部分功能 直接ssh中执行bt命令 仅限6.x以上版本面板)
```powershell
bt
```
停止
```powershell
/etc/init.d/bt stop
```
启动
```powershell
/etc/init.d/bt start
```
重启
```powershell
/etc/init.d/bt restart
```
卸载
```powershell
/etc/init.d/bt stop && chkconfig --del bt && rm -f /etc/init.d/bt && rm -rf /www/server/panel
```
查看当前面板端口
```powershell
cat /www/server/panel/data/port.pl
```
修改面板端口，如要改成8881（centos 6 系统）
```powershell
echo '8881' > /www/server/panel/data/port.pl && /etc/init.d/bt restart
```
修改面板端口，如要改成8881（centos 7 系统）
```powershell
echo '8881' > /www/server/panel/data/port.pl && /etc/init.d/bt restart
```
强制修改MySQL管理(root)密码，如要改成123456
```powershell
cd /www/server/panel && python tools.py root 123456
```
修改面板密码，如要改成123456
```powershell
cd /www/server/panel && python tools.py panel 123456
```
查看宝塔日志
```powershell
cat /tmp/panelBoot.pl
```
查看软件安装日志
```powershell
cat /tmp/panelExec.log
```
站点配置文件位置
```powershell
/www/server/panel/vhost
```
删除域名绑定面板
```powershell
rm -f /www/server/panel/data/domain.conf
```
清理登陆限制
```powershell
rm -f /www/server/panel/data/*.login
```
查看面板授权IP
```powershell
cat /www/server/panel/data/limitip.conf
```
关闭访问限制
```powershell
rm -f /www/server/panel/data/limitip.conf
```
查看许可域名
```powershell
cat /www/server/panel/data/domain.conf
```
关闭面板SSL
```powershell
rm -f /www/server/panel/data/ssl.pl && /etc/init.d/bt restart
```
查看面板错误日志
```powershell
cat /tmp/panelBoot
```
查看数据库错误日志
```powershell
cat /www/server/data/*.err
```
站点配置文件目录(nginx)
```powershell
/www/server/panel/vhost/nginx
```
站点配置文件目录(apache)
```powershell
/www/server/panel/vhost/apache
```
站点默认目录
```powershell
/www/wwwroot
```
数据库备份目录
```powershell
/www/backup/site
```
站点日志
```powershell
/www/wwwlogs
```
## Nginx服务管理
nginx安装目录
```powershell
/www/server/nginx
```
启动
```powershell
/etc/init.d/nginx start
```
停止
```powershell
/etc/init.d/nginx stop
```
重启
```powershell
/etc/init.d/nginx restart
```
启载
```powershell
/etc/init.d/nginx reload
```
nginx配置文件
```powershell
/www/server/nginx/conf/nginx.conf
```
## Apache服务管理
apache安装目录
```powershell
/www/server/httpd
```
启动
```powershell
/etc/init.d/httpd start
```
停止
```powershell
/etc/init.d/httpd stop
```
重启
```powershell
/etc/init.d/httpd restart
```
启载
```powershell
/etc/init.d/httpd reload
```
apache配置文件
```powershell
/www/server/apache/conf/httpd.conf
```
## MySQL服务管理
mysql安装目录
```powershell
/www/server/mysql
```
phpmyadmin安装目录
```powershell
/www/server/phpmyadmin
```
数据存储目录
```powershell
/www/server/data
```
启动
```powershell
/etc/init.d/mysqld start
```
停止
```powershell
/etc/init.d/mysqld stop
```
重启
```powershell
/etc/init.d/mysqld restart
```
启载
```powershell
/etc/init.d/mysqld reload
```
mysql配置文件
```powershell
/etc/my.cnf
```
## FTP服务管理
ftp安装目录
```powershell
/www/server/pure-ftpd
```
启动
```powershell
/etc/init.d/pure-ftpd start
```
停止
```powershell
/etc/init.d/pure-ftpd stop
```
重启
```powershell
/etc/init.d/pure-ftpd restart
```
ftp配置文件
```powershell
/www/server/pure-ftpd/etc/pure-ftpd.conf
```
## PHP服务管理
php安装目录
```powershell
/www/server/php
```
启动(请根据安装PHP版本号做更改，例如：/etc/init.d/php-fpm-54 start)
```powershell
/etc/init.d/php-fpm-{52|53|54|55|56|70|71|72|73|74} start
```
停止(请根据安装PHP版本号做更改，例如：/etc/init.d/php-fpm-54 stop)
```powershell
/etc/init.d/php-fpm-{52|53|54|55|56|70|71|72|73|74} stop
```
重启(请根据安装PHP版本号做更改，例如：/etc/init.d/php-fpm-54 restart)
```powershell
/etc/init.d/php-fpm-{52|53|54|55|56|70|71|72|73|74} restart
```
启载(请根据安装PHP版本号做更改，例如：/etc/init.d/php-fpm-54 reload)
```powershell
/etc/init.d/php-fpm-{52|53|54|55|56|70|71|72|73|74} reload
```
配置文件(请根据安装PHP版本号做更改，例如：/www/server/php/52/etc/php.ini)
```powershell
/www/server/php/{52|53|54|55|56|70|71|72|73|74}/etc/php.ini
```
## Redis服务管理
redis安装目录
```powershell
/www/server/redis
```
启动
```powershell
/etc/init.d/redis start
```
停止
```powershell
/etc/init.d/redis stop
```
redis配置文件
```powershell
/www/server/redis/redis.conf
```
## Memcached服务管理
memcached安装目录
```powershell
/usr/local/memcached
```
启动
```powershell
/etc/init.d/memcached start
```
停止
```powershell
/etc/init.d/memcached stop
```
重启
```powershell
/etc/init.d/memcached restart
```
启载
```powershell
/etc/init.d/memcached reload	
```

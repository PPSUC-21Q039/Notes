## 文章

[PhpMyAdmin漏洞利用汇总 - 只言 - 博客园](F:\LocalCTF\PhpMyAdmin漏洞利用汇总 - 只言 - 博客园.html)

[phpMyAdmin 渗透利用总结-腾讯云开发者社区-腾讯云](F:\LocalCTF\phpMyAdmin 渗透利用总结-腾讯云开发者社区-腾讯云.html)

[phpmyadmin getshell姿势 - 先知社区](F:\LocalCTF\phpmyadmin getshell姿势 - 先知社区.html)

## PHPStudy中的PHPmyadmin

PHPstudy的phpmyadmin的配置文件在 libraries/onfig.default.php

```
2、查找 $cfg['PmaAbsoluteUri']=''; // 修改为你将上传到空间的phpMyAdmin的网址 。如：$cfg['PmaAbsoluteUri'] =‘http: // 网站         域名/phpmyadmin/'; 


3、查找 $cfg['Servers'][$i]['host'] =‘localhost'; // 通常用默认，也有例外，可以不用修改 


4、查找 $cfg['Servers'][$i]['auth_type'] =‘config'; // 在自己的机子里调试用config；如果在网络上的空间用cookie.
      在此有四种模式可供选择：cookie，http，HTTP，config
      ① config 方式即输入phpMyAdmin 的访问网址即可直接进入，无需输入用户名和密码，是不安全的，不推荐使用。 
      ② 设置cookie，http，HTTP方式，登录 phpMyAdmin 需要数据用户名和密码进行验证。
      具体如下：PHP 安装模式为 Apache，可以使用 http 和 cookie；PHP 安装模式为 CGI，可以使用 cookie。

 
5、查找 $cfg['Servers'][$i]['user'] = ‘root'; // MySQL用户名 


6、查找 $cfg['Servers'][$i]['password'] =''; // MySQL 密码 (only needed 留空就可以了)


7、查找 $cfg['Servers'][$i]['only_db'] = ''; // 你只有一个数据就设置一下,设置为你的数据库名；如果你想架设服务器，那么建             议留空 


8、查找 $cfg['DefaultLang'] = ‘zh'; // 这里是选择语言，zh代表简体中文的意思

 
9、查找$cfg['blowfish_secret'] =''; // 如果认证方法设置为cookie，就需要设置短语密码，设置为什么密码，由您自己决定，这里        不能留空，否则会在登录 phpMyAdmin 时提示如下图所示的错误。

```


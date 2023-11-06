# 文章
[PHP 原生类的利用小结 - 先知社区](https://xz.aliyun.com/t/9293#toc-14)<br />[SUCTF WriteUP-安全客 - 安全资讯平台](https://www.anquanke.com/post/id/146419)
# 知识点
PHP原生类 `SimpleXMLElement`，主要是有地方会对该类进行构造时，才能实现XXE，进而实现SSRF。<br />二次注入 `sig`可控，存在二次注入，从而进行报错注入。又因为过滤了`(`，所以可以将sql语句进行16进制编码后传入，从而绕过过滤。

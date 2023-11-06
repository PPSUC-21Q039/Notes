# 文章
[php 操作系统之间的一些黑魔法(绕过文件上传a.php/.) - 灰信网（软件开发博客聚合）](https://www.freesion.com/article/7470682764/)<br />[pathinfo两三事-安全客 - 安全资讯平台](https://www.anquanke.com/post/id/253383)
```java
if(!in_array(pathinfo($log_name, PATHINFO_EXTENSION), ['php', 'php3', 'php4', 'php5', 'phtml', 'pht'], true)) {
    file_put_contents($log_name, $output);
}
```
当我们给$log_name=1.php/.时，pathinfo会把1.php解析为目录，造成后缀解析为空从而绕过

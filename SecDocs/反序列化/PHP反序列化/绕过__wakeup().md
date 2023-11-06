# 文章
[PHP反序列化中wakeup()绕过总结 – fushulingのblog](https://fushuling.com/index.php/2023/03/11/php%e5%8f%8d%e5%ba%8f%e5%88%97%e5%8c%96%e4%b8%adwakeup%e7%bb%95%e8%bf%87%e6%80%bb%e7%bb%93/)
## 改属性个数
:::info
适用范围：<br />PHP5<5.6.25<br />PHP7<7.0.10
:::
当反序列化字符串中，表示属性个数的值大于真实属性个数时，会绕过 `__wakeup` 函数的执行
### 实例
[CTF日记之 “百度杯”CTF比赛 十月场 Hash_ctf hash题_二哈它爸的博客-CSDN博客](https://blog.csdn.net/sunleibaba/article/details/113501568)
## Fast Destruct
[PHP反序列化小技巧之Fast Destruct](https://hackerqwq.github.io/2021/08/29/PHP%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%B0%8F%E6%8A%80%E5%B7%A7%E4%B9%8BFast-Destruct/)
### 例题
[[ctfshow]红包挑战9](https://ctf-show.feishu.cn/docx/QdPBdLJDBoDxL7xBAtFcsksAnmg)   二血的思路最明确
## 另一种Bypass方法
[A new way to bypass __wakeup() and build POP chain - inHann的博客 | inHann’s Blog](https://inhann.top/2022/05/17/bypass_wakeup/)

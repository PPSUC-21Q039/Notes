# WP
[极客大挑战2020 官方Write-up](https://mp.weixin.qq.com/s?__biz=MzIzOTg0NjYzNg==&mid=2247485218&idx=1&sn=e910ddbd965ecb069b4da3d06443f337&chksm=e92292a1de551bb7c48bcca06053faed2a212642ee6a2f7767f671cc553f6a2d435f99fbfae6&mpshare=1&scene=23&srcid=1202ez9PcajE5NTRrZG6OF9G&sharer_sharetime=1606872114678&sharer_shareid=8752e0fdce9cf3d7a08d6c6826060293#rd)
# 知识点
PHP原生类绕过哈希比较
:::info
注意：

1. 第一点是像`Error`和`Exception`两个报错类，我们无法完全控制其`__toString()`方法，除了我们自定义的报错信息，还会带上你定义该类时的所在文件路径，以及定义的代码行等信息。所以，如果要使两个报错类打印出来的字符串完全相同，必须在同一行进行初始化。
2. 第二点是报错类除了能够传递自定义报错信息外，还可以设置一些其他的参数，通过这些参数可以使得定义的两个类在弱类型比较时不同，不然在弱类型比较时还是为相同。
:::

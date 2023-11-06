当做题没有思路时，并且明显感觉正则过滤意图明显，可用用`get_defined_functions()`去遍历看看有哪些可以使用的函数，从而获取思路
```powershell
<?php
$a = get_defined_functions();
foreach ($a["internal"] as $value){
    if (!preg_match('/[\x00- 0-9\'"`$&.,|[{_defgops\x7F]+/i', $value)) {
        echo $value."<br>";
    }
}
```
### 例题
[ctf-writeups/ISITDTU CTF 2019 Quals/web/easyphp.md at master · Samik081/ctf-writeups](https://github.com/Samik081/ctf-writeups/blob/master/ISITDTU%20CTF%202019%20Quals/web/easyphp.md)

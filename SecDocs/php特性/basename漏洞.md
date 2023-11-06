[https://bugs.php.net/bug.php?id=62119%E3%80%82](https://bugs.php.net/bug.php?id=62119%E3%80%82)
### basename()
返回路径中的文件名部分，会去掉文件名开头和结尾的非ASCII值。<br />var_dump(basename("\xffconfig.php")); => config.php<br />var_dump(basename("config.php\xff")); => config.php

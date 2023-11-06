# 知识点：
绕过htmlspecialchars()<br />通过事件触发标签来绕过 例如 onclick=javascript:alert()<br />onfocus

# 思路：
'onclick=javascript:alert("xss")>//&submit=搜索<br />![image.png](./images/20231017_2355259119.png)

# 知识点：
请求头Cookies xss注入
# 思路：
payload
```
Cookie: user="+type="text"+onclick="javascript:alert(1)"+"
```
与level-11类似<br />![image.png](./images/20231017_2355169277.png)

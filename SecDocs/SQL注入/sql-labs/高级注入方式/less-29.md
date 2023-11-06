# 知识点：
因为 return 表示了函数的结束运行，所以这个函数捕捉到 id 的时候就会返回 return $id_value，这样就导致了 用户加入构造两组 id 的话，那么后面的 id 就会绕过函数检测。<br />Apache PHP 会解析最后一个参数<br />Tomcat JSP 会解析第一个参数
# 思路：
index.php<br />![image.png](./images/20231017_2353587164.png)

login.php<br />![image.png](./images/20231017_2353594763.png)

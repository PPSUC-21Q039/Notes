## 知识点：
布尔型盲注, 报错注入

# 方法1: 布尔型注入

![image.png](./images/20231017_2352484120.png)![image.png](./images/20231017_2352491325.png)![image.png](./images/20231017_2352505419.png)![image.png](./images/20231017_2352515981.png)![image.png](./images/20231017_2352521228.png)<br />![image.png](./images/20231017_2352534595.png)

# 方法2：报错注入
(1). 通过floor报错<br />and (select 1 from (select count(*),concat((payload),floor (rand(0)*2))x from information_schema.tables group by x)a)<br />其中payload为你要插入的SQL语句<br />需要注意的是该语句将 输出字符长度限制为64个字符<br />(2). 通过updatexml报错<br />and updatexml(1,payload,1)<br />同样该语句对输出的字符长度也做了限制，其最长输出32位<br />并且该语句对payload的反悔类型也做了限制，只有在payload返回的不是xml格式才会生效<br />(3). 通过ExtractValue报错<br />and extractvalue(1, payload)<br />输出字符有长度限制，最长32位。<br />![image.png](./images/20231017_2352543991.png)<br />![image.png](./images/20231017_2352555080.png)<br />![image.png](./images/20231017_2352561966.png)

## floor报错

爆数据库<br />![image.png](./images/20231017_2352585357.png)		<br />爆数据库版本<br />![image.png](./images/20231017_2352595737.png)

爆用户名<br />![image.png](./images/20231017_2353016325.png)


爆表名<br />![image.png](./images/20231017_2353028047.png)


爆列名<br />![image.png](./images/20231017_2353048970.png)

爆值<br />![image.png](./images/20231017_2353057107.png)![image.png](./images/20231017_2353066014.png)

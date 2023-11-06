
## 知识点：
单引号sql注入 联合注入


## 思路：

先试试整型注入，发现没用<br />![image.png](./images/20231017_2352118890.png)		

向后面加入单引号，发现可以单引号注入<br />![image.png](./images/20231017_2352121411.png)	

		后面加上 --+ 将后面的limit注释掉<br />![image.png](./images/20231017_2352131562.png)	

使用order by 确定列的数量，发现为3	![image.png](./images/20231017_2352149117.png)		

使用联合注入，查看回显的列，发现为2，3列![image.png](./images/20231017_2352166023.png)	<br />之后先用database(),user()查看数据库名和用户名![image.png](./images/20231017_2352176616.png)	<br />再查看数据库中的表![image.png](./images/20231017_2352182207.png)	<br />再看看users表中列![image.png](./images/20231017_2352198164.png)	<br />查询users表中id，name，password的数据![image.png](./images/20231017_2352207840.png)

## 文章

http://www.nooemotion.com/2023/01/25/%E6%98%A5%E7%A7%8B%E4%BA%91%E5%A2%83-tsclient/

https://exp10it.cn/2023/07/%E6%98%A5%E7%A7%8B%E4%BA%91%E9%95%9C-tsclient-writeup

https://zysgmzb.club/index.php/archives/233

https://fushuling.com/index.php/2023/08/29/%E6%98%A5%E7%A7%8B%E4%BA%91%E5%A2%83%C2%B7tsclient/

## 打靶过程

用 fscan 扫 39.99.159.103， 扫到mssql弱密码

![image-20231010194036653](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010194036653.png)

用MDUT直接连接

SweetPotato提权，上线CS

![image-20231010195355311](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010195355311.png)

查看在线用户，存在John用户

![image-20231010195642318](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010195642318.png)

进程注入来获取John

![image-20231010195701835](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010195701835.png)

存在一个远程共享

![image-20231010195921804](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010195921804.png)

存在一个密码

![image-20231010200056341](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010200056341.png)

搭建代理

![image-20231010201854253](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010201854253.png)

![image-20231010201907376](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010201907376.png)

![image-20231010203328059](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010203328059.png)

改密码

![image-20231010204059228](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010204059228.png)

连接远程桌面

![image-20231010204401577](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010204401577.png)

镜像劫持提权

![image-20231010205508115](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010205508115.png)

WIN2016$是域管理员

![image-20231010205637748](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010205637748.png)

![image-20231010210834984](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010210834984.png)

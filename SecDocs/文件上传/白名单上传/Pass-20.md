# 知识点：


# 思路：
## 1.save_name 利用%00截断
![image.png](./images/20231018_0001065498.png)
## 2.利用move_uploaded_file()特性绕过
move_uploaded_file()有这么一个特性，会忽略掉文件末尾的 /.<br />![image.png](./images/20231018_0001074531.png)

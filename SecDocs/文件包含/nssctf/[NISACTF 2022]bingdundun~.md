# 知识点
文件包含<br />文件上传<br />phar协议
# 思路
提示可以上传压缩文件，所以我们可以尝试使用phar伪协议<br />将一句话木马压缩为zip文件<br />上传<br />![image.png](./images/20231018_0001384002.png)<br />很明显这里是一个文件包含点，并且会自动添加.php后缀<br />![image.png](./images/20231018_0001393539.png)
```php
?bingdundun=phar://a262e1025302cd5e46e2c2b288a80d37.zip/shell
```
直接getshell就可以

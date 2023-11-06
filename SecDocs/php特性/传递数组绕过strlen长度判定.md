```powershell
$a = $_POST[Ki1ro]
if strlen($a) < 2 {
	echo "success"
}
```
如果需要传递参数，但所需字符串比较长，但使用了strlen限制的长度，可以通过传递数组来绕过
```http
Ki1ro[] = 11111111111111111111111111111111111
```
能够成功通过

[https://t.zsxq.com/VRfqRFe](https://t.zsxq.com/VRfqRFe)<br />摘取出create_function的源代码（图1），可见用户输入的参数是function_args、function_code，他们被拼接成一个完整的PHP函数：

function __lambda_func ( function_args ) { function_code } \0

这个函数代码会先放在zend_eval_stringl里执行，可以理解为eval。执行成功后，再于函数列表中找到__lambda_func函数，将其重命名成lambda_%d，%d代表“这是本进程第几个匿名函数”。最后从函数列表里删除__lambda_func。

由于代码就是简单的拼接，所以我们可以闭合括号，执行任意代码。

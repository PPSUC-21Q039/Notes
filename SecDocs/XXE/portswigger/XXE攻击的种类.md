XXE 攻击有多种类型：
# 利用 XXE 检索文件
其中定义了包含文件内容的外部实体，并在应用程序的响应中返回。
# 利用 XXE 执行 SSRF 攻击
其中外部实体是基于后端系统的 URL 定义的。
# 利用盲目的 XXE 带外泄露数据
其中敏感数据从应用程序服务器传输到攻击者控制的系统。
# 利用盲XXE通过错误消息检索数据
攻击者可以触发包含敏感数据的解析错误消息。

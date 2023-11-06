## 文章

[内网渗透之内网代理 _ Dar1in9's Blog](F:\LocalCTF\内网渗透之内网代理 _ Dar1in9's Blog.html)

windows后台启动

用vb启动，以frpc为例

```bash
set ws=wscript.createobject("wscript.shell")
ws.run "cmd /c frpc -c C:\Windows\System32\frpc.ini",0
```

将上面的代码保存为vbs文件，双击运行即可，任务管理器就可以看到frpc进程了

如果要开机自动运行，就将vbs文件拷贝到 **C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp** windows启动目录存放即可
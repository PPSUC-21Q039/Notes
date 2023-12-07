# Android 取证 杂知识点

# 小米手机基本信息

## 设备标识/序列号

`data\com.miui.systemAdSolution\shared_prefs\mi_stat_pref.xml`

![image-20231203000257590](img/Android 取证.assets/image-20231203000257590.png)

## 小米应用商店数据库

应用的安装路径（包括md5）：`/data/com.xiaomi.market/databases/market_2.db` ，在X-Ways里面直接过滤就行

![img](img/Android 取证.assets/2817142-20230925202522608-2045166106.png)

![img](img/Android 取证.assets/2817142-20230925202523630-1194720093.png)

## WiFi 配置文件（原生应用）

`WifiConfigStore.xml`

![image-20231203163356963](img/Android 取证.assets/image-20231203163356963.png)

查看WiFi连接数：

![image-20231203163427188](img/Android 取证.assets/image-20231203163427188.png)

搜索一共有几个SSID即可。

## Android 手机短信记录（原生应用）

`mmssms.db`

![image-20231203174159529](img/Android 取证.assets/image-20231203174159529.png)

sms表中read字段值为0表示未读，type字段值为1表示接收的短信：

![img](img/Android 取证.assets/2817142-20230925202522627-1869491332.png)



# Android Whatsapp 应用取证（非原生，通用）

`\data\com.whatsapp\databases\msgstore.db`

<img src="img/Android 取证.assets/image-20231206013904904.png" alt="image-20231206013904904" style="zoom:50%;" />

数据在 `chat` 表里面：

![image-20231206013946385](img/Android 取证.assets/image-20231206013946385.png)

包括了 创建时间等，但是并没有找到WP里面的 `message_type`。

WP:

> ## 87.参考’潘志辉的手机镜像HUAWEIP30pro’,潘志辉手机华为P30Pro的WhatsApp的有多少个对话群组不包含对话讯息记录(系统自行发出的不作计算)?(2分)
>
> 先看一下有多少群组，根据chatid去看内容
>
> [![img](img/Android 取证.assets/2817142-20231123224903232-2048110326.png)](https://img2023.cnblogs.com/blog/2817142/202311/2817142-20231123224903232-2048110326.png)
>
> 通过分析，`message_type`的值为7表示系统消息，写个sql，剩下3个没有消息记录
>
> [![img](img/Android 取证.assets/2817142-20231123224903025-998128093.png)](https://img2023.cnblogs.com/blog/2817142/202311/2817142-20231123224903025-998128093.png)
>
> 结果为`3`

# 获取 APK

ADB 环境下：
1、连接手机
输入 adb 命令：`adb devices`

2、打开手机对应的软件

3、获取当前界面正在运行应用的包名：
输入 adb 命令：`adb shell dumpsys window | findstr  mCurrentFocus`

4、获取APK文件路径；注：package-name是上一步中获取的包名
输入 adb 命令：`adb shell pm path “package-name”`     

5、将 APK 导出到 PC 端进行保存
输入 adb 命令：`adb pull “手机APK文件路径” “PC文件夹路径”`
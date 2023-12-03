# Android 取证 杂知识点

# 小米手机基本信息

## 设备标识/序列号

`data\com.miui.systemAdSolution\shared_prefs\mi_stat_pref.xml`

![image-20231203000257590](img/Android 取证.assets/image-20231203000257590.png)

## 小米应用商店数据库

应用的安装路径（包括md5）：`/data/com.xiaomi.market/databases/market_2.db` ，在X-Ways里面直接过滤就行

![img](img/Android 取证.assets/2817142-20230925202522608-2045166106.png)

![img](img/Android 取证.assets/2817142-20230925202523630-1194720093.png)

## WiFi 配置文件

`WifiConfigStore.xml`

![image-20231203163356963](img/Android 取证.assets/image-20231203163356963.png)

查看WiFi连接数：

![image-20231203163427188](img/Android 取证.assets/image-20231203163427188.png)

搜索一共有几个SSID即可。

## Android手机短信记录

`mmssms.db`

![image-20231203174159529](img/Android 取证.assets/image-20231203174159529.png)

sms表中read字段值为0表示未读，type字段值为1表示接收的短信：

![img](img/Android 取证.assets/2817142-20230925202522627-1869491332.png)
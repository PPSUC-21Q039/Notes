# 配置动态IP（DHCP）上网

1.1 查看网卡列表

`ifconfig`

`ls /etc/sysconfig/network-scripts/`

一般默认第一个就是你电脑的网卡。

1.2 修改有线网卡信息

`vim /etc/sysconfig/network-scripts/ifcfg-ens160` 具体网卡可能有变

```
TYPE="Ethernet"
BOOTPROTO="dhcp"         # 启用动态IP地址
DEFROUTE="yes"
PROXY_METHOD="none"
BROWSER_ONLY="no"
IPV4_FAILURE_FATAL="no"
NAME="ens192"。         # 网卡名
UUID="b2ed67df-1641-4993-a727-9ba68f252da3" # UUID
DEVICE="ens192"         # 设备名称
ONBOOT="yes"            # 开机自启
```

1.2 重启网络

`service network restart `

1.3 检查网络

`ping www.baidu.com`

若能ping通，说明上网成功
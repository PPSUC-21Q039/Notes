# WireShark 入门笔记

## DHCP

### 基本信息

过滤条件：

```
_ws.col.protocol == "DHCP"
```

DHCP 的请求内容在 Option 50 里面。

![image-20231210015653494](img/WireShark.assets/image-20231210015653494.png)

### Transaction ID

![image-20231210020104729](img/WireShark.assets/image-20231210020104729.png)

有Release、Discover、Offer、Request、ACK等。

## DNS

过滤语句：

```
_ws.col.protocol == "DNS"
```

DNS 就是发去一个查询请求，然后response一个，内容就是TXT里面的，所以 24 帧的回复就是：`ACOOLDNSFLAG`

![image-20231210020633655](img/WireShark.assets/image-20231210020633655.png)

### 查看是哪个根服务器回复了

过滤DNS的回复：

```
dns.response_to
```

## SMB

查看打开的文件：

![image-20231210212837016](img/WireShark.assets/image-20231210212837016.png)

也可以在这个里面查看文件：

<img src="img/WireShark.assets/image-20231210213336448.png" alt="image-20231210213336448" style="zoom:67%;" />

### 登录状态码

![image-20231210213237907](img/WireShark.assets/image-20231210213237907.png)

### File smb.pcapng - What is the tree that is being browsed?

![image-20231210213523998](img/WireShark.assets/image-20231210213523998.png)

## TCP - Shell （明码）

![image-20231210214203580](img/WireShark.assets/image-20231210214203580.png)
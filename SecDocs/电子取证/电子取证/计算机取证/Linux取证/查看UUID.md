[Linux 中获取硬盘分区或文件系统的 UUID 的七种方法](https://zhuanlan.zhihu.com/p/62459117)
## **blkid**
```java
# blkid
/dev/sda1: UUID="d92fa769-e00f-4fd7-b6ed-ecf7224af7fa" TYPE="ext4" PARTUUID="eab59449-01"
/dev/sdc1: UUID="d17e3c31-e2c9-4f11-809c-94a549bc43b7" TYPE="ext2" PARTUUID="8cc8f9e5-01"
/dev/sdc3: UUID="ca307aa4-0866-49b1-8184-004025789e63" TYPE="ext4" PARTUUID="8cc8f9e5-03"
/dev/sdc5: PARTUUID="8cc8f9e5-05"
```
## **lsblk**
```java
# lsblk -o name,mountpoint,size,uuid
NAME   MOUNTPOINT  SIZE UUID
sda                 30G 
└─sda1 /            20G d92fa769-e00f-4fd7-b6ed-ecf7224af7fa
sdb                 10G 
sdc                 10G 
├─sdc1               1G d17e3c31-e2c9-4f11-809c-94a549bc43b7
├─sdc3               1G ca307aa4-0866-49b1-8184-004025789e63
├─sdc4               1K 
└─sdc5               1G 
sdd                 10G 
sde                 10G 
sr0               1024M
```
## **by-uuid**
```java
# ls -lh /dev/disk/by-uuid/
total 0
lrwxrwxrwx 1 root root 10 Jan 29 08:34 ca307aa4-0866-49b1-8184-004025789e63 -> ../../sdc3
lrwxrwxrwx 1 root root 10 Jan 29 08:34 d17e3c31-e2c9-4f11-809c-94a549bc43b7 -> ../../sdc1
lrwxrwxrwx 1 root root 10 Jan 29 08:34 d92fa769-e00f-4fd7-b6ed-ecf7224af7fa -> ../../sda1
```
## **hwinfo**
```java
# hwinfo --block | grep by-uuid | awk '{print $3,$7}'
/dev/sdc1, /dev/disk/by-uuid/d17e3c31-e2c9-4f11-809c-94a549bc43b7
/dev/sdc3, /dev/disk/by-uuid/ca307aa4-0866-49b1-8184-004025789e63
/dev/sda1, /dev/disk/by-uuid/d92fa769-e00f-4fd7-b6ed-ecf7224af7fa
```
## **udevadm**
```java
# udevadm info -q all -n /dev/sdc1 | grep -i by-uuid | head -1
S: disk/by-uuid/d17e3c31-e2c9-4f11-809c-94a549bc43b7
```
## **tune2fs**
```java
# tune2fs -l /dev/sdc1 | grep UUID
Filesystem UUID: d17e3c31-e2c9-4f11-809c-94a549bc43b7
```
## **dumpe2fs**
```java
# dumpe2fs /dev/sdc1 | grep UUID
dumpe2fs 1.43.5 (04-Aug-2017)
Filesystem UUID: d17e3c31-e2c9-4f11-809c-94a549bc43b7
```

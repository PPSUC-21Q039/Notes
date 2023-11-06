```bash
sudo sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
sudo apt-get update
apt-get install nfs-common -y
```


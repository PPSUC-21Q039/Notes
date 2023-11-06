## Nginx配置文件解析
[Nginx配置文件解析](https://mp.weixin.qq.com/s?__biz=Mzg3MjE1NjQ0NA==&mid=2247489260&idx=1&sn=dfbe2e060942d7f5deeebe874b321c6c&chksm=cef2ca9ff9854389e4b26e88efdbbe5352fd7b63bf5b2851983d82c54929f8422e923829084b&scene=178&cur_album_id=1895955433656254465#rd)<br />[万字长文看Nginx配置详解!](https://zhuanlan.zhihu.com/p/372610935)
#### Nginx配置文件示例
```nginx
# 全局块
user www-data;
worker_processes  2;  ## 默认1，一般建议设成CPU核数1-2倍
error_log  logs/error.log; ## 错误日志路径
pid  logs/nginx.pid; ## 进程id

# Events块
events {
  # 使用epoll的I/O 模型处理轮询事件。
  # 可以不设置，nginx会根据操作系统选择合适的模型
  use epoll;

  # 工作进程的最大连接数量, 默认1024个
  worker_connections  2048;

  # http层面的keep-alive超时时间
  keepalive_timeout 60;

  # 客户端请求头部的缓冲区大小
  client_header_buffer_size 2k;
}

# http块
http { 

  include mime.types;  # 导入文件扩展名与文件类型映射表
  default_type application/octet-stream;  # 默认文件类型

  # 日志格式及access日志路径
  log_format   main '$remote_addr - $remote_user [$time_local]  $status '
    '"$request" $body_bytes_sent "$http_referer" '
    '"$http_user_agent" "$http_x_forwarded_for"';
  access_log   logs/access.log  main;

  # 允许sendfile方式传输文件，默认为off。
  sendfile     on;
  tcp_nopush   on; # sendfile开启时才开启。

  # http server块
  # 简单反向代理
  server {
    listen       80;
    server_name  domain2.com www.domain2.com;
    access_log   logs/domain2.access.log  main;

    # 转发动态请求到web应用服务器
    location / {
      proxy_pass      http://127.0.0.1:8000;
      deny 192.24.40.8;  # 拒绝的ip
      allow 192.24.40.6; # 允许的ip   
    }

    # 错误页面
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
      root   html;
    }
  }

  # 负载均衡
  upstream backend_server {
    server 192.168.0.1:8000 weight=5; # weight越高，权重越大
    server 192.168.0.2:8000 weight=1;
    server 192.168.0.3:8000;
    server 192.168.0.4:8001 backup; # 热备
  }

  server {
    listen          80;
    server_name     big.server.com;
    access_log      logs/big.server.access.log main;

    charset utf-8;
    client_max_body_size 10M; # 限制用户上传文件大小，默认1M

    location / {
      # 使用proxy_pass转发请求到通过upstream定义的一组应用服务器
      proxy_pass      http://backend_server;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $http_host;
      proxy_redirect off;
      proxy_set_header X-Real-IP  $remote_addr;
    }

  }
}
```

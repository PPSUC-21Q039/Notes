### 镜像（image）
我们可以在Docker Hub上下载各种images，例如nginx，mysql，ubuntu等，也可以将自己的软件运行环境打包成一个image
### 容器（Container）
使用image来新建一个container<br />举个栗子：用一个Windows 7 iso镜像，可以给好多电脑安装系统。用一个MySQL Docker 镜像，可以创建好多个MySQL 容器
### Docker 入门
例如：<br />查阅Docker Hub内的[官方MySQL 文档](https://hub.docker.com/_/mysql)，首先下载MySQL镜像<br />docker pull mysql<br />如果要指定某个版本的MySQL，在mysql后加冒号指定版本，例如：<br />docker pull mysql:8.0.10<br />不指定版本则默认为latest（最新版）<br />等待下载完成，下载完成后查看目前已经下载好的images：<br />docker images<br />确认镜像已经下载成功，接下来使用这个镜像新建一个容器：<br />docker run --name first_mysql_container -p 23306:3306 -e MYSQL_ROOT_PASSWORD=yourpassword -d mysql<br />其中的命令和参数分别为：

- run：docker操作，用来新建容器；
- --name first_mysql_container：给容器命名，可选；
- -p 23306:3306：端口映射，将容器内的3306端口映射到主机的23306端口
- -e MYSQL_ROOT_PASSWORD=yourpassword：设置MySQL root密码
- -d ：容器创建后将会在后台运行，命令执行后返回一个container id
- mysql：使用mysql镜像，如果要指定版本，则写为 mysql:tag

使用命令 docker ps来查看已经创建的容器，Docker会显示以下详情：

- CONTAINER ID ：唯一的容器id，对应每一个单独的容器
- IMAGE：这个容器是使用什么镜像创建的
- COMMAND
- CREATED： 容器创建的时间
- STATUS：容器已经运行了或者停止了多长时间
- PORTS：端口映射情况
- NAMES：容器的名字

创建好容器之后，进入容器，亲手操作mysql：<br />docker exec -it first_mysql_container bash

- exec：docker命令，在运行的容器中执行命令
- -it：我一般都加上这两个参数
- first_mysql_container：容器名字，此处填容器ID亦可
- bash：在这个容器内运行bash

之后输入 mysql -u root -p 即可使用MySQL

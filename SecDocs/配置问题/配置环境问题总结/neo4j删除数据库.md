清空数据库方法如下
进入到neo4j存储数据库的目录，比如：~/Software/neo4j-community-4.3.3，然后：

关闭neo4j的服务
./bin/neo4j stop
1
进入到data的目录
cd data
1
删除neo4j的数据库（这是你要清空的数据库）
rm -rf databases/neo4j
rm -rf transactions/neo4j
1
2
重启neo4j服务
./bin/neo4j start
1
如果是企业版，可以新建一个完全清空的数据库
如果是社区版，在配置文件中如果默认是neo4j数据库，则会在没有这个数据库的时候自动新建一个这样的数据库
————————————————
版权声明：本文为CSDN博主「呆萌的代Ma」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_35757704/article/details/120233655
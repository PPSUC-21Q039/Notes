# WP
[（详解）[RoarCTF 2019]Easy Java_FPointzero的博客-CSDN博客](https://blog.csdn.net/m0_63705566/article/details/123214229)<br />[[RoarCTF 2019]Easy Java - 春告鳥 - 博客园](https://www.cnblogs.com/Cl0ud/p/12177085.html)
# 知识点
JAVA文件泄露
:::info
WEB-INF主要包含一下文件或目录： <br />/WEB-INF/web.xml：Web应用程序配置文件，描述了 servlet 和其他的应用组件配置及命名规则。 <br />/WEB-INF/classes/：含了站点所有用的 class 文件，包括 servlet class 和非servlet class，他们不能包含在 .jar文件中 <br />/WEB-INF/lib/：存放web应用需要的各种JAR文件，放置仅在这个应用中要求使用的jar文件,如数据库驱动jar文件 <br />/WEB-INF/src/：源码目录，按照包名结构放置各个java文件。 <br />/WEB-INF/database.properties：数据库配置文件
:::

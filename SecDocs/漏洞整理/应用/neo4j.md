## CVE-2021-34371

具体链接 [CVE-2021-34371](F:\vulhub\neo4j\CVE-2021-34371)

Neo4j是一个开源图数据库管理系统。

在Neo4j 3.4.18及以前，如果开启了Neo4j Shell接口，攻击者将可以通过RMI协议以未授权的身份调用任意方法，其中`setSessionVariable`方法存在反序列化漏洞。因为这个漏洞并非RMI反序列化，所以不受到Java版本的影响。

在Neo4j 3.5及之后的版本，Neo4j Shell被Cyber Shell替代。
